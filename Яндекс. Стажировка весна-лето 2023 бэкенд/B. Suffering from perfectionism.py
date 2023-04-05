# https://contest.yandex.ru/contest/44525/problems/B

# Версия 1. Валится на тесте 5 1 1
#                            6 8 2 1 1

def main():
    amount_of_sculptures, perfect_kg, minutes_left = map(int, input().split())
    sculptures_kg = list(map(int, input().split()))
    sculptures_sorted = sorted(sculptures_kg,
                               key=lambda a: abs(perfect_kg - a))
    result_count = 0
    result_indices = []

    index = 0
    while minutes_left >= 0 and index < amount_of_sculptures:
        kg_added_or_deleted = abs(perfect_kg - sculptures_sorted[index])
        if kg_added_or_deleted <= minutes_left:
            result_count += 1
            result_indices.append(sculptures_kg.
                                  index(sculptures_sorted[index]) + 1)

            minutes_left -= kg_added_or_deleted
        index += 1
    return result_count, set(result_indices)


if __name__ == '__main__':
    result_count, result_indices = main()
    print(result_count)
    if result_count > 0:
        print(*result_indices)
