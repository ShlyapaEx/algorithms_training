# https://contest.yandex.ru/contest/27665/problems/B/


def get_words_count(text: str) -> list[int]:
    cum_words_count = []
    words_count = {}
    words = text.split()

    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 0
        cum_words_count.append(words_count[word])
    return cum_words_count


def main():
    with open('input.txt', 'r', encoding='utf-8') as file:
        file_text = file.read()
    result = get_words_count(file_text)
    print(*result)


if __name__ == '__main__':
    main()
