import pywikibot

# Connect using settings from user-config.py
site = pywikibot.Site()  # family/mylang automatically loaded

try:
    print(f"Connected to {site}")
    print(f"Version: {site.version()}")
except Exception as e:
    print(f"Connection failed: {e}")
