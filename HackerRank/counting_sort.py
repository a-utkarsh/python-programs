import math
import os
import random
import re
import sys

def countingSort(arr):
    return arr.sort()
if __name__ == '__main__':


    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)
    print(result)


