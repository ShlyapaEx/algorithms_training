# https://contest.yandex.ru/contest/27663/problems/D/

def count_unique_words():
    with open('input.txt', 'r', encoding='utf-8') as file:
        file_text = file.read()
    result = set(file_text.split())
    return len(result)


def main():
    result = count_unique_words()
    print(result)


if __name__ == '__main__':
    main()
