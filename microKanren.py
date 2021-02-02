#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""
microKanren language in Python 3.

- See https://codon.com/hello-declarative-world
- Code from https://github.com/jcoglan/kanrens/blob/master/python/main.py
- See https://blog.jcoglan.com/2020/02/07/why-recursion-matters-part-2/
- Original paper is on http://webyrd.net/scheme-2013/papers/HemannMuKanren2013.pdf
- Python 3 version was adapted by Lilian Besson (@Naereen) https://GitHub.com/Naereen
"""

if __name__ == '__main__':
    print(__doc__)

import copy
from collections import OrderedDict


class Variable(object):
    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return self._name


class State(object):
    def __init__(self, values=None):
        self._values = values or OrderedDict()

    def bind(self, name):
        values = copy.copy(self._values)
        var = Variable(name)
        values[var] = None
        return (State(values), var)

    def assign(self, var, value):
        values = copy.copy(self._values)
        values[var] = value
        return State(values)

    def walk(self, key):
        if key in self._values:
            value = self._values[key]
            if value is None:
                return key
            else:
                return self.walk(value)
        elif isinstance(key, tuple):
            return (self.walk(key[0]), self.walk(key[1]))
        else:
            return key

    def unify(self, a, b):
        a = self.walk(a)
        b = self.walk(b)

        if a == b:
            return self
        elif isinstance(a, Variable):
            return self.assign(a, b)
        elif isinstance(b, Variable):
            return self.assign(b, a)
        elif isinstance(a, tuple) and isinstance(b, tuple):
            unify_left = self.unify(a[0], b[0])
            if unify_left:
                unify_right = unify_left.unify(a[1], b[1])
                return unify_right
            else:
                return None
        else:
            return None

    def result(self, index):
        return self.walk(list(self._values.keys())[index])

    def __repr__(self):
        return '[State ' + str(self._values) + ']'


def eq(a, b):
    def pursue(state):
        new_state = state.unify(a, b)
        if new_state:
            return [new_state]
        else:
            return []

    return pursue


def bind(names, func):
    def pursue(state):
        vars = []
        for name in names:
            (state, var) = state.bind(name)
            vars.append(var)
        goal = func(vars)
        return goal(state)

    return pursue


def either(a, b):
    def pursue(state):
        return a(state) + b(state)

    return pursue


def both(a, b):
    def pursue(state):
        states = []
        for a_state in a(state):
            states += b(a_state)
        return states

    return pursue


NULL = object()

def from_list(list):
    if list:
        return (list[0], from_list(list[1:]))
    else:
        return NULL

def to_list(tuple):
    if tuple == NULL:
        return []
    else:
        return [tuple[0]] + to_list(tuple[1])


if __name__ == '__main__':
    world = State()

    def with_vars(vars):
        [x, y] = vars
        return either(eq(x, 5), eq(x, 6))

    goal = bind(['x', 'y'], with_vars)
    print(goal(world))


if __name__ == '__main__':

    def with_vars(vars):
        [x, y] = vars
        return both(eq(x, 'wigwam'), eq(y, 'wotsit'))

    goal = bind(['x', 'y'], with_vars)
    print(goal(world))


if __name__ == '__main__':
    print(from_list([1,2,3,4]))
    print(to_list(from_list([1,2,3,4])))


def append(x, y, z):
    def x_not_null(vars):
        [first, x_rest, z_rest] = vars
        return both(
            both(
                eq(x, (first, x_rest)),
                eq(z, (first, z_rest))
            ),
            append(y, x_rest, z_rest)
        )

    return either(
        both(
            eq(x, NULL),
            eq(y, z)
        ),
        bind(['first', 'x_rest', 'z_rest'], x_not_null)
    )



if __name__ == '__main__':
    def with_vars(vars):
        [x, y, z] = vars
        return append(x, y, from_list([1,2,3,'a','b','c']))

    goal = bind(['x', 'y', 'z'], with_vars)
    states = goal(world)

    for state in states:
        print('')
        print(('x', to_list(state.result(0))))
        print(('y', to_list(state.result(1))))

