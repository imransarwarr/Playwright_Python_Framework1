from dotenv import load_dotenv
import os

# Get absolute path of qa.env
env_path = os.path.join(os.path.dirname(__file__), "../config/qa.env")

# Load environment variables
load_dotenv(env_path)


class ConfigReader:

    QA_URL = os.getenv("QA_URL")
    USERNAME = os.getenv("APP_USERNAME")
    PASSWORD = os.getenv("APP_PASSWORD")
