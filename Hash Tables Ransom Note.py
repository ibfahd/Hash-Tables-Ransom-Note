#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    res = True
    for n in note:
        if n in magazine:
            cnn = note.count(n)
            cnm = magazine.count(n)
            res = res and (cnn <= cnm)
        else:
            res = False
    if res:
        print("Yes")
    else:
        print("No")
        
if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    checkMagazine(magazine, note)
