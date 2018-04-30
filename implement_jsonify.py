# Implement JSONify

# {'a': {'b':1}}

def json(d):
    """JSONify something without using the built-in """
    if d == {}:
        #base case
        return '{}'
