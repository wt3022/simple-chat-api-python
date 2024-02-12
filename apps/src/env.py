from collections import namedtuple
import os

import dotenv


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(ROOT_DIR, ".env")
dotenv.load_dotenv(env_path)


_DatabaseValues = namedtuple("db", ("name", "user", "password", "host", "port"))
DB = _DatabaseValues(
    name=os.getenv("DB_NAME"),
    user=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
)

LONG_POLLING_TIMEOUT_SECONDS = int(os.getenv("LONG_POLLING_TIMEOUT_SECONDS"))
LONG_POLLING_LOOP_DELAY_SECONDS = int(os.getenv("LONG_POLLING_LOOP_DELAY_SECONDS"))


def __getattr__(x):
    return os.getenv(x, None)
