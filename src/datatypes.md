# Data Types

## Learning Objectives
- To be able to define data types
- To be able to write expressions using simple data types 



## Overview
Computers are devices that store, retrieve, and manipulate data at extreme speeds. This simple definition really undersells the excitement of computing, of course: computers bring us interactive entertainment, they enable massive increases in human productivity, and they run the complex algorithms that form the backbone of many systems that govern our lives. They can be fun, useful, and sometimes unaccountably powerful. But, nevertheless: a computer's job is to push data around really fast. 

In order for us to write computer programs, then, we need a way of understanding and organizing the data that a computer is supposed to be working with. Data types allow us to do this.

---

## Data

**Data** are pieces of information. We use data to model entities & solve problems. All data in Python have a **data type**. Data types define the set of possible values a piece of data can have and the possible **operators** that can be used to manipulate values from that set of possible values in order to produce other new values as outputs. 

You might be familiar with the word "operation" from grade-school mathematics, as in "order of operations" when figuring out how to evaluate an expression like `3 + 4 - (3 * 7)`. In that case, the operations were addition, subtraction, and multiplication, denoted by the `+`, `-`, and `*` operators respectively. An **operator** is the name that we give to the symbol that denotes the operation. In programming, operators work in a very similar way.

We'll encounter a huge variety of data types in Python, but we'll start by talking about a few simple ones to start: the `int`, `float`, `bool`, `str`, and `None`. These types are useful for representing numbers, text, and program logic. 

<div class="warning">
The following sections introduce many new operators and several examples are included. If you're curious about how a particular operator works in a case that's not listed, you are strongly urged to try it out for yourself using print statements.
</div>

### Numeric Types

`int` is a data type that represents *whole integer numeric values*. These values can be positive, negative, or zero, but they must not have any fractional (decimal) parts. In Python, `3`, `1`, `0`, `-10`, `-1033` are all examples of `int` values. 

#### Values
It would be very limiting to only have access to integer numbers, and so there is the `float` data type in Python that can represent numbers that also contain a fractional (decimal) part. In Python, `3.0`, `1.4`, `0.0`, `-10.10`, `-1033.33333` are all examples of `float` values. The type is called `float` because it's short for "floating point number", which is the official name for the way that Python represents numbers with fractional parts inside of your computer's memory.

For the most part, `int` and `float` values can be used interchangeably in Python. Sometimes it's useful for a program to expect an `int` specifically rather than a `float`; for example, we might write a program that allows a user to choose a numbered item from an entree list on a menu. In that case, it would make sense to expect that the user's answer should be an `int` ("I'll have the number 3, please!") instead of a `float` ("Could I please have the number 3.7623, extra spicy?").

#### Arithmetic Operators
Recall that data types are not just defined by the kinds of information they can represent—they also describe the kinds of operators that we can use on the data that belongs to the type. For numeric types like `int` and `float`, the important operators are all mathematical. Take a look at the table below to see four commonly used operators (`+`, `-`, `*`, `/`) on the `int` data type. Most of them will be familiar to you already!

| Operator | Operation      | Example with `int` values | Output Value | Output Type |
| -------- | -------------- | ------------------------- | ------------ | ----------- |
| `+ `     | Addition       | `3 + 5`                   | `8`          | `int`       |
| `-`      | Subtraction    | `4 – 6`                   | `-2`         | `int`       |
| `*`      | Multiplication | `2 * 3`                   | `6`          | `int`       |
| `/`      | Division       | `3 / 2`                   | `1.5`        | `float`     |

Each of the four common arithmetic operators in Python follow the rules of basic arithmetic. These four operators are all examples of *binary infix operators*, meaning that they are placed between two values that they are operating on. These values on the left and the right of the operator are called **operands**. 

