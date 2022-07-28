import sys
import numpy as np
import matplotlib.pyplot as plt


def average(list):
    return sum(list)/len(list)


def forwardCompare():
        # large g
    lExp = [0 for i in range(50)]
    sExp = [0 for i in range(50)]
# format
# 0 #Maze file: #.txt
#1 #A* executions: #
#2 #Expanded Cells: #
#3 #Path length: #
#4 #
#5 #
# 6 #Maze file: #.txt
#7 #A* executions: #
#8 #Expanded Cells: #
#9 #Path length: #
#
#

# each maze uses 6 lines
# mazeno stored on lines# mod 6 == 0
# expanded cells #lines with line# mod 6 == 2
#

    f = open('largeG_report.txt', 'r')
    lines = f.readlines()
    n = len(lines)
    print(n)
    i = 0
    while i < n:
        print(i)
        print('index:', int(lines[i][11:13])-50, 'value:', lines[i+2][16:])
        lExp[int(lines[i][11:13]) - 50] = int(lines[i+2][16:])
        i += 6

    print('large G')
    print(lExp)

    f = open('smallG_report.txt', 'r')
    lines = f.readlines()
    n = len(lines)
# print(n)
    i = 0
    while i < n:
        # print(i)
        # print('index:', int(lines[i][11:13])-50, 'value:', lines[i+2][16:])
        sExp[int(lines[i][11:13]) - 50] = int(lines[i+2][16:])
        i += 6

    print('\n\n\n small G')
    print(sExp)
    # put into graph
    print('average small g expansions', str(average(sExp)))
    print('average large g expansions', str(average(lExp)))

    plt.plot(sExp, label='small g avg = {}'.format(str(average(sExp))))
    plt.plot(lExp, label='large g avg = {}'.format(str(average(lExp))))
    plt.title('Small vs Large g')
    plt.ylabel('Number of cells expanded')
    plt.xlabel('Maze number')
    plt.legend()
    plt.show()


def forwardAdaptCompare():
    lExp = [0 for i in range(50)]
    aExp = [0 for i in range(50)]
# format
# 0 #Maze file: #.txt
#1 #A* executions: #
#2 #Expanded Cells: #
#3 #Path length: #
#4 #
#5 #
# 6 #Maze file: #.txt
#7 #A* executions: #
#8 #Expanded Cells: #
#9 #Path length: #
#
#
# each maze uses 6 lines
# mazeno stored on lines# mod 6 == 0
# expanded cells #lines with line# mod 6 == 2
#

    f = open('largeG_report.txt', 'r')
    lines = f.readlines()
    n = len(lines)
    i = 0
    while i < n:
        # print(i)
        # print('index:', int(lines[i][11:13])-50, 'value:', lines[i+2][16:])
        lExp[int(lines[i][11:13]) - 50] = int(lines[i+2][16:])
        i += 6

    print('large G')
    print(lExp)

    f = open('adaptive_report.txt', 'r')
    lines = f.readlines()
    n = len(lines)
# print(n)
    i = 0
    while i < n:
        # print(i)
        # print('index:', int(lines[i][11:13])-50, 'value:', lines[i+2][16:])
        aExp[int(lines[i][11:13]) - 50] = int(lines[i+2][16:])
        i += 6

    print('adaptive')
    print(aExp)
    # put into graph
    print('average adaptive expansions', str(average(aExp)))
    print('average large g expansions', str(average(lExp)))

    plt.plot(aExp, label='adaptive avg = {}'.format(str(average(aExp))))
    plt.plot(lExp, label='large g avg = {}'.format(str(average(lExp))))
    plt.title('Adaptive vs Forward A*')
    plt.ylabel('Number of cells expanded')
    plt.xlabel('Maze number')
    plt.legend()
    plt.show()


def bfCompare():
    lExp = [0 for i in range(50)]
    bExp = [0 for i in range(50)]

    f = open('largeG_report.txt', 'r')
    lines = f.readlines()
    n = len(lines)
    i = 0
    while i < n:
        # print(i)
        # print('index:', int(lines[i][11:13])-50, 'value:', lines[i+2][16:])
        lExp[int(lines[i][11:13]) - 50] = int(lines[i+2][16:])
        i += 6

    print('large G')
    print(lExp)

    # change file name to backwards_report.txt
    f = open('backwards_report.txt', 'r')
    lines = f.readlines()
    n = len(lines)
# print(n)
    i = 0
    while i < n:
        # print(i)
        # print('index:', int(lines[i][11:13])-50, 'value:', lines[i+2][16:])
        bExp[int(lines[i][11:13]) - 50] = int(lines[i+2][16:])
        i += 6

    print('backwards')
    print(bExp)
    # put into graph
    print('average backwards expansions', str(average(bExp)))
    print('average large g expansions', str(average(lExp)))

    plt.plot(bExp, label='backwards avg = {}'.format(str(average(bExp))))
    plt.plot(lExp, label='large g avg = {}'.format(str(average(lExp))))
    plt.title('Backwards A* vs Forward A*')
    plt.ylabel('Number of cells expanded')
    plt.xlabel('Maze number')
    plt.legend()
    plt.show()


# read all graph stats that apply
# plot comparisons between
if __name__ == "__main__":
    # forwardCompare()
    # forwardAdaptCompare()
    bfCompare()
