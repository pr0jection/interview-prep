"""
Backtracking is a class of algorithms for constraint satisfaction problems that
incrementally builds a candidates to the solutions, and abandons a candidate
(backtracks) as soon as it determines the candidate cannot possibly work.

It is applicable primarily when (1) there are partial candidate solutions and
(2) there is a quick test of whether a partial candidate can possibly be completed.

For instance, in the 8 queens puzzle:
    - root() returns the empty chess board
    - reject() returns true if any queens are attacking one another
    - accept() returns true if there are 8 queens on the board
    - first() places a queen in an empty spot
    - next() places a queen in the next empty spot
"""

from typing import Optional

class SearchSpace:
    ...


class Candidate:
    ...


def root(p: SearchSpace) -> Candidate:
    """ Return the candidate at the root of the search tree. """
    ...


def reject(p: SearchSpace, c: Candidate) -> bool:
    """ Return true if it is certain that the candidate is not worth completing. """
    ...


def accept(p: SearchSpace, c: Candidate) -> bool:
    """ Return true if the candidate is a complete and valid solution. """
    ...


def first(p: SearchSpace, c: Candidate) -> Optional[Candidate]:
    """ Return the first extension of a candidate. """
    ...


def next(p: SearchSpace, s: Candidate) -> Optional[Candidate]:
    """ Return the next extension of a candidate after `s`. """
    ...


def output(p: SearchSpace, c: Candidate) -> None:
    """ Use the solution as appropriate. """
    ...


def backtrack(p: SearchSpace, c: Candidate) -> None:
    if reject(p, c):
        return

    if accept(p, c):
        # don't assume that a solution is the leaf of a search tree
        # i.e. continue searching
        output(p, c)

    s = first(P, c)
    while s:
        backtrack(p, s)
        s = next(p, s)


p = SearchSpace()
backtrack(p, root(p))
