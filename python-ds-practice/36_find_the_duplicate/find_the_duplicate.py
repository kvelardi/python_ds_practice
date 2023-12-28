def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """

    # create a set to store the nums
    num_set = set()

    # loop over the nums
    for num in nums:

        # if the num is in the set, return it
        if num in num_set:
            return num

        # otherwise, add it to the set
        else:
            num_set.add(num)

    # if we get here, there was no duplicate
    return None