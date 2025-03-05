# Loops and Comprehensions

## Learning Objectives

- Learn how to repeat some action for each element of a sequence using a `for` loop
- Become familiar with certain patterns of processing sequences:
    - aggregating,
    - mapping,
    - & filtering
- Learn how to repeat some action while a condition holds using a `while` loop
- Identify cases when a `for` loop is more appropriate than a `while` loop and vice versa

## Overview

[comment]: <> (TODO: Harry please approve of this or change it, I felt like it's also an interesting pun since if you don't remember to advance in your iteration, you can end up in an infinite loop)
> *Those who do not remember the past are condemned to repeat it*
> -- George Santayana, *The Life of Reason*

Our programs so far have been pretty linear - going from one instruction to the next, potentially skipping a few when using a conditional, but with a clear start and end nonetheless. However, what if we wanted to do one thing 100 times? 10,000 times? Endlessly, only stopping when a condition is met? Copy-pasting can only get us so far
