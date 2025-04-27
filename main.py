from random import randint
from math import inf


def gen_data(num: int) -> list:
    return [randint(1, 100) for i in range(1, num + 1)]


def find_min_max(
    data: list, start: int, end: int, min: int = inf, max: int = -inf
) -> tuple:
    """
    Recursively find the minimum and maximum values in a given list of numbers.

    Args:
      data (list): A list of numbers.
      start (int): The starting index of the slice of the list.
      end (int): The ending index of the slice of the list.
      min (int): The current minimum.
      max (int): The current maximum.

    Returns:
      tuple: A tuple containing the minimum and maximum values found in the given list.
    """
    if start == end:
        return min if data[start] >= min else data[start], (
            max if data[start] <= max else data[start]
        )

    middle = (start + end) // 2
    left_min, left_max = find_min_max(data, start, middle, min, max)
    right_min, right_max = find_min_max(data, middle + 1, end, min, max)
    
    return left_min if right_min > left_min else right_min, (
        left_max if right_max < left_max else right_max
    )


if __name__ == "__main__":
    data = gen_data(30)
    print(f"Data: {data}")

    the_min, the_max = find_min_max(data, 0, len(data) - 1)
    print(f"Find min: {the_min}, when min is {min(data)}")
    print(f"Find max: {the_max}, when max is {max(data)}")
