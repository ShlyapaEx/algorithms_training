# https://contest.yandex.ru/contest/44525/problems/B

# Версия 2. Работает исправно, но TL

def main():
    amount_of_sculptures, perfect_kg, minutes_left = map(int, input().split())
    sculptures_kg = list(map(int, input().split()))
    sculptures_sorted = sorted(sculptures_kg,
                               key=lambda a: abs(perfect_kg - a))
    result_count = 0
    result_indices = []

    for index, current_kg in enumerate(sculptures_sorted):
        if minutes_left >= 0:
            kg_added_or_deleted = abs(perfect_kg - current_kg)
            if kg_added_or_deleted <= minutes_left:
                result_count += 1
                found_index = sculptures_kg.index(current_kg)
                result_indices.append(found_index + 1)
                sculptures_kg[found_index] = -1
                minutes_left -= kg_added_or_deleted
    return result_count, result_indices


if __name__ == '__main__':
    result_count, result_indices = main()
    print(result_count)
    if result_count > 0:
        print(*result_indices)
