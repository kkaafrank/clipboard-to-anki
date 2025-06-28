from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path


class ParserType(Enum):
    TEN_TEN = "10ten"
    PYTHON = "python"
    CUSTOM = "custom"


@dataclass
class ParserSettings:
    parser_type: ParserType = field(default=ParserType.TEN_TEN)
    should_only_add_tenten_first_spelling: bool = field(default=True)
    should_only_add_tenten_first_pronunciation: bool = field(default=True)
    should_remove_parts_of_speech: bool = field(default=True)
    custom_parser_path: Path = field(default=Path(""))
