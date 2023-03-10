import os
from dotenv import load_dotenv
from pathlib import Path


base_dir = Path(__file__).resolve().parent
env_file = base_dir / '.env'
# print(env_file)
load_dotenv(env_file)


class Config:
    DEBUG = True
#     zapewnia autorestartowanie serwera w przypadku zmiany kodu
    SERET_KEY = os.environ.get('SECRET_KEY')
#     zapewnia bezpieczeństwo danych; niegdy w kodzie; nie udostepniamy publicznie;

# print(Config.SERET_KEY)