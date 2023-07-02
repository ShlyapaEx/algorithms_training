# https://contest.yandex.ru/contest/27663/problems/I/

def sort_languages_easy(_, students: list[set[str]]) -> tuple[set[str], set[str]]:
    intersected_languages = students[0].intersection(*students)
    all_languages = students[0].union(*students)

    return (intersected_languages, all_languages)


def sort_languages_hard(students_count: int, students: list[set[str]]) -> tuple[list[str], list[str]]:
    languages_with_count = {}
    intersected_languages = []
    all_languages = []

    for i in range(students_count):
        for language in students[i]:
            if language in languages_with_count:
                languages_with_count[language] += 1
            else:
                languages_with_count[language] = 1
  
    for language, students_know_count in languages_with_count.items():
        if students_count == students_know_count:
            intersected_languages.append(language)
        all_languages.append(language)

    return (intersected_languages, all_languages)

def main():
    students_count = int(input())
    students = []
    for _ in range(students_count):
        languages_count = int(input())
        students.append({input() for _ in range(languages_count)})
    results = sort_languages_easy(students_count, students)
    
    for result in results:
        print(len(result))
        for language in result:
            print(language)


if __name__ == '__main__':
    main()
