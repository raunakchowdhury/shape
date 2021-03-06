# shape
- Day 1: Implemented Merge, Insertion, and Selection Sorts.
- Day 2: Implemented Python's version of OOP and integrated sorting algorithms from Day 1 to sort a virtual library of books.
- Day 3: Same as day 2, but instead sorted Rational numbers in addition to mathematical functionality. Built a Tree object and implemented post-, in-, and pre-order traversals. Also implemented a rudimentary calculator that interprets a tree of numbers and math operations to print out the value of the tree.
- Day 4: Wrote a Stack object and used it to generate an expression tree (the "calculator" from day 3). Used a Stack to convert from infix to postfix notation.
- Day 5: Simulated the Josephus game with a circular Queue. Used the heapq package to HeapSort.
  - The [Josephus Game](https://en.wikipedia.org/wiki/Josephus_problem):
    - Given N people in a circle, start with one person and count to K.
    - Eliminate the Kth person and repeat with the person after the Kth person.
  - Learned how to delete gravity:
    - ```
      import antigravity
      ```
- Day 6: Wrote [TopologicalSort](https://en.wikipedia.org/wiki/Topological_sorting) for directed acyclic graphs ([DAGs](https://en.wikipedia.org/wiki/Directed_acyclic_graph)). Implemented [Breadth First Search](https://en.wikipedia.org/wiki/Breadth-first_search) using a Queue.
- Day 7: Used an AI to solve the 8-square variant of a [sliding puzzle](https://en.wikipedia.org/wiki/Sliding_puzzle). More specifically, wrote Breadth-First Search and [Depth-First Search](https://en.wikipedia.org/wiki/Depth-first_search). Wrote a second version of Depth-First Search that searches heuristically (eg. consider the states that that have the least number of moves to solve first).
- Day 8: Partially completed [A* search](https://en.wikipedia.org/wiki/A*_search_algorithm).
- Day 9: Rewrote and refactored A* search. A* search now works!
- Day 10: Began implementing the [Minimax algorithm](https://en.wikipedia.org/wiki/Minimax), one technique used in game-playing.
- Day 11: Finished implementing Minimax, completing the first MVP of the AI. Added some heuristics to make the AI more intelligent.
- Day 12 and 13: Finished creating the AI, which can play [Othello](https://en.wikipedia.org/wiki/Computer_Othello) competitively! I have also saved copies of other AIs for black-box testing purposes; my AI is located in rc3246_ai.py.

## Running Othello and the AI
To run Othello from the directory, clone the repo first. From the root of the repo, run the following commands:
```
cd ai-project/othello/
python othello_gui.py rc3246_ai.py
```
The AI will enter as the White player. To pit two AIs against each other, run:
```
cd ai-project/othello/
python othello_gui.py ai_1.py ai_2.py
```
Where  ai_1 is the Black player and ai_2 is the White player.
These are the AIs you can choose from:
- rc3246_ai.py (My AI)
- bcw2122.py
- akm2220_ai.py
- randy_ai.py

### SHAPE '18:
![SHAPE picture](/ai-project/shape2018.jpg)
