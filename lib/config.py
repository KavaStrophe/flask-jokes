
from dotenv import load_dotenv
import os

load_dotenv()


class Environment:
    db_uri: str = os.getenv('SQLALCHEMY_DATABASE_URI')
    remote_joke_type: str = os.getenv('REMOTE_JOKE_TYPE') if os.getenv('REMOTE_JOKE_TYPE') != None else "chuck_norris_jokes"
    api_paging_default_per_page: int = int(os.getenv('API_PAGING_DEFAULT_PER_PAGE')) if os.getenv(
        'API_PAGING_DEFAULT_PER_PAGE') != None else 20
    api_paging_default_page: int = int(os.getenv('API_PAGING_DEFAULT_PAGE')) if os.getenv(
        'API_PAGING_DEFAULT_PAGE') != None else 1
