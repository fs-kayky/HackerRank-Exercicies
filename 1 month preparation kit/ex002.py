import math
import os
import random
import re
import sys


def miniMaxSum(arr):    
    arr.sort()
    sumMax = 0
    sumMin = 0

    for i in range(len(arr)-1):
        sumMax = arr[i] + sumMax

    arr.sort(reverse=True)

    for i in range(len(arr)-1):
        sumMin = arr[i] + sumMin

    print(sumMax, sumMin,)

    
    ...    # Write your code here


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
