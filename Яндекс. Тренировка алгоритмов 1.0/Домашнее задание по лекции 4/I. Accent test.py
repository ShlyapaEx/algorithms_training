# https://contest.yandex.ru/contest/27665/problems/I/

def has_only_one_capital_letter(word: str):
    capital_letter_count = 0
    for character in word:
        if character.isupper():
            capital_letter_count += 1
        if capital_letter_count > 1:
            return False
    return True


def check_accents(accents: list[str], text: str):
    mistakes_count = 0
    accents_dictionary = {}

    for word in accents:
        word_as_key = word.lower()
        if word_as_key not in accents_dictionary:
            accents_dictionary[word_as_key] = {word}
        accents_dictionary[word_as_key].add(word)

    for text_word in text.split():
        word_as_key = text_word.lower()

        if text_word == word_as_key or not has_only_one_capital_letter(text_word):
            mistakes_count += 1
        elif word_as_key in accents_dictionary \
                and text_word not in accents_dictionary[word_as_key]:
            mistakes_count += 1

    return mistakes_count


def main():
    accents_count = int(input())
    accents = [None] * accents_count
    for i in range(accents_count):
        accents[i] = input()
    text = input()

    mistakes_count = check_accents(accents, text)
    print(mistakes_count)


if __name__ == '__main__':
    main()
