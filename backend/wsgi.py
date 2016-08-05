from Application import create_app
from config import get_config

app = create_app(config_obj=get_config())
