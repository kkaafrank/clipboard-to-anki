"""This module contains the main driver functions for starting the application"""

import atexit
import logging
import sys

import pyperclip
from PyHotKey import keyboard

import src.hotkey_functions.register_hotkey as register_hotkey
import src.logger.setup_logging as setup_logging
from src.anki.anki_connect import add_note_to_deck
from src.parser.tenten_parser import parse_tab_delimited_dictionary_entry

logger = logging.getLogger(__name__)


def main(_: list[str]) -> int:
    """Main driver function for"""
    is_hotkey_registered = register_hotkey.register_hotkey(
        lambda: add_note_to_deck(pyperclip.paste())
    )
    if not is_hotkey_registered:
        logger.error("Unable to register hotkey")
        return 1

    logger.debug("Hotkey registered")
    atexit.register(register_hotkey.unregister_all_hotkeys)
    keyboard.start_listener()

    # TODO: replace with gui event loop
    while True:
        pass

    keyboard.stop_listener()
    return 0


def add_10ten_card_to_anki():
    """Adds the copied tab delimited 10ten dictionary entry to anki"""
    card_fields = parse_tab_delimited_dictionary_entry(pyperclip.paste())
    add_note_to_deck(card_fields)


if __name__ == "__main__":
    setup_logging.setup_logger()
    sys.exit(main(sys.argv[1:]))
