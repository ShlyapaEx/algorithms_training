# https://contest.yandex.ru/contest/27794/problems/C/

# TODO: Префиксные обратные подъёмы???

def create_prefix_ups(points_heights: list) -> list[int]:
    prefix_ups = [0] * (len(points_heights))

    for i in range(1, len(points_heights)):
        height_change = points_heights[i] - points_heights[i - 1]
        if height_change < 0:
            height_change = 0
        prefix_ups[i] += prefix_ups[i - 1] + height_change

    return prefix_ups


def create_reverse_prefix_ups(points_heights: list) -> list[int]:
    reverse_prefix_ups = [0] * (len(points_heights))

    for i in range(len(points_heights) - 2, -1, -1):
        height_change = points_heights[i] - points_heights[i + 1]
        if height_change < 0:
            height_change = 0
        reverse_prefix_ups[i] += reverse_prefix_ups[i + 1] + height_change

    return reverse_prefix_ups


def get_total_lift_heights(points_heights: list, tracks_descriptions: list[tuple]):
    results = []
    prefix_ups = create_prefix_ups(points_heights)
    reverse_prefix_ups = create_reverse_prefix_ups(points_heights)

    for track_data in tracks_descriptions:
        start_point = track_data[1] - 1
        finish_point = track_data[0] - 1

        if start_point > finish_point:
            results.append(prefix_ups[start_point] - prefix_ups[finish_point])
        else:
            results.append(reverse_prefix_ups[start_point]
                           - reverse_prefix_ups[finish_point])
    return results


def main():
    points_count = int(input())
    points_heights = []

    for _ in range(points_count):
        points_heights.append(tuple(map(int, input().split()))[1])

    tracks_count = int(input())
    tracks_descriptions = []

    for _ in range(tracks_count):
        tracks_descriptions.append(tuple(map(int, input().split())))

    results = get_total_lift_heights(points_heights, tracks_descriptions)
    for result in results:
        print(result)


if __name__ == '__main__':
    main()
