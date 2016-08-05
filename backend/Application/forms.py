from flask_wtf import Form
from wtforms import fields, validators

from wtforms.ext.dateutil.fields import DateTimeField
choice_options = [
    (1, 'Hours'),
    (24, 'Days'),
    (24 * 7, 'Weeks'),
    (24 * 7 * 365, 'Years'),
]

def is_in_future(date):
    pass

class CardForm(Form):
    title = fields.StringField(validators=[validators.Required()])
    description = fields.TextAreaField(validators=[validators.Optional()])
    labels = fields.StringField(validators=[validators.Optional()])
    
    board = fields.SelectField(validators=[validators.Required()], choices=[])
    list = fields.StringField(validators=[validators.Required()])

    start = DateTimeField(validators=[])
    frequency_kind = fields.SelectField('Frequency', choices=choice_options, 
                                        filters=[int], validators=[validators.Required()])
    frequency_val = fields.IntegerField('Frequency', 
                                        validators=[validators.NumberRange(min=1)])

    due_date = fields.IntegerField('Due date in minutes after scheduled creation', 
                                   validators=[validators.Optional(), 
                                               validators.NumberRange(min=1)])
    
    save = fields.SubmitField()
    delete = fields.SubmitField()