One detail to note in the table above is that while addition, subtraction, and multiplication of two `int` values will always yield an `int` as a result, the division of two `int` values doesn't produce another `int` value. Instead, the value that is produced belongs to the `float` data type. This reveals an important point: *the output type of an operation will not always match the types of its inputs.*

Fortunately, this is a pretty minor detail. The same four operators can be used on values of the `float` data type—again behaving in predictable ways—and in fact the operations can be performed on `int` and `float` values mixed together. 

| Operator | Operation      | Example with `int` and `float` values | Output Value | Output Type |
| -------- | -------------- | ------------------------------------- | ------------ | ----------- |
| `+ `     | Addition       | `3.1 + 5`                             | `8.1`        | `float`     |
| `-`      | Subtraction    | `4.0 – 0.86`                          | `3.14`       | `float`     |
| `*`      | Multiplication | `-2.0 * 3`                            | `-6.0`       | `float`     |
| `/`      | Division       | `3.0 / 2.0`                           | `1.5`        | `float`     |

Note that when either the left or right operand (or both) are `float` values, then the output type is always `float`.

#### Modulo & Integer Division

There are two additional operators for numeric types that are slightly more complicated than the common arithmetic ones. These are the `%` ("**modulo**" or "mod") operator and the `//` ("integer division") operator. Both of these are again defined for `int` and `float`, but we'll generally stick to using them with `int` values. 

The integer division operation allows us to divide two `int` values and get an `int` as a result. The way that you can think about how this works is that we do regular division arithmetic, and then **truncate** the result by removing the fractional part (the part after the decimal). Whereas `3 / 2` (regular division) is `1.5`, `3 // 2` (integer division) is `1`. Generally speaking, if we write `a // b`, then we're calculating the number of times that `b` "goes into" `a`. Check out some of the examples in the table below.

| Example Expression | Example Result |
| ------------------ | -------------- |
| `16 // 5`          | `3`            |
| `15 // 5`          | `3`            |
| `14 // 5`          | `2`            |
| `3 // 7`           | `0`            |
| `-11 // 2`         | `-5`           |

Modulo (or "mod", for short) is an operation that complements integer division. When we write the expression `a % b` (read aloud like "`a` mod `b`"), we are calculating the remainder left after dividing `a` by `b`. For example, we might write `16 % 5` in order to evaluate the remainder after using integer division to divide `16` by `5`. We find that `5` "goes into" `16` `3` times, making `15`. Thus, the remainder after dividing `16` by `5` is equivalent to `16 - 15`, or `1`. Sometimes this is easier to learn by example, so here are a couple of tables with plenty of examples. In the first, we see what happens as we change the number on the lefthand side.

| Example Expression | Example Result |
| ------------------ | -------------- |
| `0 % 3`            | `0`            |
| `1 % 3`            | `1`            |
| `2 % 3`            | `2`            |
| `3 % 3`            | `0`            |
| `4 % 3`            | `1`            |
| `5 % 3`            | `2`            |
| `6 % 3`            | `0`            |

The output of `a % b` is always a number between `0` and `b - 1`. Moreover, as we increment `a` one by one, we see that the output increases by one each time until it wraps back around to `0` and starts the pattern again.

Now, let's look at what happens when we fix the lefthand value and "mod it" by a bunch of other different numbers:

| Example Expression | Example Result |
| ------------------ | -------------- |
| `12 % 1`           | `0`            |
| `12 % 2`           | `0`            |
| `12 % 3`           | `0`            |
| `12 % 4`           | `0`            |
| `12 % 5`           | `2`            |
| `12 % 6`           | `0`            |
| `12 % 7`           | `5`            |
| `12 % 13`          | `12`           |

If `a` is evenly divisible by `b`, then `a % b` will always output `0`. If `a` is less than `b`, `a % b` will always output `a`. Can you think about why this two facts are true?

##### Example: Pizza Party

Suppose I'm having a pizza dinner with my friends. If I have thirteen pizzas with eight slices and there are fifteen of us, what is the minimum number of full slices we can all expect to eat if we share evenly? To calculate the result, we can first think about how to write the expression that calculates how many slices of pizza we have in total. 

