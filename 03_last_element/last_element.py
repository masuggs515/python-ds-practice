def last_element(lst):
    last = len(lst) -1
    if len(lst) == 0:
        return None
    return lst[last]
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """