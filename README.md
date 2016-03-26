# N-Queens in Python

## Authors
Todd Wickizer and Joshua Djakaria


## About

This is an implementation and solution of the famous N-Queens probelm in python. The code will solve the n-queens probelm with two algorithms:
 * Min Conflicts
 * Back Tracking

Then It will compare the time required to solve the two algorithms.

## Requirements

Python 2.7.x

## Usage

The code is designed to be ran from the command line in the following way:

`python nqueens.py <n>`

where n is the board size, for example:

`python nqueens.py 8`
will solve a board size of 8 x 8


### Results

Seems like under n=15 backtracking wins. Over 15 min-conflicts dominates.
