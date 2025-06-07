import logging
import os
from pathlib import Path
from datetime import datetime

MESSAGE_FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
TIME_FORMAT = "%Y-%m-%d %H:%M"


def setup_logger():
    appdata_path = Path(os.environ.get("LOCALAPPDATA", ""))
    current_time = datetime.now()
    timestamp = datetime.strftime(current_time, "%y_%m_%d_%H_%M")
    log_file = appdata_path / "cliboard-to-anki" / timestamp
    log_file = log_file.with_suffix(".log")

    log_file.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        format=MESSAGE_FORMAT,
        datefmt=TIME_FORMAT,
        encoding="utf-8",
        level=logging.DEBUG
    )
