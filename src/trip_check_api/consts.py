import os
from dotenv import load_dotenv

load_dotenv()
AUTHKEY = os.getenv("TRIPCHECK_API_KEY")
PDX_BOUNDS = "-122.875228,45.414915,-122.631469,45.559331"
RAW_BUCKET_NAME = os.getenv("RAW_BUCKET_NAME")
