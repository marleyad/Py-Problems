def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # Initialize an empty dictionary
    count_dict = {}

    # Count occurrences of each number
    for num in nums:
        count_dict[num] = count_dict.get(num, 0) + 1

    # Find the number with the maximum count
    max_count = 0
    mode_number = None
    for num, count in count_dict.items():
        if count > max_count:
            max_count = count
            mode_number = num

    return mode_number


print(mode([2, 2, 3, 3, 2]))