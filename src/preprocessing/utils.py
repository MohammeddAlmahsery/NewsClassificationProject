def lower_and_special(x):
    """
    Lowercase and remove special characters from a string.
    
    params:
    x: string
    
    returns:
    string
    """    
    
    return ''.join([c.lower() for c in x if c.isalpha() or c == ' '])