```python
13 * 8 # eight slices per pizza, thirteen pizzas
```

Next, we want to figure out how many full slices per person we'll have if we share evenly. We could try to calculate this with regular division to determine the result. The expression that does this is `(13 * 8) / 15`. (Technically the parentheses are optional, but I recommend using them liberally throughout your programs to make sure that your order of operations is always what you're expecting.)

```python
print("Calculating number of slices per person...")
print((13 * 8) / 15)
```

If we run this program, the output is `6.933333333333334`. This answer is mathematically accurate, but it doesn't answer the question as asked. We want to know the number of **full** slices per person—I don't know about you, but I don't know how to cut a pizza slice into `.933333333333334`ths.

Switching the expression to use integer division (`//`) should solve the problem:
```python
print("Calculating number of full slices per person...")
print((13 * 8) // 15)
```

Looks like each person will get `6` slices of pizza. But we know from our first attempt that every person could actually have a few more bites of pizza each. If we divvy out `6` slices of pizza per person, there will be some slices left over. How many? This is something that we can answer with the `%` operator! What we want is to know the *remainder* after dividing `13 * 8` slices of pizza over `15` people, so we write the program like so:

```python
print("Calculating number of slices remaining...")
print((13 * 8) % 15)
```

We have four slices left over, it seems. We can check our work to verify that this makes sense: `13 * 8` is `104`. `15` goes into `104` `6` times, and `15 * 6` equals `90`. After all `15` people get their `6` slices each, there will be `104 - 90`, or `14` slices remaining. 

### Booleans

Types aren't just about numbers! We can have data types containing values that represent other entities, like *truth* and *falsehood*. The `bool` data type consists of just two values: `True` and `False`. That's it—just those two! They're spelled exactly that way (note the capital `T` and `F`) and they don't take quotes around them like we saw for printed text earlier. `bool` is short for "boolean", which is the name of the system of logic using only these two possible values. 

#### Logical Operators

The `bool` data type comes with a few important operators that represent logic concepts of *conjunction*, *disjunction*, and *negation*; or, more simply, the concepts of "and", "or", and "not", respectively. The operators are spelled out as words in this case, unlike the ones that we used for arithmetic. That is, the operator for "logical and" is literally just: `and`. `or` and `not` round out the trio, and they work by combining boolean values based on the following rules encoded as truth tables below.

| `a`     | `b`     | `a and b` |
| ------- | ------- | --------- |
| `True`  | `True`  | `True`    |
| `True`  | `False` | `False`   |
| `False` | `True`  | `False`   |
| `False` | `False` | `False`   |

To summarize: `and` is an operator that evaluates to `True` only when the left and right operands are both `True`. Otherwise, it evaluates to `False`.

| `a`     | `b`     | `a or b` |
| ------- | ------- | -------- |
| `True`  | `True`  | `True`   |
| `True`  | `False` | `True`   |
| `False` | `True`  | `True`   |
| `False` | `False` | `False`  |

To summarize: `or` is an operator that evaluates to `True` when at least one of the left or the right operands are `True`. Otherwise, if both are `False`, it evaluates to `False`.

| `a`     | `not a` |
| ------- | ------- |
| `True`  | `False` |
| `False` | `True`  |

`not` is an example of a *unary operator*, meaning that it operates on only a single value.

Similar to operators on numeric values, logical operators can be chained together to create longer expressions. These expressions are generally evaluated left-to-right with the official order of operations setting `not` operations to be evaluated first, followed by `and`, then by `or`. This can be a bit confusing to remember, so you are again encouraged to use parentheses liberally in order to enforce your desired order of operations. 


#### Simplifying `bool` Expressions
Let's take a look at a quick example, evaluating `not (True and False) or not True and not False`, where on each line we write a new, simplified expression. 

