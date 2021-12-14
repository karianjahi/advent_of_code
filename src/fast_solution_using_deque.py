from collections import deque


def count_number_of_fish_after_n_days(laternfish_list, no_of_days):
    # init counts
    basket = deque([0] * 9)
    for laternfish in laternfish_list:
        basket[laternfish] += 1

    # run through days
    for each_day in range(no_of_days):
        basket[7] += basket[0]
        basket.rotate(-1)
    return sum(basket)

print(count_number_of_fish_after_n_days([3, 4, 3, 1, 2], 256))
