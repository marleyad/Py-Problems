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
    phrase_to_return = ''

    for char in phrase:
        if char.lower() == to_swap:
            char = char.swapcase()
        phrase_to_return += char
    
    return phrase_to_return
            