```python
not (True and False) or not True and not False
# start by evaluating not (True and False), which
# means we need to first solve the contents of the parentheses.
not (False) or not True and not False 
# not (False) is just True
True or not True and not False 
# in order to handle the or, we have to simplify its right side
True or False and not False 
True or False and True 
True or False # from definition of "and"
True # from definition of "or"
```

Therefore, the expression `not (True and False) or not True and not False` has the value of `True`. We can verify that by printing it out:

```python
print(not (True and False) or not True and not False)
```

### Strings
In our very first code example for this course, we had our program print out the message `Hello, World!`. In order to do so, we specified the message as text placed within a pair of quotation marks. Text values like this belong to the data type named `str` (short for "string"). Any sequence of **characters** (individual letters, numbers, punctuation, or spacing like spacebar or tab) placed within a pair of quotation marks can be a `str` value. There is no limit to the number of characters that can be contained in a `str` value.

Here are several examples of `str` values:
- `"Hello, World!"`
- `"Harry S. Smith"`
- `"3330 Walnut Street"`
- `"!@#$%^&*()0123456789"`

When we write out strings in our programs, we can actually enclose them within pairs of single quotes (`'`), double quotes (`"`), or triples of single or double quotes (`'''` or `"""`). This can come in handy when the text you want to represent has one or both of these quote characters within it. 

Here are a few more examples of `str` values, showing off the different quote styles: 

- `'This is a valid str.'`
- `"This isn't a valid str."`
- `"""This is a str with triple "s..."""`
- `'''This is a str with triple 's...'''`
- `"""This isn't "easy" to read, but it is a valid str."""`

Strings are sequences of characters, and it often makes sense to discuss the size or length of a `str` value. In Python, the **length** of a `str` is the number of characters it contains. This includes all characters: letters, numerals, punctuation, spaces. Here is a table of examples, including the lengths of each `str` value.

| `str`         | Length                                                            |
| ------------- | ----------------------------------------------------------------- |
| "Harry"       | 5                                                                 |
| "HarrySmith"  | 10                                                                |
| "Harry Smith" | 11 (the space counts!)                                            |
| "1100?"       | 5 (digits & punctuation count, too )                              |
| "👀"           | 1 (`str` values can contain emojis, which are each one character) |
| " "           | 1 (non-empty because it contains a space bar)                     |
| ""            | 0 (an empty sequence of characters is still a valid `str`)        |

That last `str` there—`""`—is called the "empty string." It's a valid string, and it is a sequence of zero characters.


#### Operators for `str`

There are lots of different ways to manipulate strings in Python, but we'll start by introducing just two simple operators. The first defines the **concatenation** operation, which is the process of joining two strings together end-to-end. The operator itself will look very familiar: `+`!

In order to create the string `"CIS1100"`, we could concatenate the strings `"CIS"` and `"1100"` together like so:

```python
"CIS" + "1100"
```

In order to see the result, we can print it out:

```python
print("CIS" + "1100") # prints CIS1100
```

There are a few important things to pay attention to here. The first is that there is no space added when concatenating two `str` values: `"CIS" + "1100"` takes all three of the characters of the first string and then all four of the characters of the second string with nothing added in between, so the resulting `"CIS1100"` has exactly seven characters. This means that if we concatenate two strings that represent words or names, the result will look a little clumsy:

```python
print("Grace" + "Hopper") # prints GraceHopper
```

In order to put a space between them, we need to add that space as a character to one of the strings.

```python
# both examples print out Grace Hopper
print("Grace " + "Hopper")
print("Grace" + " Hopper")
```

The second important thing to note about the expression `"CIS" + "1100"` is that its second string is, in fact, a `str` value, and *not* an `int` value! Even though the contents of the string are the characters `1`, `1`, `0`, `0` and are therefore all numerals, the fact that they are contained within a pair of quotes means that they are interpreted as components of a `str` value. The importance of this is emphasized by the fact that you cannot concatenate a `str` with a value of another data type in Python. Trying to execute the following line of code will result in an error, including the message "`can only concatenate str (not "int") to str`".

