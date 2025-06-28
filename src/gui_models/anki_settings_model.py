from dataclasses import dataclass, field


@dataclass
class AnkiSettings:
    anki_connect_ip: str = field(default="")
    anki_connect_port: str = field(default="")
    anki_deck: str = field(default="")
    anki_deck_options: list[str] = field(default_factory=list)
    anki_note_type: str = field(default="")
    anki_note_type_options: list[str] = field(default_factory=list)
