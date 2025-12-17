# RijksBot – Wikidata Bot Approval Process

RijksBot is a bot that **updates existing Wikidata items** with Rijksmuseum IDs and related statements—it does not create new items.

This document outlines the steps taken to request approval for a Wikidata bot called **RijksBot**, which updates existing Wikidata items with Rijksmuseum IDs and related statements.

## Purpose

RijksBot is a Python bot designed to **add Rijksmuseum IDs (`P13234`) to existing Wikidata items** using the Wikidata OAuth API.  
The goal is to strengthen linked data between Wikidata and the Rijksmuseum collection while preserving existing information.

Key features:
- Batch processing of Wikidata items
- Non-destructive edits (only adds missing data)
- Adds Rijksmuseum ID and optional related statements: collection (`P195`), object number (`P217`), location (`P276`)
- Uses `pywikibot`
- Focused on data quality and consistency


## 1. Code preparation

The bot code was made publicly available to ensure transparency and enable community review:

**Repository:**  
`Jeroen-DeMeester/rijks-wikidata-bot`  
_A Python script for batch adding Rijksmuseum URIs to Wikidata using the OAuth API._

## 2. Testing environment

Before running on live Wikidata, the bot was tested extensively in the safe sandbox environment:

`https://test.wikidata.org/`

Testing confirmed:
- The script works as intended
- The Wikidata data model is respected
- No destructive or unsafe edits occur

## 3. Bot request page

An official request page was created:

`Wikidata:Requests for permissions/Bot/RijksBot`

The page includes:
- Task description
- Examples of edits
- Link to the source code
- Test results

## 4. Transclusion to the main requests page

Initially, the request was not visible in the list of current requests.  
A community member explained that the request must be **transcluded** on the main requests page:

`Wikidata:Requests for permissions/Bot`

By adding:

```wiki
{{Wikidata:Requests for permissions/Bot/RijksBot}}
```

the request appeared on the main page, making it visible to reviewers and the community.

## 5. Clarification about the Bot List

RijksBot did not appear in the large table listing other bots.  

This table:
- Is not a list of new requests
- Shows historical, approved, or archived bots

A bot only appears there after:
- Approval
- Administrative processing

So the absence from this table during review is normal.

## 6. Approval and results

After review, **RijksBot was approved by the Wikidata community**.  

Since approval, RijksBot has successfully updated **5367 Wikidata items**.  
- Rijksmuseum ID (`P13234`) is added if missing  
- Related statements (`P195`, `P217`, `P276`) are added only if absent  
- Existing information is never overwritten

Thanks to the constructive feedback from Wikipedian volunteers, the approval process was much smoother and more efficient.

## 7. Future potential

With the current setup, RijksBot can easily be extended to:
- Update additional Wikidata items
- Add other relevant properties
- Continue ensuring data quality and consistency

This makes the platform more valuable for researchers and the public alike.