```python
print("CIS" + 1100)
```

Our second `str` operation will be string repetition using the `*` operator. In this case, we can provide a `str` value on the left hand side of the operator and an `int` value on the right hand side of the operator. This number on the right tells us how many times to repeat the text on the left. For example, we could write some lines of code that let your friends know how funny they are:

```python
print("ha" * 1)  # ha
print("ha" * 2)  # haha
print("ha" * 4)  # hahahaha
print("ha" * 10) # hahahahahahahahahaha
```

Or, you could imitate a [villain from a horror movie](https://www.youtube.com/watch?v=4lQ_MjU4QHw):

```python
# I won't share the output here, but try to run this line. 
print("All work and no play makes Jack a dull boy." * 1000)
```

### `None`

This is a special type that contains only a single value: `None`! From the Python documentation: 

> It is used to signify the absence of a value in many situations.

Sometimes we may ask the computer to perform some operation for which there is no result, in which case we might get the answer of `None` in return. There are no operators that can apply to `None`. We will not use `None` much in the beginning of the course, but you should be aware of it as it begins to crop up in later lessons. 

### Relational Operators

There is a group of operators that can be applied to values of different data types, and so we'll conclude our discussion of data types with these, called *relational operators*. These operators provide us ways of comparing two values for order or equality. The output data type is always a `bool`.

#### Equality (`==` and `!=`)

The `==` operator, called "double equals" when read aloud, allows us to ask if two values are equivalent to each other. This operator works with values of any different types. The following table shows a few examples of its usage:

| Expression              | Result        |
| ----------------------- | ------------- |
| `4 == 4`                | `True`        |
| `5 == 4`                | `False`       |
| `4.0 == 4`              | `True`        |
| `"4" == 4`              | `False`       |
| `"4" == "4"`            | `True`        |
| `"4" == "4.0"`          | `False`       |
| `"Comp" == "Sci"`       | `False`       |
| `"Comp" == "Comp"`      | `True`        |
| `True == False`         | `False`       |
| `(4 + 3) % 6 == 3 // 2` | `True`[^expl] |

[^expl]: `(4 + 3)` is `7`. `7 % 6` is `1`. On the right hand side, `3 // 2` is `1` since we're using integer division. So, the expression simplifies to `1 == 1`, which is `True`.

Numbers (`int` and `float` values) are compared based on their numeric value, and so `4` and `4.0` are considered equal. `str` values are compared character-by-character, so `"4"` and `"4.0"` are not equal: their first characters are the same, but they differ after that point. The last row of the table demonstrates that we can compare the results of entire expressions.

We also have the `!=` ("not equals") operator available. It allows us to ask whether two values are different, and it produces exactly the opposite result compared to using `==`. The following table uses the same expressions as the previous table, but replaces `!=` with `==`.

| Expression              | Result  |
| ----------------------- | ------- |
| `4 != 4`                | `False` |
| `5 != 4`                | `True`  |
| `4.0 != 4`              | `False` |
| `"4" != 4`              | `True`  |
| `"4" != "4"`            | `False` |
| `"4" != "4.0"`          | `True`  |
| `"Comp" != "Sci"`       | `True`  |
| `"Comp" != "Comp"`      | `False` |
| `True != False`         | `True`  |
| `(4 + 3) % 6 != 3 // 2` | `False` |

The inclusion of the `None` type in Python means that sometimes we need to ask the question: "does this value exist?" We do so by comparing the result to `None`, e.g. `"yes" * 2 == None` or `4.0 - 3.9999999 == None`. In both cases, and indeed most of the time, the answer is `False`.



#### Ordering (`<`, `<=`, `>`, `>=`)

Sometimes, we may be interested in determining how two values compare to each other: is this less than that? is this number greater than or equal to this other one? These next four operators (`<`, `<=`, `>`, `>=`) allow us to do these comparisons in Python. Like the equality operators, these operators both produce `bool` values as the output type; however, the comparison operators must take in two values of the same type. Values should be both numeric [`int` or `float`], both `str`, or both `bool` on the left and the right hand side. The next table has some examples.

| Expression            | Result                   |
| --------------------- | ------------------------ |
| `4 < 5`               | `True`                   |
| `4 > 5`               | `False`                  |
| `9 <= 9`              | `True`                   |
| `9 < 9`               | `False`                  |
| `"apple" < "banana"`  | `True`                   |
| `"carrot" > "banana"` | `True`                   |
| `"banana" > "banana"` | `False`                  |
| `True > False`        | `True`                   |
| `100 / 12 <= 4.5 * 2` | `True`                   |
| `4 > "howdy"`         | 🚨Error! Type mismatch. 🚨 |
| `True <= None`        | 🚨Error! Type mismatch. 🚨 |


## Example: Leap Years

Let's use our newfound knowledge of these arithmetic, relational, and logical operators to write a program. We'll write code that determines whether or not a year counts as a Leap Year. From Wikipedia:

> A leap year [...] is a calendar year that contains an additional day [...] compared to a common year. The 366th day [...] is added to keep the calendar year synchronised with the astronomical year or seasonal year.

Generally speaking, every four years, we have an additional day in the calendar: February 29th, my half-birthday. But this is actually an oversimplification, since we skip the Leap Year every 100 years in order to be properly aligned. But! That would be too few Leap Years, so we reinstitute the Leap Year every 400 years even though we'd normally skip it due to the 100-year-rule. In short, a year is a Leap Year if:
- The year number is divisible by four and the year number is not divisible by 100, or
- The year number is divisible by 400

In order to write a program that can do this calculation, we'll need a way of determining if a number is divisible by another. Recall that the `%` (modulo) operator has the property that if `a` is divisible by `b`, then `a % b` will be `0`. So, we have the ability to write a few divisibility tests by modding the year and comparing the result to `0`.
- To determine if a year, e.g. `2024`, is divisible by four, we write `2024 % 4 == 0`.
- To determine if a year, e.g. `2024`, is **not** divisible by `100`, we write `2024 % 100 != 0`. (Note the use of `!=` instead of `==`.)
- To determine if a year, e.g. `2024`, is divisible by `400`, we write `2024 % 400 == 0`.

We've now come up with a way to write three "questions" about the year whose answers will be `True` or `False` depending on the divisibility of the year. We still need some way of connecting these three questions into the larger one about Leap Years. We'll combine these smaller questions using logical operators—`and` & `or`—based on our definition of a leap year. Recall the definition I wrote above:

> A year is a Leap Year if the year number is divisible by four **and** the year number is not divisible by 100, **or** the year number is divisible by 400

Notice that the definition above already includes the words `and` & `or`, giving us a pretty strong hint about how to solve the problem! If we replace each of the subquestions about divisibility with the expressions that we came up with to test them, then the program starts to take shape:

> A year is a Leap Year if (the year `% 4 == 0` `and` the year `% 100 != 0`) `or` (the year `% 400 == 0`)

If we replace "year" with a year number that we want to test, we can write a program that gives us an answer to the Leap Year question:

```python
{{#include ../programs/datatypes/leap_year.py::2}}
```

This program prints `True`, which is correct, since 2024 is a Leap Year. Happy half-birthday to me!

To test it on different years, we have to change each instance of the year in the expressions to represent that new year. This can be a little tedious, but we'll see a better way of doing this in the next section. Below is an example of extending the Leap Year program to test three different years. Can you predict what the program should print? When you run it, does it match your expectations?

```python
{{#include ../programs/datatypes/leap_year.py}}
```