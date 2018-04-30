# Implement JSONify without the built-in
# Everything done on the whiteboard
# don't panic :-)
# what's the base case?
# what's the simplist real json with stuff in it
# if the value itself is a larger structure, that determines if we have to keep going
# step by step find if values are #/arrays/dict

# A lot of recursive problems have to do with parsing things
# another exercise, turn json back into a dictionary 


d = {'a' : 1, 'b' : 2}

def json(d):
    """JSONify something without using the built-in """
    s = "{"

    for k in d:

        if d[k] in (int, float, str):
            s += str(k) + ':' + str(d[k]) + ","

        elif type d[k] is dict:
            st = str(k) + ':' + json(d[k])

        elif type (d[k]) is list:
            # what if we encounter a list?
            s += str(k) + ':' + '[' + ','.join[json(item) for item in d([k])] + ']'

    return s
