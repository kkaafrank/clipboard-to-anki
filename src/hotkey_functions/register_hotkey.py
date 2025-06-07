"""Module for registering (and unregistering) hot keys"""

from typing import Callable

from PyHotKey import Key, keyboard


def register_hotkey(function_to_bind: Callable) -> bool:
    """Registers a hotkey to the function passed in

    Args:
        function_to_bind: the function to bind to the hotkey

    Returns:
        bool: whether or not the hotkey was successfully registered
    """
    # TODO: read config file/gui for hotkey to use
    hotkey_id = keyboard.register_hotkey(
        keys=[Key.alt_l, "d"],
        count=None,
        func=function_to_bind,
    )

    if hotkey_id == -1:
        return False

    return True


def unregister_all_hotkeys():
    """Unregisters all hotkeys"""
    keyboard.unregister_all_hotkeys()
