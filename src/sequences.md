# Sequences

## Learning Objectives

- Identify and use different kinds of basic sequences: strings, ranges, lists and tuples
- Understand the limitations and restrictions of each type of sequence
- Understand the difference between mutable and immutable sequences
- Use an index to access a value in a sequence
- Use slicing to obtain a subsequence

## Overview

> *There is at times a magic in identity of position.*
> -- E.M. Forster, *A Room with a View*

> *She knew all the indices to the idle lonely.*
> -- Joan Didion, *Play It as It Lays*


Our data types so far have been quite lonely: a single number as an `int` or a `float`, or a single truth value as a `bool`. We can build interactive programs with just a few numbers to describe a square, but we find ourselves in a position where we have to declare a new variable for each individual value that we want to store and manipulate. In this section, we'll learn about new **sequence** data types that serve as containers for multiple pieces of information. Our introduction to sequences will come with a closer look at a familiar data type: `str`.


## Strings as Sequences of Characters

### Strings are Sequences

As we learned before, the `str` data type is how we represent text in Python. We can create a string by writing out a literal as a bunch of characters placed between a pair of the quotation marks of your choice:

```python
vocabulary_word = "vermiculate"
```

A string is defined not just by the characters it contains, but by the order in which those characters are stored. The words *relatives* and *versatile* are anagrams of each other—they contain the same characters—but they are not the same words and they are not the same strings!

```python
a = "relatives"
b = "versatile"
print(a == b)   # prints False!
```

In Python, a **sequence** is a kind of data type that is capable of storing several pieces of information in a specific order. We see that a `str` value fits this description: it is capable of storing arbitrarily many characters and it does so in a specific order. We are limited to storing just one *kind* of data in a string (characters), and we'll see that this is actually restrictive compared to other sequence types in Python.

Since strings know the order of the characters that make them up, we can actually access individual characters one at a time using *indexing*. 

### Strings are Indexable Sequences
A sequence is **indexable** in the sense that we can refer to its first value, its second value, and so on, all the way up to its final value. In Python, the indices that we use start at `0` (not `1`), meaning that when we diagram the index of each character in a string, it looks like this:

```
"indexing"
 01234567
```

Notice that *indexing* is a word with eight letters (that is, `len("indexing") == 8` is `True`) and since we start counting at `0`, the index of the last character is `7`. That difference between the length of a string and the index of its last element is present in strings of different lengths:

```
"short"     # 5 characters long
 01234      # biggest index: 4

"lengthy"   # 7 characters long
 0123456    # biggest index: 6
```

In general, for a string and for all sequences, the index of the `n`th element is `n - 1`. The first element lives at index `0`, the fourth element lives at index `3`, the 653rd element lives at index `652`, and the last element in a string of `n` characters lives at index `n - 1`.

Now that we've belabored the point 1000 times (of which the final time would be found at index `999`...), we can confidently move on to the **indexing operator** in Python. For a sequence `s` of any type, you can access the element at position `i` inside of that sequence by writing `s[i]`. 


For example, in `"Travis Q. McGaha"`, the `Q` is the eighth letter and so it lives at index `7`. Therefore, to pull that character out of the larger string, we can do the following.

```python
full_name = "Travis Q. McGaha"
middle_initial = full_name[7]

print(middle_initial)           # prints 'Q'
```

It's worth noting that the type of `middle_initial` in this case is still `str`—individual characters in Python still count as strings themselves. In any case, we could expand the example to get Travis' first and last initials too:

```python
full_name = "Travis Q. McGaha"
middle_initial = full_name[7]   # Q
first_initial = full_name[0]    # T
last_initial = full_name[10]    # M
```

The indices that are valid for a sequence of length `n` always range from `0` to `n - 1`. An empty sequence, like the empty string `""`, is one that has a length of `0` and therefore has no valid indices to speak of.

If you try to access an index that is not valid (because it is too big), you will crash your program with an `IndexError`:

```python-repl
>>> "HSS"[100]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

An interesting feature is that python also allows for **negative** indexes: `my_seq[-1]` would be the last character of the sequence `my_seq`. For a sequence of length `n`, the allowable negative indices range from `-1` to `-n`:

```python-repl
>>> "miso"[-1]
'o'
>>> "miso"[-2]
's'
>>> "miso"[-3]
'i'
>>> "miso"[-4]
'm'
```

However, an index that is 'too negative' will still result in an `IndexError`:

```python-repl
>>> "miso"[-100]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

### Strings are Concatenatable Sequences

Since each initial is just a `str`, we can concatenate them all together using the `+` operator. This is actually another common feature of Python sequences: two sequences of the same type can usually be concatenated together. (There are some exceptions.)

