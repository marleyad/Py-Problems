def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!

    # first try below:
    # float_nums = [num for num in nums if isinstance(num, float)]

    # total = 0

    # for num in float_nums:
    #     total += num
    
    # return total

    return sum([num for num in nums if isinstance(num, float)])


print(sum_floats([1, 2, 3]))