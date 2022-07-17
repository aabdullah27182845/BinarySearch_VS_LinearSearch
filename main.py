import time
import random


def linearSearch(inputList, targetValue):
    for i in range(len(inputList)):
        if inputList[i] == targetValue:
            return i
    return -1

def binarySearch(inputList, targetValue):
    start = 0
    end = len(inputList) - 1
    mid = (end-start) // 2
    while start <= end:
        if targetValue > inputList[mid]:
            start = mid + 1
            mid = (end-start) // 2 + start
        elif targetValue < inputList[mid]:
            end = mid - 1
            mid = (end-start) // 2 + start
        else:
            return mid
    return -1

def recursiveBinarySearch(inputList, targetValue, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(inputList) - 1

    if high < low:
        return -1
    
    mid = (start + end) // 2

    if inputList[mid] == targetValue:
        return targetValue
    elif inputList[mid] > targetValue:
        return recrusiveBinarySearch(inputList, targetValue, low, midpoint - 1)
    else:
        return recursiveBinarySearch(inputList, targetValue, midpoint + 1, high)

def main():
    length = 10000
    sortedList = set()
    while len(sortedList) < length:
        sortedList.add(random.randint(-3*length, 3*length))
    sortedList = sorted(list(sortedList))

    start = time.time()
    for target in sortedList:
        linearSearch(sortedList, target)
    end = time.time()
    print("Average linear time is", (end-start)/length, "seconds")

    start2 = time.time()
    for target in sortedList:
        binarySearch(sortedList, target)
    end2 = time.time()
    print("Average binary time is", (end2-start2)/length, "seconds")


if __name__ == "__main__":
    main()