```python
full_name = "Travis Q. McGaha"
middle_initial = full_name[7]   # Q
first_initial = full_name[0]    # T
last_initial = full_name[10]    # M

full_initials = first_initial + middle_initial + last_initial
print(full_initials)            # prints "TQM"
```


### Strings are Sliceable Sequences

Now that we are more comfortable with sequences and their indices, we can interrogate a claim recently made to me by a bumper sticker on a passing car: that there is no *earth* without *art*. I absolutely agree with the implied argument that there's not much point in being here on this planet without being able to express ourselves creatively. But perhaps there's something more literal here to investigate:

```
"earth"
 12345
```

If we look at the indices of the characters in the string `"earth"`, we can see that the bumper sticker was also correct in a *sequency sense*: characters `2` through `4` of `"earth"` do literally spell out `"art"`. Pulling one sequence out of another is something that we'll often want to do in our programs—not just when we have a pun that we want to belabor—and Python has a syntax for doing it. In the context of strings, if we want to obtain a **subsequence** of a string `s` including all characters starting at index `i` and stopping *before* index `j`, then we can do that by writing `s[i:j]`. For instance:

```python
print("earth"[1:4])     # prints "art" 🖌️
print("earth"[0:3])     # you also can't have "earth"
                        # without "ear" 👂
```

Notice that in each case we are *excluding* the character at the end position. `"earth[1:4]"` gives `"art"`, which is the subsequence consisting of characters at positions `1`, `2`, and `3` only. This takes some getting used to. 

A positive feature of including the starting index but excluding the latter is that you can pretty easily calculate how many characters you're getting: `s[i:j]` will always have a length of `i - j` characters.

Another implication of this design choice means that if you want to get a subsequence containing all characters including the last one, the stopping index is one larger than the highest index of any element actually present in the sequence:

```python
title = "crossroads"
# all three examples below give exactly the same value
roads_one = title[5:10]
roads_two = title[5:len(title)]
roads_three = title[5:]

print(roads_one)                                # prints "roads"
print(roads_one == roads_two == roads_three)    # prints True
```

This last version—`title[5:]`—is a useful syntactical shorthand for getting all characters in `title` starting at position `5` and going all the way to the end of the string. In fact, we can do something similar for shorthand when taking all characters up until a certain position:

```python
title = "crossroads"
# both examples below give exactly the same value
cross_one = title[0:5]
cross_two = title[:5]

print(cross_one)                 # prints "cross"
print(cross_one == cross_two)    # prints True
```

It's also possible to take non-contiguous slices—slices that skip over a fixed number of elements between selections from the larger sequence. Thus, the full slicing syntax emerges:

> If you want every `k`th element of a string `s` starting at index `i` and ending at index `j`, you can write:

```python
s[i:j:k]
```

Broadly, the "formula" is `[start:stop:step]`. Let's take a look at an example. If we want to obtain just `"BC"` as a slice, we can write the following expression:

```python-repl
>>> interwoven_alphabet = "AaBbCc"
>>> interwoven_alphabet[2:5:2]
'BC'
```

How do we get `"BC"`? Writing down the indices of the string helps to illuminate:

```
AaBbCc
012345
```

We start taking characters at position `2` based on the `start`. That's `"B"`. Then, we take a step of `2` over to position `4`. That's `"C"`. We take one more step of size `2` over to position `6`—but `6` is greater than `5`, which is our stopping position. We take `"B"` and `"C"` and nothing else, making our slice.

Take another example:

```python-repl
>>> interwoven_alphabet[0:6:3]
'Ab'
```

We'll start at position `0`, taking `"A"`. We'll take a step of `3` over to position `3` and take `"b"`. We'll take another step of `3` over to position `6`, which is our stopping index. We're done, and `"Ab"` is the output slice.

We can extend this even further with *negative* step sizes: it gets a bit tricky, but it can be useful. In these cases, we'll actually have `start` values that are greater than our `stop` values; this works since we'll be stepping backwards from `start` to `stop`:

```python-repl
>>> "devolve"[4:0:-1]
'love'
```

We start at position `4`, which is `"l"`. We take a step of `-1` to position `3`, which is `"o"`. Another step of `-1` to position `2`, which is `"v"`. Stepping by `-1` to position `1` gives us `e`, and then we take one more step of `-1` over to position `0`, which is our `stop` position. We're done, and `"love"` is the result. Awww 💖.

Taking slices in reverse is a little tricky to get the hang of. For example, there's a big difference between `"devolve"[3:0:-1]` and `"devolve"[3::-1]`—try it out! This is mostly a niche application anyway, but it's worth bringing up for an idiom that comes in handy from time to time. A slice of `[::-1]` is shorthand for reversing a sequence.

