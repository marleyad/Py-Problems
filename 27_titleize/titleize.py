def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    split_words = list(phrase.lower().split(' '))

    captialized_list = [word.capitalize() for word in split_words]

    return ' '.join(captialized_list)

print(titleize('this is awesome'))