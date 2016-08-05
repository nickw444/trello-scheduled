from .Base import Base
import sqlalchemy as sa
from sqlalchemy_utcdatetime import UTCDateTime
from sqlalchemy.orm import column_property

class RecurringCard(Base):
    __tablename__ = 'recurring_card'

    id = sa.Column(sa.Integer(), primary_key=True)

    title = sa.Column(sa.String(255))
    description = sa.Column(sa.Text())
    labels = sa.Column(sa.String(255))
    
    board = sa.Column(sa.String(255))
    list = sa.Column(sa.String(255))

    start = sa.Column(UTCDateTime())
    last_run = sa.Column(UTCDateTime())

    frequency = sa.Column(sa.Interval())
    frequency_kind = sa.Column(sa.Integer())
    frequency_val = sa.Column(sa.Integer())

    due_date_int = sa.Column(sa.Interval())

    next_run = column_property(last_run + frequency)

    user_id = sa.Column(sa.Integer(), sa.ForeignKey('user.id', ondelete='CASCADE'), 
                        nullable=False)
    user = sa.orm.relationship('User')

