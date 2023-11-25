from dotenv import load_dotenv
import os

load_dotenv()

KEY = os.environ.get("KEY")
PATH_ENCODE_PHOTO = os.environ.get("PATH_ENCODE_PHOTO")
PATH_DEFAULT_PHOTO = os.environ.get("PATH_DEFAULT_PHOTO")
