# https://contest.yandex.ru/contest/27663/problems/I/

def sort_languages(students_count: int, students: list[tuple[str]]):
    pass


def main():
    students_count = int(input())
    students = []
    for _ in range(students_count):
        languages_count = int(input())
        students.append(tuple(input() for _ in range(languages_count)))
    result = sort_languages(students_count, students)


def fuck():
    students_count = int(input())
    languages = {}
    languages_known_by_all = []
    left_languages = []
    for _ in range(students_count):
        language_count = int(input())
        for _ in range(language_count):
            new_language = input()
            if new_language in languages.keys():
                languages[new_language] += 1
            else:
                languages[new_language] = 1
    for key, item in languages.items():
        if item == students_count:
            languages_known_by_all.append(key)
        left_languages.append(key)

    print(len(languages_known_by_all))
    for i in range(len(languages_known_by_all)):
        print(languages_known_by_all[i])
    print(len(left_languages))
    for i in range(len(left_languages)):
        print(left_languages[i])


if __name__ == '__main__':
    fuck()
