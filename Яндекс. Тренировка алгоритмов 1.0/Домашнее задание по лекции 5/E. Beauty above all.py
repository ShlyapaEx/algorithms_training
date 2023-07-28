# https://contest.yandex.ru/contest/27794/problems/E/


def get_min_length_section(trees_sorts: int, trees: list[int]):
    # TIME LIMIT EXTENDED :(
    min_start = len(trees) + 1
    min_end = len(trees) + 1
    min_len = len(trees) + 1

    end = 0
    # checked_range = [0, trees[0]]
    unique_checked_range = {trees[0], }
    for start in range(1, len(trees) - trees_sorts + 1):
        removed_value = trees[start]
        if trees[start + 1] != removed_value:
            unique_checked_range.remove(removed_value)
        # start_value = checked_range.pop(0)
        # if start_value not in checked_range:

        while len(unique_checked_range) != trees_sorts and end < len(trees) - 1:
            end += 1
            unique_checked_range.add(trees[end])
        if len(unique_checked_range) == trees_sorts:
            new_len = end - start + 1
            if new_len < min_len:
                min_start, min_end, min_len = start, end, new_len
            if new_len == trees_sorts:
                break
    return (min_start + 1, min_end + 1)


def main():
    # trees_count, trees_sorts = map(int, input().split())
    # trees = list(map(int, input().split()))
    trees_sorts = 5
    trees = [5, 5, 4, 3, 3, 2, 1, 2, 5, 5, 1, 2, 3, 4, 5]
    result = get_min_length_section(trees_sorts, trees)
    print(*result)


if __name__ == '__main__':
    main()
