"""This module contains the main driver functions for starting the application"""

import atexit
import logging
import sys

from PyHotKey import keyboard

import src.hotkey_functions.register_hotkey as register_hotkey
import src.logger.setup_logging as setup_logging
from src.anki.anki_connect import add_note_to_deck

logger = logging.getLogger(__name__)


def main(_: list[str]) -> int:
    """Main driver function for"""
    is_hotkey_registered = register_hotkey.register_hotkey(add_note_to_deck)
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


if __name__ == "__main__":
    setup_logging.setup_logger()
    sys.exit(main(sys.argv[1:]))
