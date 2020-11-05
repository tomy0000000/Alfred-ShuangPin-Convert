# -*- coding: utf-8 -*-
"""Functions to be called by workflow"""
import json
import os

MAPPING_NAMES = ["independents", "initials", "vowels"]
LAYOUT_NAMES = ["zhuyin", "xiaohe", "microsoft"]
MAPPINGS = {}
DIRNAME = os.path.abspath(os.path.dirname(__file__))
for name in MAPPING_NAMES + LAYOUT_NAMES:
    with open(os.path.join(DIRNAME, "mappings", "%s.json" % name)) as f:
        MAPPINGS[name] = json.load(f)


def convert_layout(words, layout):
    if layout not in LAYOUT_NAMES:
        raise ValueError(layout)
    results = []
    for word in words:
        results.append("".join([MAPPINGS[layout][x] for x in word]))
    return results


def matching_sequence(text):
    begin = 0
    end = 6 if len(text) > 6 else len(text)
    results = []

    while begin != end:
        try:
            results.append(matching_word(text[begin:end]))
            begin = end
            end = begin + 6 if begin + 6 <= len(text) else len(text)
        except ValueError as error:
            if begin + 1 == end:
                raise error
            end -= 1

    return results


def matching_word(transcript):
    # Length Check
    if len(transcript) < 1 or len(transcript) > 6:
        raise ValueError("transcription length should be range from 1 to 6 chars")

    # Parse Independent first
    result = parse_independent(transcript)
    if result:
        return result

    # Then for combination
    result = parse_combination(transcript)
    if result:
        return result

    # Nothing left to parse
    raise ValueError("unmatched")


def parse_independent(transcript):
    # Length Check
    if len(transcript) > 4:
        return None

    # Parsing
    if transcript in MAPPINGS["independents"]:
        return [MAPPINGS["independents"][transcript]]

    # Length of 1 must be independent
    if len(transcript) == 1:
        raise ValueError("unmatched for 1 char")

    return None


def parse_combination(transcript):
    # Parse initials
    initial = None
    initial_end = 2
    while initial_end > 0:
        if transcript[:initial_end] in MAPPINGS["initials"]:
            initial = MAPPINGS["initials"][transcript[:initial_end]]
            break
        initial_end -= 1

    if not initial:
        return None

    # Parse vowels
    vowel = None
    if transcript[initial_end:] in MAPPINGS["vowels"]:
        vowel = MAPPINGS["vowels"][transcript[initial_end:]]
    else:
        return None

    return [initial, vowel]


if __name__ == "__main__":
    converted = matching_sequence(input("Pinyin Sequence: "))
    print(" ".join(convert_layout(converted, "zhuyin")))
    print(" ".join(convert_layout(converted, "xiaohe")))
