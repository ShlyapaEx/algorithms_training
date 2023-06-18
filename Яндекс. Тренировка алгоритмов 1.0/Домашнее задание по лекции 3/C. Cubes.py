# https://contest.yandex.ru/contest/27663/problems/C/

def get_intersection_of_sets(set_1: set[int], set_2: set[int]) -> set[int]:
    result = set()
    for number in set_1:
        if number in set_2:
            result.add(number)
    return result


def get_difference_of_sets(set_1: set[int], set_2: set[int]) -> set[int]:
    result = set()
    for number in set_1:
        if number not in set_2:
            result.add(number)
    return result


def process_cubes_shenanigans(ann_cubes_count: int, boris_cubes_count: int):
    ann_cubes_set, boris_cubes_set = set(), set()
    for _ in range(ann_cubes_count):
        ann_cubes_set.add(int(input()))
    for _ in range(boris_cubes_count):
        boris_cubes_set.add(int(input()))

    similar_cubes = get_intersection_of_sets(ann_cubes_set, boris_cubes_set)
    left_ann_cubes = get_difference_of_sets(ann_cubes_set, similar_cubes)
    left_boris_cubes = get_difference_of_sets(boris_cubes_set, similar_cubes)

    print(len(similar_cubes))
    print(*sorted(similar_cubes))

    print(len(left_ann_cubes))
    print(*sorted(left_ann_cubes))

    print(len(left_boris_cubes))
    print(*sorted(left_boris_cubes))


def main():
    ann_cubes_count, boris_cubes_count = map(int, input().split())
    process_cubes_shenanigans(ann_cubes_count, boris_cubes_count)


if __name__ == '__main__':
    main()
