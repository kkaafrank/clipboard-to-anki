"""This module contains functions for parsing copied 10Ten dictionary entries"""

import logging
import re

MULTI_DEFINITIONS_REGEX = r"(\(\d+\))"
PARENTHESES_REGEX = r"(\(.*?\))"

logger = logging.getLogger(__name__)


def parse_tab_delimited_dictionary_entry(entry: str) -> tuple[str, str, str]:
    """Parses a tab-delimited 10Ten dictionary entry

    Args:
        entry: the copied 10Ten dictionary entry

    Returns:
        word, pronunciation, and definition section
    """
    # separate dictionary fields
    logger.debug("Parsing %s", entry)
    word, pronunciation, definition = entry.split("\t")

    # parse word and pronunciation entry
    word_field = parse_word_or_pronunciation_section(word)
    pronunciation_field = parse_word_or_pronunciation_section(pronunciation)

    # parse definition entry
    definition_field = parse_definition_section(definition)

    logger.debug(
        "Parsed to %s, %s, %s", word_field, pronunciation_field, definition_field
    )
    return word_field, pronunciation_field, definition_field


# TODO: add additional parameter for how to parse this entry
def parse_word_or_pronunciation_section(word_or_pronunciation: str) -> str:
    """Parses the word or pronunciation section of a 10Ten dictionary entry.
    Currently only returns the first part of the word or pronunciation section.
    This is usually the most common way to write/pronounce the word.

    Args:
        word_entry: word or pronunciation section

    Returns:
        A cleaned up version of the word or pronunciation section
    """
    word_or_pronunciation = word_or_pronunciation.replace(" ", "")
    words = word_or_pronunciation.split(";")
    return words[0]


# TODO: add additional parameter for how to parse this entry
def parse_definition_section(definition_entry: str) -> str:
    """Parses the definition section of a 10Ten dictionary entry

    Args:
        definition_entry: definition section of the 10Ten dictionary entry

    Returns:
        A string containing each dictionary entry separated by a line break
    """
    definitions = get_multiple_definition_strings(
        definition_entry,
    )

    cleaned_definitions = []
    for definition in definitions:
        def_no_parts_of_speech = re.sub(PARENTHESES_REGEX, "", definition)
        def_no_parts_of_speech = def_no_parts_of_speech.strip()
        cleaned_definitions.append(def_no_parts_of_speech)

    return "<br>".join(cleaned_definitions)


def get_multiple_definition_strings(
    definition_string: str,
) -> list[str]:
    """Parses a 10Ten dictionary entry into each definition.

    Args:
        definition_string: the definition part of the dictionary entry with multiple definitions

    Returns:
        list of each definition as a separate item in the list
    """
    multi_defs_match_iter = re.finditer(MULTI_DEFINITIONS_REGEX, definition_string)
    group_matches = list(multi_defs_match_iter)

    if not group_matches:
        return [definition_string]

    num_groups = len(group_matches)
    definition_string_len = len(definition_string)

    definitions = []
    for group_index, match_obj in enumerate(group_matches):
        definition_start_index = match_obj.end()
        definition_end_index = definition_string_len
        if group_index + 1 != num_groups:
            definition_end_index = group_matches[group_index + 1].start()

        definitions.append(
            definition_string[definition_start_index:definition_end_index]
        )

    return definitions
