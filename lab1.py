def max_list_iter(int_list):  # must use iteration not recursion

    """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""

    try:
        if len(int_list) == 0:
            return None
        else:
            macks = int_list[0]
            for i in range(1, len(int_list)):
                if int_list[i] > macks:
                    macks = int_list[i]

            return macks
    except TypeError:
        raise ValueError


def reverse_rec(int_list):  # must use recursion

    """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
    if int_list is None or not int_list:
        raise ValueError

    else:
        if len(int_list) == 1:
            return int_list
        else:
            return [int_list[-1]] + reverse_rec(int_list[:-1])


def bin_search(target, low, high, int_list):  # must use recursion

    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    if int_list is None:
        raise ValueError
    try:
        mid = low + ((high - low) // 2)
        if int_list[low] == target:
            return low
        elif int_list[high] == target:
            return high
        elif int_list[mid] == target:
            return mid
        elif high - low <= 1:
            return None
        else:
            if target < int_list[mid]:
                return bin_search(target, low, mid - 1, int_list)
            else:
                return bin_search(target, mid + 1, high, int_list)
    except IndexError:
        return None
