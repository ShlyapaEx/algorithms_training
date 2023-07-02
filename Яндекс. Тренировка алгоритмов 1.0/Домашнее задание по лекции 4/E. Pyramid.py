# https://contest.yandex.ru/contest/27665/problems/E/


def get_max_pyramid_height(all_blocks_widths: list, all_blocks_heights: list):
    max_block_width = max(all_blocks_widths)
    widthest_block_height = all_blocks_heights[all_blocks_widths
                                               .index(max_block_width)]

    pyramid_blocks = {max_block_width: widthest_block_height}

    for i in range(len(all_blocks_widths)):
        if all_blocks_widths[i] not in pyramid_blocks \
                or all_blocks_heights[i] > pyramid_blocks[all_blocks_widths[i]]:
            pyramid_blocks[all_blocks_widths[i]] = all_blocks_heights[i]

    return sum(pyramid_blocks.values())


def main():
    blocks_amount = int(input())
    all_blocks_widths = [0] * blocks_amount
    all_blocks_heights = [0] * blocks_amount
    for i in range(blocks_amount):
        all_blocks_widths[i], all_blocks_heights[i] = map(int, input().split())

    result = get_max_pyramid_height(all_blocks_widths, all_blocks_heights)
    print(result)


if __name__ == '__main__':
    main()
