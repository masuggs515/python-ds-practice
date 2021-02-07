def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_swap = to_swap.lower()
    msg = ""
    for char in phrase:
        if char.lower() == to_swap:
            if char.isupper():
               msg += char.lower()
            else:
               msg += char.upper()
        else:
            msg += char       
    return msg