```python-repl
>>> "evol"[::-1]
'love'
>>> "pots"[::-1]
'stop'
```

### Membership in Strings

Strings support the use of the `in` keyword to ask if one string is a subsequence of another string. In particular, we know that we can find `"art" in "earth"`—that expression evaluates to `True`—but `"at" in "earth"` is `False`. For two strings `s` and `t`, `s in t` is `True` when you can find `s` as an uninterrupted sequence of characters in `t`. Some corollary properties:
1. if `len(s) > len(t)`, then `s in t` is always `False`
2. `s in s` is always `True`
3. `"" in t` is also always `True`

### Immutability and Strings

While we can index, slice, concatenate and do many other operations with strings, we cannot actually modify them. In technical terms, the `str` datatype is said to be immutable.

*But wait, I can set my variable to `"abcd"`, then modify it to `"AB"` and it works! Isn't that changing the string?*

No, it actually is not! Consider the following code samples:

**Valid code**
```python-repl
>>> my_var = "abcd"
>>> print(my_var)
abcd
>>> my_var = "New string"
>>> print(my_var)
New string
```

**Invalid code**
```python-repl
>>> my_var = "abcd"
>>> print(my_var)
abcd
>>> my_var[0] = "d"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

The difference is very subtle, but crucial for understanding immutability:
- In the first sample, we are **replacing** the string stored in `my_var` (namely `"abcd"`) with **another string** (namely `"New string"`). We are modifying `my_var`, and Python is happy.
- In the second sample, we are trying to modify **the actual string** stored in `my_var` by trying to change its first character, and Python throws an error.

Expressed in another way, we are allowed to **reassign** variables that store strings. But we cannot modify the contents (i.e. characters) of the stings themselves!

From this, you can understand that all of the operations we do on strings don't modify the string, but actually give you a new, possibly different string:

```python-repl
>>> string_one = "abcd"
>>> print(string_one)
abcd
>>> string_two = string_one[1:2]
>>> print(string_one)
abcd
>>> print(string_two)
b
```

Strings are not the only immutable data type - ranges and tuples are also part of this club, as you will see below.

### Taking Inventory

A string's identity is based on the characters it contains and the order in which those characters belong. The ordering of the characters allows us to count them, starting from `0`, using **indices.** We can use **indexing** to query a string for a character stored at a particular position. We can extend indexing to **slicing** by defining a range of indices that we want to pull characters from. And we can check for **membership** inside of strings using the `in` keyword, deciding whether one string is present inside of another. Each of these properties of a string is held in common with the other sequences we'll introduce next.


## Ranges

If `str` is the immutable datatype for sequences of characters, then we can think of the `range` as the corresponding immutable type used for sequences of *numbers.* A **range** is an ordered sequence of numbers defined by a start point, stop point, and step size. Whereas a string can feature characters in any order, ranges are more narrowly constrained. They are defined by a `start`, `stop`, and `step` parameter. (Sound familiar?)

### Creating Ranges

#### `range(n)`
The simplest ranges can be created by omitting both the `start` and `step`, which will default to `0` and `1`, respectively. Writing `range(10)` gives us a sequence of all `int` values from `0` up until `9`. `range(100)` is a bit bigger, containing all numbers from `0` up until `99`. A smaller range might be `range(3)`, containing just `0`, `1`, and `2`. In each case, when creating a range from `0` to some stop value of `n`, the resulting range is a sequence of `n` different numbers in ascending order. 

#### Stopping & Stepping

Like slices, ranges can be customized more fully using the `start` and `step`. Also like with slices, we can provide a negative `step` size to count down from our `start` to our `stop`.

| Contents              | Expression         |
| --------------------- | ------------------ |
| 0, 1, 2, 3, 4         | `range(5)`         |
| 1, 2, 3, 4, 5         | `range(1, 6)`      |
| 1, 3, 5               | `range(1, 6, 2)`   |
| 0, 10, 20, 30, 40, 50 | `range(0, 51, 10)` |
| *empty!*              | `range(6, 0)`      |
| 6, 5, 4, 3, 2, 1      | `range(6, 0, -1)`  |

The procedure for determining the contents of a range from its `start/stop/step` is the same as before: our first number will be `start`, and we'll `step` by a fixed amount until we cross over to the other side of `stop`. 

Have a hard time remembering your times tables? You can list all multiples of a number in a certain range using the `step` parameter. `range(0, 100, 9)` gives all multiples of `9` between `0` and `99`, whereas `range(0, 100, 13)` does the same for multiples of `13`.

## Lists

While ranges are very useful for iteration (see the chapter on loops), they are not great for storing data. What if you wanted to remember all the PennIDs in CIS 1100? Or the tasks you have to complete tomorrow? Or the first 5000 prime numbers?

Lists are the answer! Simply put, a list is a mutable, ordered collection of things. You can add things to it, you can remove things from it, you know if an element comes before or after another, and the elements inside a list don't even have to have the same data type.🤯

### Creating a list

The simplest of lists is the empty list, denoted as a pair of square brackets `[]` with nothing in between. If we want a list that contains the number 1, we would define it as `[1]`. If we want a list that contains multiple elements, we separate them by commas: `[1, "Harry", 50]`.

```python-repl
>>> empty_list = []
>>> print(empty_list)
[]
>>> one_elem = [1]
>>> print(one_elem)
[1]
>>> multiple_elems = [1, "Harry", 50]
>>> print(multiple_elems)
[1, 'Harry', 50]
```

### Working with a list
#### Basic sequence operations
Lists support most of the operations that strings support. Consider the list `my_list = ["a", "b", 23, 55, 70]` for the following examples:
- Getting the length: `len(my_list) # evaluates to 5`
- Getting the i-th element: `my_list[2] # evaluates to 23`
- Slicing: `my_list[1:3] # evaluates to ['b', 23]`
- Concatenation: `my_list + [22, "a"] # evaluates to ['a', 'b, 23, 55, 70, 22, 'a']`
- Membership: `23 in my_list # evaluates to True`

