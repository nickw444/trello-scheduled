from .Base import Base
import sqlalchemy as sa
from sqlalchemy_utcdatetime import UTCDateTime
from flask_login import UserMixin

class User(Base, UserMixin):
    __tablename__ = 'user'
    id = sa.Column(sa.Integer(), primary_key=True)

    name = sa.Column(sa.String(255))
    email = sa.Column(sa.String(255))

    trello_id = sa.Column(sa.String(255), unique=True)
    trello_token = sa.Column(sa.String(255))

    cards = sa.orm.relationship('RecurringCard')
    
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return u'{}'.format(self.id)
