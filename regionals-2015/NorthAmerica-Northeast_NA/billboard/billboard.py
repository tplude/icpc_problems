
import itertools

def find_max_poster(board_dimensions):
    widths = list(map(lambda x: x[0], board_dimensions))
    heights = list(map(lambda x: x[1], board_dimensions))

    optimal_sizes = []
    max_area = 0
    for size in itertools.product(widths,heights):
        area = size[0] * size[1]
        total_area = 0
        for board in board_dimensions:
            if size[0] <= board[0] and size[1] <= board[1]:
                total_area += area
        if total_area == max_area and total_area > 0:
            optimal_sizes.append((size[0], size[1]))
        elif total_area > max_area:
            max_area = total_area
            optimal_sizes = [(size[0], size[1])]
    print(optimal_sizes)
    widths_of_sols = list(map(lambda x: x[0], optimal_sizes))
    filtered_widths = list(filter(lambda x: x[0] == min(widths_of_sols), optimal_sizes))
    hts_of_filtered_widths = list(map(lambda x: x[1], filtered_widths))
    filtered_hts = list(filter(lambda x: x[1] == min(hts_of_filtered_widths), filtered_widths))
    if len(filtered_hts) == 0:
        print("0 0")
    else:
        print("{} {}".format(filtered_hts[0][0], filtered_hts[0][1]))

def main():
    num_problems = int(input())
    for p in range(num_problems):
        num_boards = int(input())
        board_dimensions = []
        for num in range(num_boards):
            dims = list(map(int, input().strip().split(' ')))
            board_dimensions.append(dims)
        find_max_poster(board_dimensions)

if __name__ == '__main__':
    main()
