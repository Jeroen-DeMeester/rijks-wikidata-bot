import csv  # Module for reading CSV files
import re   # Module for regular expressions (used to validate Rijksmuseum URIs)
import os # To access system and environment variables
import pywikibot  # Python library for interacting with Wikidata/Wikipedia
import logging # To log messages, warnings and errors to a log file
from datetime import datetime  # work with dates and times

# Wikidata property we want to set: P13234 = Rijksmuseum ID
PROPERTY = "P13234"

# Input CSV containing QIDs and Rijksmuseum URIs
CSV_FILE = "rijks_uris.csv"

# Setup logging
# Create a 'logs' directory if it does not exist
os.makedirs("logs", exist_ok=True)
# Create a timestamped logfile to avoid overwriting previous runs
# Format: rijks_upload_YYYY-MM-DD_HH-MM-SS.log
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
LOG_FILE = os.path.join("logs", f"rijks_upload_{timestamp}.log")

logging.basicConfig(
    filename=LOG_FILE, # path to log file
    filemode="w",  # overwrite log file each run
    format="%(asctime)s - %(levelname)s - %(message)s", # log line structure (timestamp, level, message)
    level=logging.INFO # store INFO, WARNING, ERROR, CRITICAL messages
)

# Initialize counters for summary logging
total_rows = 0
success_count = 0  # count of successes
fail_count = 0     # count of failures

# Connect to the Wikidata site via Pywikibot
site = pywikibot.Site()  # Pywikibot haalt family/mylang uit user-config.py
repo = site.data_repository()  # Access the data repository for Wikidata items

# Define regex to validate the Rijksmuseum URI format
# Must start with "https://id.rijksmuseum.nl/200..." 
RIJKS_REGEX = re.compile(r"^https://id\.rijksmuseum\.nl/(200\d+)$")

# Function to check if a Wikidata item already has a given property
def has_property(item, pid):
    # Returns True if the item already has the property (claim) defined
    return pid in item.claims

# Open the CSV file for reading
# Using utf-8 encoding to avoid encoding issues
with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)  # Treat first row as header, map columns to names
    rows = list(reader)  # Convert iterator to list for easier counting
    total_rows = len(rows)
    logging.info(f"Total rows in CSV: {total_rows}")

    # Loop through each row in the CSV
    for row in rows:
        qid = row.get("qid", "").strip()  # Get QID, remove leading/trailing spaces
        uri = row.get("uri", "").strip()  # Get URI, remove leading/trailing spaces

        # Skip rows with missing QID or URI
        if not qid or not uri:
            logging.warning(f"Skipping incomplete row: {row}")
            fail_count += 1
            continue

        # Validate the Rijksmuseum URI using the regex
        match = RIJKS_REGEX.match(uri)
        if not match:
            # Log a warning if URI does not match expected format
            logging.warning(f"{qid}: Invalid Rijks URI format — {uri}")
            fail_count += 1
            continue

        # Extract the actual Rijksmuseum ID (the 200... number) from the URI
        rijks_id = match.group(1)

        try:
            # Load the Wikidata item
            item = pywikibot.ItemPage(repo, qid)
            item.get()  # Retrieve all data for this item

            # Skip if the property already exists
            if has_property(item, PROPERTY):
                if any(
        				claim.getTarget() != rijks_id and
        				claim.getRank() != 'deprecated'
        			for claim in item.claims[PROPERTY]
        		):
			        logging.warning(f"{qid}: {PROPERTY} has a different value than {rijks_id}")
                else:
                    logging.info(f"{qid}: {PROPERTY} already exists — skipped")
                continue

            # Create a new claim for the property
            claim = pywikibot.Claim(repo, PROPERTY)
            claim.setTarget(rijks_id)  # Set the claim target to the Rijksmuseum ID

            # Real write according to user-config.py settings
            item.addClaim(claim)
            logging.info(f"{qid}: ✅ P13234 set to {rijks_id}")
            success_count += 1

        except Exception as e:
            # Catch and log any exceptions while processing the item
            logging.error(f"{qid}: Error — {e}")
            fail_count += 1

# ====================================================
# --- Log summary of run ---
# ====================================================
logging.info("=== Run summary ===")
logging.info(f"Total rows processed: {total_rows}")
logging.info(f"Successful: {success_count}")
logging.info(f"Failures/skipped: {fail_count}")
logging.info("=== End of run ===")

print(f"Log written to {LOG_FILE}")
