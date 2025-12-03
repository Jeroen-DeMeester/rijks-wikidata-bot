# Rijksmuseum Uploader for Wikidata

This Python project automates the addition of **Rijksmuseum IDs** (property `P13234`) to Wikidata items from a CSV file. It leverages [Pywikibot](https://www.mediawiki.org/wiki/Manual:Pywikibot) to interact with Wikidata safely.

## Table of Contents

- [Project Overview](#project-overview)  
- [Requirements](#requirements)  
- [Setup](#setup)  
- [CSV Format](#csv-format)  
- [Test Connection (optional but recommended)](#test-connection-optional-but-recommended)  
- [Usage](#usage)  
- [Logging](#logging)  
- [Best Practices](#best-practices)  
- [Troubleshooting](#troubleshooting)  


## Project Overview

The goal of this project is to ensure that Wikidata items for artworks or objects in the Rijksmuseum collection have the correct Rijksmuseum ID (`P13234`). The script reads a CSV file containing:

- `qid`: Wikidata item ID (e.g., `Q100905723`)  
- `uri`: Rijksmuseum URI (e.g., `https://id.rijksmuseum.nl/200122652`)  

The script will:

1. Validate the URI format (`https://id.rijksmuseum.nl/200...`)  
2. Skip rows with missing data or invalid URIs  
3. Check if the item already has `P13234`  
4. Add the claim if missing  
5. Log successes and failures to a timestamped log file  

## Requirements

- Python 3.14+  
- Pywikibot (install via `pip install pywikibot` or include in `requirements.txt`)
- Access to a Wikidata account (test or live environment)  

Optional modules are part of the standard library (`csv`, `re`, `os`, `logging`, `datetime`).  

## Setup

1. **Clone the repository**  

```bash
git clone https://github.com/<your-username>/rijks-wikidata-bot.git
cd rijks-wikidata-bot
```

2. **Create a Python virtual environment and activate it**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install the required package(s)**

```bash
pip install -r requirements.txt
```

4. **Generate user configuration**

To run the bot, you need a `user-config.py` file in the project root. This file tells Pywikibot which Wikidata site to connect to and which bot account to use.

Create a `user-config.py` with the following content: 

```python
from collections import defaultdict  # needed for Pywikibot usernames

# ---- CHOOSE YOUR ENVIRONMENT ----
# For test.wikidata.org use:
# mylang = 'test'
#
# For live Wikidata use:
# mylang = 'wikidata'

family = 'wikidata'
mylang = 'test'  # change to 'wikidata' for live use

# Bot usernames
usernames = defaultdict(dict)
usernames['wikidata'][mylang] = '<YourBotName>'  # replace with your bot username

# Optional: path to a file storing passwords for your bot
password_file = None
```
Make sure you have permission to run a bot on Wikidata before performing live edits.

## CSV Format

The input CSV should have **two columns**:

```bash
qid,uri
Q100905723,https://id.rijksmuseum.nl/200122652
Q102304818,https://id.rijksmuseum.nl/200122530
```

The `qid` column must contain the Wikidata QID.

The `uri` column must start with `https://id.rijksmuseum.nl/200...`.

Only the numeric part after `nl/` will be stored as the property value. Rows with missing QID or invalid URI are skipped automatically.

A demo file `rijks_uris_demo.csv` is included in this repository as an example.

## Test Connection (optional but recommended)

Before running the full batch, you can verify that Pywikibot is correctly configured and can connect to Wikidata.

Run the script:

```bash
python test-connection.py
```

If the configuration is correct, the script will confirm a successful connection to the target environment (test or live), based on your `user-config.py`.

## Usage

Ensure `user-config.py` points to the correct environment (wikidata or test).

Replace the contents of `rijks_uris.csv` with your own data, based on the format shown in `rijks_uris_demo.csv`.

Run the script:

```bash
python batch_wiki_rijksObject.py
```

The script will add `P13234` claims for valid rows in the CSV.

## Logging

All logs are saved in the logs/ directory with a timestamp:

```bash
logs/rijks_upload_YYYY-MM-DD_HH-MM-SS.log
```

Each run logs:
- Total rows processed
- Successful additions
- Failures or skipped rows
- Individual item messages

## Best Practices

- **Test first**: Always test on [test.wikidata.org](https://test.wikidata.org)
 before writing live.
- **Start small:** Begin by uploading a few items to ensure everything works as expected. Only scale up to larger batches once you are confident. 

- **Check existing claims:** The script automatically skips items that already have the `P13234` property to avoid duplicates.

- **Rate limiting:** Pywikibot respects Wikidata's server limits (maxlag) out of the box. No manual `time.sleep` is needed for normal usage.

## Troubleshooting

Common issues:

- **Incorrect user-config.py**: Make sure your `user-config.py` exists in the project root and contains the correct family, mylang, and username.  
- **Item does not exist**: If a QID does not exist in the target environment (live or test), you must create it manually before adding claims.
- **Rate limit / maxlag errors**: Pywikibot automatically handles retries when the server signals maxlag. No additional `time.sleep()` is required for standard batch sizes.


**Author:** Jeroen De Meester  
**Repository:** [https://github.com/Jeroen-DeMeester/rijks-wikidata-bot](https://github.com/Jeroen-DeMeester/rijks-wikidata-bot)