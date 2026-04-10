'''Summation'''

import json

def summation_one(num):
    '''summtion'''

    total = 0
    for i in range(num + 1):
        total += i
    return total

def summation_two(num):
    '''summation formula'''

    return int(num * (num + 1) / 2)

def is_intersect(one, two, three):
    '''is it intersect?'''
    inter = False
    for i in one:
        for j in two:
            if i == j:
                for k in three:
                    if i == j == k:
                        inter = True
                        return inter
    return inter

def main():
    '''main function'''
    print(is_intersect(json.loads(input()), json.loads(input()), json.loads(input())))

main()