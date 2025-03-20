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

Our programs so far have been pretty linear - going from one instruction to the next, potentially skipping a few when using a conditional, but with a clear start and end nonetheless. However, what if we wanted to do one thing 100 times? 10,000 times? Endlessly, only stopping when a condition is met? Copy-pasting can only get us so far, but there are sleeker ways to achieve the same end goal, and do even more!

## The `for` loop

More often than not, we want to perform a particular action a set number of times, or do something for every element in a list/ string/ tuple/ etc. This is a perfect application of the `for` loop. Let's begin with a simple example: printing all the integers from 1 to 100:

```python
my_numbers = range(1, 101)
for number in my_numbers:
    print(number)
```
🖨️👇
```
1
2
3
[... you know how this goes ...]
98
99
100
```

A lot just happened: we wrote **two** lines of code and got **100** lines of output! This is a testament to how powerful loops are. Let's unpack how they work.

### Syntax

The general form of a `for` loop is as follows:

```python
for <element> in <iterable thing>:
    <do something>
    <do some more stuff>
    <do however much you want>
```

Here we're using `<element>` and `<iterable thing>` as placeholders for actual variables:
- `<iterable thing>` should be a variable storing an iterable type, for instance a sequence: `list`, `range`, `string`, `tuple`
- `<element>` is the name of the variable **created by the `for` loop** to store each value from `<iterable thing>`, one by one:
    - This variable will first be set to the first element, then the second element, the third, and so on, until the end
    - This variable will remain in scope (i.e. still be usable) even after the loop concludes

### How it works

Let's consider another simpler example and look at what happens, step by step:
```python
my_range = range(1, 4)
for i in my_range:
    print(i)
```
🖨️👇
```
1
2
3
```
This code is logically equivalent to the following code fragment, but with no loops:
```python
my_range = range(1, 4)
i = my_range[0]
print(i) # prints 1
i = my_range[1]
print(i) # prints 2
i = my_range[2]
print(i) # prints 3
```
The point to remember is that the variable used in the loop takes every value from the thing we are iterating over, one by one.

Another thing you probably noticed is that this time we used another variable name, `i`. The variable name is nothing special, but a lot of programmers often use single letter variables like `i`, `j`, `k` because of convenience and tradition.

While a name like this is convenient to type, and is also meaningful when the `i` represents an **i**ndex, in another context it might be better to use a different variable name for code readability.

### Using `for` loops with different data types

#### Iterating over strings

#### Iterating over tuples

#### Iterating over lists

### Using `for` loops for different things

#### Doing something `n` times

#### Copying and filtering

#### Aggregating

#### Mapping

## The `while` loop

### Syntax

### How it works

### Using `while` loops

#### Animation with `penndraw`

#### Infinite `while` loops

#### Counting with a `while`

#### Iterating over a sequence with a `while`

## How to choose between `for` and `while`
