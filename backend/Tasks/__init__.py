from twopi_flask_utils.celery import (
    create_celery, 
    create_db_session
)

from config import get_config
from models import RecurringCard

import logging
log = logging.getLogger(__name__)

config = get_config()
app = create_celery(__name__, config)
app.db_session = create_db_session(app)


def cron_task():
    # Only a single cron task should be running at a time...
    # Use MySQL as a mutex.

    # Find any cards where last_run + frequency_hours < now()
    # Update last_run to the new expected.

    app.db_session.query(RecurringCard).filter(
        
    )

    pass


@app.task
def create_card():
    pass