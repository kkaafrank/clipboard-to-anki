from dataclasses import dataclass, field
from enum import Enum


class ShortcutModifierKeys(Enum):
    SHIFT = "shift"
    ALT = "alt"
    CTRL = "ctrl"
    ALT_SHIFT = "alt-shift"
    ALT_CTRL = "alt-ctrl"
    CTRL_SHIFT = "ctrl-shift"
    CTRL_ALT_SHIFT = "ctrl_alt_shift"


@dataclass
class ShortcutSettings:
    modifier: ShortcutModifierKeys = field(default=ShortcutModifierKeys.ALT)
    key: str = field(default="d")
