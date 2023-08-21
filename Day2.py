#Given the meal price,tip percent,and tax percent for a meal, find and print the meal's total cost. Round the result to the nearest integer.
CODE:
import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):

    tip =meal_cost * tip_percent/100
    tax =meal_cost * tax_percent/100
    total = meal_cost+tip+tax
    print(round(total))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
