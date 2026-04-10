'''Insertion Sort'''

import json

def insertion(arr, last):
    '''Insertion Sort'''

    time = 0
    key = 1
    while key <= last:
        hold = arr[key]
        walker = key - 1
        while True:
            if walker < 0 or (ord(hold[0]) > ord(arr[walker][0])):
                break
            if hold[0] == (arr[walker])[0]:
                if int(hold[1:]) >= int(arr[walker][1:]):
                    break
            arr[walker+1] = arr[walker]
            walker -= 1
            time += 1
        arr[walker+1] = hold
        time += 1
        key += 1
        print(arr)
        if walker < 0:
            time -= 1
    print("Comparison times:", time)

def main():
    '''main'''

    arr = json.loads(input())
    last = int(input())
    insertion(arr, last)

main()