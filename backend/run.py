from Application import create_app
from config import get_config
from flask_script import Manager
from flask_migrate import MigrateCommand
import logging

logging.basicConfig(level=logging.DEBUG)

config = get_config()
app = create_app(config_obj=config)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
