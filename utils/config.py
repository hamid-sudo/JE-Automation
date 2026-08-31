import os
from pathlib import Path

from dotenv import load_dotenv

env_file = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_file, override=True)

BASE_URL = os.getenv("BASE_URL")
JE_USERNAME = os.getenv("JE_USERNAME")
JE_PASSWORD = os.getenv("JE_PASSWORD")

if not all([BASE_URL, JE_USERNAME, JE_PASSWORD]):
    raise ValueError(
        "BASE_URL, JE_USERNAME, and JE_PASSWORD are required in the .env file."
    )



TEST_OWNER_NAME = os.getenv("TEST_OWNER_NAME")
TEST_EMAIL_PREFIX = os.getenv("TEST_EMAIL_PREFIX")
TEST_EMAIL_DOMAIN = os.getenv("TEST_EMAIL_DOMAIN")
TEST_ACCOUNT_PASSWORD = os.getenv("TEST_ACCOUNT_PASSWORD")

RUN_POS_TRANSACTION_TESTS = os.getenv("RUN_POS_TRANSACTION_TESTS", "false")
POS_COUNTER_NAME = os.getenv("POS_COUNTER_NAME")
POS_PRODUCT_NAME = os.getenv("POS_PRODUCT_NAME")