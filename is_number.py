# Short routine to determine whether an input string is either a number 
#  or not -- true or false. We use this to eliminate empty or bad data
#  values from the input file.

def is_number (s):
    try:
        float (s)
        return True
    except ValueError:
        return False


