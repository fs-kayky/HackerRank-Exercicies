import math
import os
import random
import re
import sys


def timeConversion(s):
    time = s.split(':')
    time[-1],mod = time[-1][:len(time[-1])//2], time[-1][len(time[-1])//2:]

    if(mod == "AM"):
        if(time[0] == "12"):
            return f'00:{time[1]}:{time[2]}'
        else:
            return (f'{time[0]}:{time[1]}:{time[2]}')
    elif(mod == "PM"):
        if(time[0] == "12"):
            return f'{int(time[0])}:{time[1]}:{time[2]}'
        else:
            return f'{int(time[0])+12}:{time[1]}:{time[2]}'
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
