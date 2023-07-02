# https://contest.yandex.ru/contest/27665/problems/H/


def get_letters_with_count(string: str) -> dict[str, int]:
    letters_with_count = {}
    for letter in string:
        if letter not in letters_with_count:
            letters_with_count[letter] = 0
        letters_with_count[letter] += 1
    return letters_with_count


def get_possible_occurrences_number_slow(word: str, sequence: str) -> int:
    possible_occurrences_number = 0
    word_length = len(word)
    sequence_length = len(sequence)
    word_letters_with_count = get_letters_with_count(word)

    base_sequence_fragment = sequence[:word_length - 1]

    for i in range(sequence_length - (word_length - 1)):
        sequence_fragment = base_sequence_fragment + \
            sequence[i + word_length - 1]
        fragment_letters_with_count = get_letters_with_count(sequence_fragment)
        if word_letters_with_count == fragment_letters_with_count:
            possible_occurrences_number += 1
        base_sequence_fragment = sequence_fragment[1:]
    return possible_occurrences_number


def get_possible_occurrences_number_fast(word: str, sequence: str):
    matching_letters_count = 0
    word_length = len(word)
    word_letters_with_count = get_letters_with_count(word)

    left_sliding_window_border = 0

    for index, character in enumerate(sequence):
        if index < word_length:
            left_sliding_window_border += 1
        else:
            pass
            # Мне надоело, я не понимаю эту задачу


def main():
    word_length, sequence_length = map(int, input().split())
    word, sequence = input(), input()

    result = get_possible_occurrences_number_fast(word, sequence)
    print(result)


if __name__ == '__main__':
    main()
