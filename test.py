# Importeer de benodigde modules
from dotenv import load_dotenv # Om variabelen uit een .env bestand te laden
import os # Om toegang te krijgen tot systeem- en omgevingsvariabelen

# Laad het .env bestand. Hierdoor worden alle variabellen uit .env beschikbaar
load_dotenv()

# Haal waarden uit .env (Wikidata API OAuth 1.0 keys)
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

# print Hello world as test
print('Hello world')