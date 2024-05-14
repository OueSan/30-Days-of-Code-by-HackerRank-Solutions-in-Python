#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Calculate tip
    tip = meal_cost * tip_percent / 100
    # Calculate tax
    tax = meal_cost * tax_percent / 100
    # Calculate total cost
    total_cost = meal_cost + tip + tax
    # Round the total cost to the nearest integer and print it
    print(round(total_cost))

if __name__ == '__main__':
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    
    solve(meal_cost, tip_percent, tax_percent)