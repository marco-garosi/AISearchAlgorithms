# Artificial Intelligence Search Algorithms
Search Algorithms applied to Artificial Intelligence (agent search) with real-time visualization to better understand how they work and how they reach the goal.

# How to use
Here's the basic steps to get this software running.

## 1
You should install the required packages (see `requirements.txt`). The software was built and tested with Python 3.10.6.

## 2
Run `main.py`.

## How to change tweak parameters
You may change some parameters in the `Problem.py` source file.
You may change the cost-evaluation function `f(n)` to return:
- "standard" f, as described in the simple version of A*: f(n) = g(n) + h(n);
- "weighted" f, as described in the weighted version of A*: f(n) = g(n) + W * h(n) - and you may change the weight W.
You may do this by changing the value returned by `f(node)` (swap commented line).

You may introduce new heuristic functions. As of now, two heuristic functions are defined:
- h1, which computes the so-called Manhattan distance from current state to goal state;
- h2, which computes the so-called Euclidean distance from current state to goal state.
You may do this by changind the value returned by `h(node)` (swap commented line).

# Disclosure
This software is provided as-is, with no warranty or liability. It is intended to be a "proof-of-concept", demonstrating the search algorithms introduced in the "Artificial Intelligence - A Modern Approach" (*AIMA*) book by Stuart Russell and Peter Norvig.