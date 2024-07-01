import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    arr = [int(arr_one) for arr_one in input().strip().split(' ')]
    for i in range(len(arr)):
        print(str(arr[-i-1]), end = " ")