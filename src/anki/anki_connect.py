"""This module contains functions for interacting with the anki connect api"""

import json
import logging

import requests

logger = logging.getLogger(__name__)

# TODO: replace these with reading from gui/config
ANKI_ADDRESS = "127.0.0.1"
ANKI_PORT = "8765"
NOTE_TYPE = "Basic-Japanese"
DECK = "anki connect test"
API_VERSION = 6
ADD_NOTE_ACTION = "addNote"


# TODO: pass in args instead of using constants
def add_note_to_deck(fields: list[str]):
    payload = format_add_note_request_payload(DECK, NOTE_TYPE, fields)
    url_str = f"http://{ANKI_ADDRESS}:{ANKI_PORT}"
    response = requests.post(url_str, payload, timeout=5)
    logger.debug(response)


def format_add_note_request_payload(
    deck_name: str, note_type: str, fields: list[str]
) -> str:
    payload = {
        "action": ADD_NOTE_ACTION,
        "version": API_VERSION,
        "params": {
            "note": {
                "deckName": deck_name,
                "modelName": note_type,
                # TODO: replace this with a query to the api
                "fields": {
                    "Vocab": fields[0],
                    "Reading": fields[1],
                    "Meaning": fields[2],
                },
                "options": {
                    "allowDuplicate": True,
                    "duplicateScope": "All",
                    "duplicateScopeOptions": {"checkAllModels": True},
                },
            },
        },
    }

    return json.dumps(payload)
