# https://contest.yandex.ru/contest/27665/problems/J/

import re
from typing import Literal


def keywithmaxval(words: dict):
    most_frequent_word = ''
    most_frequent_word_count = 0
    most_frequent_word_first_line = 0
    most_frequent_word_first_row = 0
    for word in words:
        if words[word]['word_count'] > most_frequent_word_count:
            most_frequent_word = word
            most_frequent_word_count = words[word]['word_count']
            most_frequent_word_first_line = words[word]['first_met_line']
            most_frequent_word_first_row = words[word]['first_word_number']
        elif words[word]['word_count'] == most_frequent_word_count:
            if words[word]['first_met_line'] < most_frequent_word_first_line \
                    or words[word]['first_word_number'] < most_frequent_word_first_row:
                most_frequent_word = word
                most_frequent_word_count = words[word]['word_count']
                most_frequent_word_first_line = words[word]['first_met_line']
                most_frequent_word_first_row = words[word]['first_word_number']
    return most_frequent_word


def is_identifier(word: str, control_words: set, is_case_sensitive: bool,
                  can_start_with_number: bool) -> bool:
    if word.isnumeric():
        return False
    if not can_start_with_number:
        if word[0].isnumeric():
            return False
    if not is_case_sensitive:
        if word.lower() in control_words:
            return False
    elif word in control_words:
        return False
    return True


def additional_cheat_checking(text: list[str], control_words: set,
                              is_case_sensitive: bool, can_start_with_number: bool):
    identifiers_with_count = {}
    # most_frequent_identifier_count = 0

    for line_number, line in enumerate(text):
        for word_number, word in enumerate(line.split()):
            if not is_case_sensitive:
                word = word.lower()
            if is_identifier(word, control_words,
                             is_case_sensitive, can_start_with_number):
                if word not in identifiers_with_count:
                    identifiers_with_count[word] = {'word_count': 0,
                                                    'first_met_line': line_number,
                                                    'first_word_number': word_number}
                identifiers_with_count[word]['word_count'] += 1

    return keywithmaxval(identifiers_with_count)


def yes_no_to_bool(string: Literal['yes', 'no']) -> bool:
    return True if string == 'yes' else False


# assert additional_cheat_checking(set(), True, False, '''int main() {
#   int a;
#   int b;
#   scanf("%d%d", &a, &b);
#   printf("%d", a + b);
# }'''.split()) == 'int'
# assert additional_cheat_checking(set(), True, False, '''#define INT int
# int main() {
#   INT a, b;
#   scanf("%d%d", &a, &b);
#   printf("%d %d", a + b, 0);
# }'''.split()) == 'd'
# assert additional_cheat_checking(set(), False, False, '''#define INT int
# int main() {
#   INT a, b;
#   scanf("%d%d", &a, &b);
#   printf("%d %d", a + b, 0);
# }'''.split()) == 'int'
# assert additional_cheat_checking({'program', 'var', 'begin', 'end', 'while', 'for'}, False, False, '''program sum;
# var
#   A, B: integer;
# begin
#   read(A, b);
#   writeln(a + b);
# end.'''.split()) == 'a'
# assert additional_cheat_checking({'_'}, True, True, '''a = 0h
# b = 0h
# c = 0h'''.split()) == '0h'
# assert additional_cheat_checking({'a'}, False, False, '''A b a a a
# b b b B a'''.split()) == 'b'
# assert additional_cheat_checking({'b'}, False, False, '''A b a a a
# b b b B a'''.split()) == 'a'
# assert additional_cheat_checking({'a', 'b'}, True, False, '''A b a a a
# b b b B a'''.split()) == 'A'
# assert additional_cheat_checking(
#     set(), False, False, '''a b c c'''.split()) == 'c'
# assert additional_cheat_checking(set(), True, False, '''3abc 3abc 3abc
# AbC  AbC  AbC
# abc  abc  abc'''.split()) == 'AbC'


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
