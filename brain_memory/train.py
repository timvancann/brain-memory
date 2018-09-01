import random
from typing import Tuple

from pymory.majorsystem import word_to_number, _load_wordlist


def _random_bool():
    return bool(random.getrandbits(1))


def _random_number() -> str:
    i = random.randint(0, 99)
    if (i < 10):
        return str(i) if _random_bool() else str(f'0{i}')
    return str(i)


def _random_word() -> str:
    wordlist = _load_wordlist()
    key = random.choice(list(wordlist.keys()))
    word = random.choice(wordlist[key])
    return word


def _ask_input(header: str, prefix: str):
    print(header)
    return input(prefix)


def _print_response(expr: bool, correct: str = 'correct!', wrong: str = 'nope'):
    if expr:
        print(correct)
    else:
        print(wrong)


def practice_to_word():
    n = _random_number()
    answer = _ask_input(header=f'convert: {n}',
                        prefix='a word: ')
    converted_answer = word_to_number(answer)

    _print_response(expr=converted_answer == n)


def practice_to_number():
    w = _random_word()
    answer = _ask_input(header=f'convert: {w}',
                        prefix='the number: ')
    converted_question = word_to_number(w)

    _print_response(answer == converted_question, wrong=f'not quite, correct number {converted_question}')
