from flask import render_template, current_app, url_for, request, redirect, abort
from flask_classy import FlaskView, route
from models import User, RecurringCard
from flask_login import login_user, current_user, logout_user
from .forms import CardForm
import json
import datetime

class IndexView(FlaskView):
    route_prefix = '/'

    def index(self):
        if current_user.is_authenticated:
            return redirect(url_for('IndexView:cards'))

        return render_template('index.html')

    def auth_callback(self):
        client_token = request.args.get('token')

        # Check the provided token is valid.
        token_user = current_app.trello.fetch_member('me', client_token)
        user_id = token_user['id']
        user_email = token_user['email']
        user_name = token_user['fullName']

        # Create/Update existing user...
        user = current_app.db.session.query(User).filter_by(trello_id=user_id).first()
        if user is None:
            # Make a user
            user = User(trello_id=user_id)
            current_app.db.session.add(user)

        # Update their details
        user.name = user_name
        user.email = user_email
        user.trello_token = client_token

        current_app.db.session.commit()

        # And log them in...
        login_user(user, remember=True)

        return redirect(url_for('IndexView:index'))

    def cards(self):
        # Fetch all cards for the current user
        return render_template('cards.index.html', cards=current_user.cards)

    def logout(self):
        logout_user()
        return redirect(url_for('IndexView:index'))

    @route('/cards/<int:card_id>', methods=['GET','POST'],endpoint='IndexView:cards_edit')
    @route('/cards/new', defaults={'card_id': None}, endpoint='IndexView:cards_new', methods=['GET','POST'])
    def card_edit(self, card_id):
        if card_id is None:
            card = None
            form = CardForm()
            del form.delete
        else:
            card = current_app.db.session.query(RecurringCard).get_or_404(card_id)
            if card.user != current_user:
                abort(403)
            form = CardForm(obj=card)

        form.board.choices = []

        member = current_app.trello.fetch_member(
            'me', current_user.trello_token, 
            fields='', boards='all', board_fields='name,closed')

        for board in member.get('boards', []):
            if not board['closed']:
                form.board.choices.append((board['id'], board['name']))

        if card_id is not None and form.delete.data:
            current_app.db.session.delete(card)
            current_app.db.session.commit()
            return redirect(url_for('IndexView:cards'))

        if form.validate_on_submit():
            if card is None:
                card = RecurringCard(user=current_user)
                current_app.db.session.add(card)

            card.title = form.title.data
            card.description = form.description.data
            card.labels = form.labels.data

            card.board = form.board.data
            card.list = form.list.data
            
            card.start = form.start.data
            card.frequency_kind = form.frequency_kind.data
            card.frequency_val = form.frequency_val.data

            card.frequency = datetime.timedelta(
                minutes=card.frequency_kind * card.frequency_val)

            card.due_date_int = datetime.timedelta(minutes=form.due_date.data)

            current_app.db.session.commit()
            return redirect(url_for('IndexView:cards'))

        return render_template('cards.single.html', form=form)

