# https://contest.yandex.ru/contest/27665/problems/A/


def get_synonim(synonyms_pairs: list[str], word_to_find: str):
    first_to_second = {}
    second_to_first = {}

    for i in range(len(synonyms_pairs)):
        broken_pair = synonyms_pairs[i].split()
        first_to_second[broken_pair[0]] = broken_pair[1]
        second_to_first[broken_pair[1]] = broken_pair[0]

    result = first_to_second.get(word_to_find) \
        or second_to_first.get(word_to_find)
    return result


def main():
    pairs_count = int(input())
    synonyms_pairs = []
    for _ in range(pairs_count):
        synonyms_pairs.append(input())
    word_to_find = input()

    result = get_synonim(synonyms_pairs, word_to_find)
    print(result)


if __name__ == '__main__':
    main()
