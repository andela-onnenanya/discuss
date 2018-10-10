def solution(arr):
    """
    Write a function that produces the output, given the input below;
    #inputArr = [1,2,3,4,5,6,7,8]
    #outputArr = [1,5,2,6,3,7,4,8]
    """
    arrLenght = len(arr)
    arr1 = arr[0:int(arrLenght/2)]
    arr2 = arr[int(arrLenght/2):]
    finalArr = []
    for i, item in enumerate(arr1):
      finalArr.append(item)
      finalArr.append(arr2[i])
    print finalArr
    return finalArr

solution([1,2,3,4,5,6,7,8])