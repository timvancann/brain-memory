import logging
import re
from os.path import join, abspath, dirname
from typing import List, Dict

import eng_to_ipa as ipa
from yaml import load

major = {
    's': 0,
    'z': 0,
    't': 1,
    'd': 1,
    'θ': 1,
    'ð': 1,
    'n': 2,
    'm': 3,
    'r': 4,
    'l': 5,
    'ʧ': 6,
    'ʤ': 6,
    'ʃ': 6,
    'ʒ': 6,
    'k': 7,
    'g': 7,
    'f': 8,
    'v': 8,
    'p': 9,
    'b': 9
}
wordlist_path = join(abspath(dirname(__file__)), "./resources/wordlist.yaml")


def word_to_number(word: str) -> str:
    letters = major.keys()
    pattern = re.compile(rf"([{''.join(letters)}])\1*")
    converted = ipa.convert(word)
    groups = pattern.findall(converted)
    logging.debug(f'{word} -> {converted} -> {groups}')
    n = ''.join([str(major[_]) for _ in groups])
    return n


def _load_wordlist() -> Dict[str, List[str]]:
    with open(wordlist_path, 'r') as f:
        lst = load(f)
    return {_['number']: _['words'] for _ in lst}


def number_to_words(number: str) -> List[str]:
    if type(number) == int:
        number = str(number)
    if type(number != str):
        raise ValueError("Please provide a valid number")
    if len(number) > 2 or len(number) == 0:
        raise ValueError("Can only convert numbers between 0 and 99")

    wordlist = _load_wordlist()

    return wordlist[number]
