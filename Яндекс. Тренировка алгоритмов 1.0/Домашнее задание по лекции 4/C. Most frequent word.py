# https://contest.yandex.ru/contest/27665/problems/C/

def get_most_frequent_word(text: str) -> str:
    words_with_count = {}
    words = text.split()

    most_frequent_word = words[0]
    max_word_count = 1
    for word in words:
        if word not in words_with_count:
            words_with_count[word] = 0
        words_with_count[word] += 1

        if words_with_count[word] > max_word_count \
                or (words_with_count[word] == max_word_count and word < most_frequent_word):
            max_word_count = words_with_count[word]
            most_frequent_word = word
    return most_frequent_word


def main():
    with open('input.txt', 'r', encoding='utf-8') as file:
        file_text = file.read()
    result = get_most_frequent_word(file_text)
    print(result)


if __name__ == '__main__':
    main()
