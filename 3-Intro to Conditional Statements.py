#!/bin/python3

import math
import os
import random
import re
import sys

def check_weirdness(N):
    if N % 2 != 0:
        print("Weird")
    else:
        if 2 <= N <= 5:
            print("Not Weird")
        elif 6 <= N <= 20:
            print("Weird")
        else:
            print("Not Weird")

if __name__ == '__main__':
    N = int(input().strip())
    check_weirdness(N)