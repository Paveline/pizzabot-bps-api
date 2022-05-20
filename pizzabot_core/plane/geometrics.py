def taxi_cub_distance(first, second):
    x_1, y_1 = first
    x_2, y_2 = second
    return max(abs(x_1 - x_2), abs(y_1 - y_2))


TAXI_CUB_GEOMETRY = {
    'distance': taxi_cub_distance,
    'moving_rules': {
        (0, 1): 'N',
        (0, -1): 'S',
        (-1, 0): 'W',
        (1, 0): 'E',
    }
}