> *Note: When using a string, we were able to check both if a character is in a string (`"c" in "chocolate"`) and if a sequence of characters is in a string (`"la" in "chocolate"`). However, since lists can store any type, including **other lists**, the expression `[23, 55] in my_list` will not check if the elements 22 and 55 are in `my_list`, but rather if the **list** `[23, 55]` is an element in `my_list`.*

Since lists are mutable, i.e. we can modify them, they also support some extra operations, which are detailed below.

#### List specific operations

The first way to modify a list is to add an element to it. This can be done either by **appending** it to the end of the list, or **inserting** it at a particular index:

```python-repl
>>> lst = []
>>> lst.append(13) # add the element 13 to the end
>>> print(lst)
[13]
>>> lst.append("string") # add the element "string" to the end
>>> print(lst)
[13, 'string']
>>> lst.append([1, 2]) # add the element [1, 2] to the end
>>> print(lst)
[13, 'string', [1, 2]]
>>> lst.append(7) # add the element 7 to the end
>>> print(lst)
[13, 'string', [1, 2], 7]
>>> print(len(lst))
4
>>> lst.insert(2, 66) # insert the element 66 at index 2
>>> print(lst)
[13, 'string', 66, [1, 2], 7]
```

The second list-specific operation is changing an element at a particular index:

```python-repl
>>> lst = ['a', 'b', 'c', 'd', 'e']
>>> print(lst)
['a', 'b', 'c', 'd', 'e']
>>> lst[2] = 50 # change the element at index 2 to the value 50
>>> print(lst)
['a', 'b', 50, 'd', 'e']
```

The third thing we are allowed to do with a list is to **extend** it by appending to it all the elements from another list:

```python-repl
>>> print(lst)
['a', 'b', 50, 'd', 'e']
>>> lst.extend([20, 21])
>>> print(lst)
['a', 'b', 50, 'd', 'e', 20, 21]
```

We are also allowed to remove elements from a list in a few different ways:
- `lst.remove(x)` removes the first occurrence of `x` from `lst`. Will cause an error if `x` is not in `lst`

  ```python-repl
  >>> print(lst)
  ['a', 'b', 50, 'd', 'e', 20, 21]
  >>> lst.remove(50)
  >>> print(lst)
  ['a', 'b', 'd', 'e', 20, 21]
  >>> lst.remove(50)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  ValueError: list.remove(x): x not in list
  ```
- `lst.pop(i)` removes and returns the element at position `i`. If no index is specified, it will default to removing and returning the last element

  ```python-repl
  >>> lst = ["a", "b", "c"]
  >>> removed_item = lst.pop(1)
  >>> print(lst)
  ['a', 'c']
  >>> print(removed_item)
  b
  >>> removed_item = lst.pop()
  >>> print(lst)
  ['a']
  >>> print(removed_item)
  c
  ```
- `lst.clear()` removes all elements from the list

  ```python-repl
  >>> lst = ["h", "a", "p", "p", 1]
  >>> lst.clear() # lst is now an empty list
  >>> print(lst)
  []
  ```

### Recap

Lists are one of the most versatile data types in Python, as they can be used to represent many real-world concepts, are mutable, can store any data type within them, and are easy to work with. However, more specialized data types are still worth knowing and understanding, as they solve particular problems much better compared to lists. 

## Tuples

[comment]: <> (TODO: actually do it)

## Summary table

[comment]: <> (TODO: insert the table from the video slides / the rec slides)