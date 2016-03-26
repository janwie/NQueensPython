"""
!!!!REQUIRES PYTHON 2.7.X!!!!
N Queens Backtracking.

Todd Wickizer
Joshua Djakaria
"""

import pprint
import sys
import random
from timeit import default_timer as timer



###############################################################################
#                                                                             #
#                          FUNCTIONS USED BY BACK TRACKING                    #
#                                                                             #
###############################################################################


def print1dArray(arr):
    '''Converts the 1d array into a 2d array so we can print it easy'''
    printable = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        printable[i][result[i]] = 1

    pprint.pprint(printable)


def canPlaceQueenAt(x, y):
    ''' This function returns wether or not a queen can be placed at x,y '''

    for i in range(0, x):
        if (result[i] == y):
            return False
        if (abs(i-x) == abs(result[i]-y)):
            return False

    return True


def placeQueen(row):
    ''' This attempts to place a queen and subsequentially backtracks if it fails '''
    for i in range(0, n):
        if (canPlaceQueenAt(row, i)):
            result[row] = i

            if (row == n-1):
                print1dArray(result)
                end = timer()
                backtracking_time = (end - start)

                print "Time for Min Conflicts: ",
                print conflicts_time 
                print "Time for BackTracking:  ",
                print backtracking_time 
                sys.exit(0)

            placeQueen(row+1)

###################################################################################
#                                                                                 #
#                          FUNCTIONS USED BY MIN CONFLICTS                        #
#                                                                                 #
###################################################################################


def amountOfConflicts(x,y):
    '''This function returns the amount of conflicts at the suggested location'''
    number = 0
    for i in range(n):
        if i == x:
            continue
        if (result[i] == y):
            number += 1
        if (abs(i-x) == abs(result[i]-y)):
            number += 1
    return number

def conflictsPerRow():
    '''Returns an array of the possible conflicts per row '''
    return [amountOfConflicts(x, result[x]) for x in range(n)]

def findMinConflict(iterations=1000):
    '''Uses the min conflict algorithim to solve n queens '''

    for i in range(iterations):

        # First we check if we have solved the problem
        row_conflicts = conflictsPerRow()

        if (sum(row_conflicts)) == 0:
            return result

        # Next we assign a queen to a random column, and place it in a row
        # with the lowest amount of current conflicts
        col = random.choice(list(range(n)))
        # Find Conflicts for that col
        col_conflicts_per_row = [amountOfConflicts(col, row) for row in range(n)]
        # Then attempt to place a queen there
        result[col] = random.choice([i for i in range(n) if col_conflicts_per_row[i] == min(col_conflicts_per_row)])


if len(sys.argv) < 2:
    print "Please Provide the board Length"
    sys.exit(0)

n = int(sys.argv[1])
result = [0]*n

start = timer()
print("Min Conflcit Solution  (if Exists):")
print1dArray(findMinConflict())
end = timer()
conflicts_time = (end - start)

start = timer()
print("Back Tracking Solution (If Exists):")
result = [0]*n
placeQueen(0)
