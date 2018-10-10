def reverseItem(item):
    toString = str(item)
    stringLent = len(toString)
    print item
    # import pdb
    # pdb.set_trace()
    newStr = toString[::-1]

    print newStr

    
    if newStr[stringLent-1] == '-':
      strToInt = 0 - int(newStr[0:stringLent-1])

    else:
      strToInt = int(newStr)
    return strToInt

def solution(LD):
    """
    Complete the function such that:

    Given a list of digits LD, reverse all the digits in LD to a new list LR.
    Return the LR and largest element in LR in a tuple such that:

        - [123] -> ([321], 321)
        - [-789, 10] -> ([-987, 1], 1)
        - [11020, 3512] -> ([2011, 2153], 2153)

    Constraints:
    Eliminate leading zeros.
    Note the position of the negative operator after the reversal.

    """
    arr1 = []
    for item in LD:
      arr1.append(reverseItem(item))
    
    print ((arr1, max(arr1)))
    return ((arr1, max(arr1)))

solution([11020, 3512])