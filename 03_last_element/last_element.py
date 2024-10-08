def last_element(lst):
    """Return last item in the list (None if the list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    if lst == []:
        return None
    return lst[-1]

print(last_element([1, 2, 3, 4, 5, 6]))
