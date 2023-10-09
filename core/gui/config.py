import os
from dotenv import load_dotenv

load_dotenv()

# Trello GUI information
TRELLO_BASE_URL = os.getenv("TRELLO_BASE_URL")
TRELLO_USERNAME = os.getenv("TRELLO_USERNAME")
TRELLO_PASSWORD = os.getenv("TRELLO_PASSWORD")
