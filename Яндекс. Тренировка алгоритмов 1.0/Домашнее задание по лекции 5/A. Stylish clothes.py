# https://contest.yandex.ru/contest/27794/problems/A/


def get_most_stylish_pair(tshirts: tuple[int], pants: tuple[int]):
    best_tshirt = tshirts[0]
    best_pants = pants[0]
    best_style = abs(tshirts[0] - pants[0])

    current_tshirt_index, current_pants_index = 0, 0

    while current_tshirt_index < len(tshirts) and current_pants_index < len(pants):
        current_tshirt = tshirts[current_tshirt_index]
        current_pants = pants[current_pants_index]

        pair_style = abs(current_tshirt - current_pants)
        if pair_style < best_style:
            best_style = pair_style
            best_tshirt = current_tshirt
            best_pants = current_pants

        if current_tshirt > current_pants:
            current_pants_index += 1
        else:
            current_tshirt_index += 1
    return best_tshirt, best_pants


def main():
    tshirts_count = int(input())
    tshirts = tuple(map(int, input().split()))
    pants_count = int(input())
    pants = tuple(map(int, input().split()))

    result = get_most_stylish_pair(tshirts, pants)
    print(*result)


if __name__ == '__main__':
    main()
