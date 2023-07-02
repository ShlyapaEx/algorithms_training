# https://contest.yandex.ru/contest/27665/problems/J/

import re
from typing import Literal


def keywithmaxval(d: dict):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]


def is_identifier(word: str, control_words: set, is_case_sensitive: bool,
                  can_start_with_number: bool) -> bool:
    if word.isnumeric() or (not can_start_with_number and word[0].isnumeric()) \
        or word in control_words \
            or (not is_case_sensitive and word.lower() in control_words):
        return False
    return True


def additional_cheat_checking(text: list[str], control_words: set,
                              is_case_sensitive: bool, can_start_with_number: bool):
    identifiers_with_count = {}

    for line_number, line in enumerate(text):
        for word_number, word in enumerate(line.split()):
            if not is_case_sensitive:
                word = word.lower()
            if is_identifier(word, control_words,
                             is_case_sensitive, can_start_with_number):
                if word not in identifiers_with_count:
                    identifiers_with_count[word] = 0
                identifiers_with_count[word] += 1

    return keywithmaxval(identifiers_with_count)


def yes_no_to_bool(string: Literal['yes', 'no']) -> bool:
    return True if string == 'yes' else False


def main():
    control_words = set()
    text = []
    with open('input.txt', 'r', encoding='utf-8') as file:
        file_lines = file.read().splitlines()
    first_line = file_lines[0].split()
    control_words_count = int(first_line[0])
    is_case_sensitive, can_start_with_number = yes_no_to_bool(first_line[1]), \
        yes_no_to_bool(first_line[2])

    for i in range(control_words_count):
        control_word = file_lines[i + 1]
        if not is_case_sensitive:
            control_word = control_word.lower()
        control_words.add(control_word)
    for i in range(control_words_count + 1, len(file_lines)):
        clean_string = re.sub(r"[^a-zA-Z0-9_ ]", ' ', file_lines[i]).strip()
        if clean_string != '':
            text.append(clean_string)
    result = additional_cheat_checking(text, control_words,
                                       is_case_sensitive, can_start_with_number)
    print(result)


if __name__ == '__main__':
    main()
