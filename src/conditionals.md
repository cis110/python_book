# Conditionals

## Learning Objectives

- Create and evaluate boolean expressions that answer questions about the state of a program's data
- Use `if`, `elif` and `else` keywords to build conditional statements that control the flow of a program 
- Choose among several enumerated possibilities using the `match` & `case` keywords

## Overview

> *"You ever made a decision?"* 
> 
> *"No, I never did that."* 
> -- Joan Didion, *Play It as It Lays*

Earlier on, we introduced the concept of **control flow** in a program as the order in which its lines of code are executed. Our first programs used only the default control flow, wherein lines are executed from top to bottom and only time each. This was sufficient for simple calculations, printing, and programs that made static drawings, but it does not allow for our programs to make any *decisions*. In this chapter, we will apply our knowledge of **boolean expressions** and introduce new control structures in order to write programs that are capable of making choices based on information available to them.


## Conditions & Conditionals

In order to write programs that respond to different situations, we'll need to introduce the concepts of **conditions** and **conditionals**. Conditions are defined as the states of the data in your program. A program's data can include things like values stored inside of variables, information requested from outside sources like the internet, or user input like mouse clicks and button presses. Conditions are defined using **boolean expressions**, or expressions of values and variables that evaluate to a boolean type. You can refer to the chapter on [data types](datatypes.md#booleans) for a refresher on the `bool` type and expressions that produce boolean values.

**Conditionals** are the structures that we use to make decisions based on the conditions that we define. These decisions take the form of questions like: "which of these actions should I take?" or "should I choose to do this next step?" 

An example of a *condition* that you would be aware of as a pedestrian in Philadelphia is whether or not the light facing you at an intersection is currently green. This condition could be true or false—the light might be green, or it might currently be yellow or red instead. The *conditional* that you use in your "walking program" is that if the condition is met; that is, *if the light is green*, then you will cross the intersection. If that condition is not met and the light is not green, then you will wait. 


---

## Conditions as Boolean Expressions

Recall that boolean expressions are expressions that evaluate to `bool` values, i.e. either `True` or `False`. Our first boolean expressions were fairly straightforward and had consistent and predictable results.

```python
3 > 4 and 9 == (81 / 9)                     # always True
not True and True or False and not False    # always False
```

Now that we are familiar with the concept of variables, we are able to write boolean expressions that will produce different results based on the values stored within those variables. For example, without context, it's impossible to evaluate whether the following expression is `True` or `False`:

```python
x % 3 == 2 and x > 5
```

`x`, as a variable, could store any number at all. The result of this expression depends on the value that we've placed in that box. *Can you think of a value of `x` that would cause the expression to evaluate to `True`? What about `False`?*

```python
# What values of x would make this program output True?
# What about False?
x = ??? # Change this line and run the program to experiment.
print(x % 3 == 2 and x > 5) 
```

When we use variables as part of boolean expressions, we are able to test conditions about the state of the world that our program represents. We build these boolean expressions by comparing values with *relational operators* and combining other boolean expressions together with *logical operators.*


### Worked Examples of Writing Expressions to Test Conditions

*"Is the number of tickets sold equal to the capacity for the venue?"* or *"Is the user's password long enough to be valid and is it different from their username?"* are the kinds of useful questions that we can formalize as boolean expressions with variables: sometimes the answers will be "yes" and sometimes "no", all depending on the values stored in the underlying variables.

```python
print("Is the number of tickets sold equal to the capacity for the venue?")
print(num_tickets == venue_capacity)

print("Is the user's password long enough to be valid and is it different from their username?")
print(len(password) >= 8 and password != username)
```

To determine if a password is long enough, we compare the length of the password (`len(password)`) to a fixed minimum length of `8` using the `>=` operator. To check to see if a user's `password` and `username` are different, we use the `!=` ("not-equals") operator to compare them. In order to combine these two smaller boolean expressions into a large one that models our condition, we join the two using the logical `and`: the condition of whether or not a password is acceptable is met if and only if the password is both long enough and distinct from the user's username.

#### One-Way Streets in Center City

In Center City Philadelphia, a numbered street is one-way heading South if its number is even and its number is not 14.[^broad] Try practicing the process of modeling conditions by writing a boolean expression that whether or not a street is one-way heading South: *"Is the given street number even and is its number not 14?"*
To answer this question, we'd need to know the street number. It's not specified in the question, which means that we'll think of it like a variable: `street_number` seems like a suitable name. 

Next, we need to know how to test whether or not a street number is even to build the first part of the boolean expression. A number is considered even if it is divisible by two, and we can test divisibility using the modulo (`%`) operator: `street_number % 2 == 0` is an expression that evaluates to `True` when `street_number` is even.

Then, we have to be able to test if our street number is not 14. Like we did in the password example, we can use the `!=` operator to have a comparison evaluate to `True` when the two values being compared are different. `street_number != 14` evaluates to `True` when `street_number` does not store the value `14`.

Finally, we can build our full condition by combining these smaller boolean expressions together with a logical operator. We want the condition to be `True` *only when* both sub-expressions are `True`; that is, when the street number is even **and** the street number is not 14. This will be a good use of the `and` operator.
```python
street_number = 2 # Change this line and run the program to experiment.
print(f"Does {street_number} Street run one-way south in Center City Philadelphia?")
print(street_number % 2 == 0 and street_number != 14)
```


[^broad]: "14th Street" doesn't actually exist in Philadelphia: we call it Broad Street instead. Furthermore, Broad Street is a two-way street instead of a one-way.

<!-- # The Boolean Expression Toolkit

#### Relational Operators
| Operator/method | Input Types                | Description                                    |
| --------------- | -------------------------- | ---------------------------------------------- |
| `<` / `<=`      | `int` & `double`           | less than / less than or equal to              |
| `>` / `>=`      | `int` & `double`           | greater than / greater than or equal to        |
| `==` / `!=`     | `int`, `double`, `boolean` | equal to / not equal to                        |
| `.equals()`     | `String`                   | equal to                                       |
| `.compareTo()`  | `String`                   | returns -ve, 0, or +ve `int`, not a `boolean`! |

---

# The Boolean Expression Toolkit

#### Logical Operators
| Operator/method | Input Types | Description                                                               |
| --------------- | ----------- | ------------------------------------------------------------------------- |
| `&&`            | `boolean`   | logical "and", evaluates to `true` only if both inputs are `true`         |
| `\|\|`          | `boolean`   | logical "or", evaluates to `true` as long as at least one input is `true` |
| `!`             | `boolean`   | logical "not", negates a single `boolean` value to its opposite           |

---

# Truth Tables

| P       | Q       | P && Q  | P \|\| Q | !P      |
| ------- | ------- | ------- | -------- | ------- |
| `true`  | `true`  | `true`  | `true`   | `false` |
| `false` | `true`  | `false` | `true`   | `true`  |
| `true`  | `false` | `false` | `true`   | `false` |
| `false` | `false` | `false` | `false`  | `true`  | --> |

## Conditionals: `if`, `elif`, and `else`

**Conditionals** allow us to control the flow of a program based on conditions defined using the values in the program. Conditionals are defined in Python using three special keywords: `if`, `elif`, and `else`. We will start by introducing the `if` statement.

### The `if` Statement

> *"`if` music be the food of love, play on."* — William Shakespeare
>

Whereas before we executed all lines of code in the program from top to bottom, our first conditional—the `if` statement—will allow us to specify a portions of our program that should be run only if a certain corresponding conditions are met. We can understand the behavior of `if` statements by examining the flow chart below:

![Copied from CSAwesome, authored by Barbara Ericson (barbarer@umich.edu), Beryl Hoffman (hoffmanb@elms.edu), Peter Seibel (peterseibel@berkeley.net). Attribution provided pursuant to CC BY-NC-SA 4.0 License, https://creativecommons.org/licenses/by-nc-sa/4.0/](img/conditionals/if-flow.png)

On reaching the `if` statement, we test a condition. If that condition is `True`, then we execute the corresponding statement or block of statements. If the condition is `False`, then we skip over all corresponding statements and resume program execution at the first line of code following the skipped statements. The motto to remember when you see a single `if` statement is: *"I am now choosing whether or not to do something."*

The `if` statement is built using the `if` keyword, a boolean expression followed by a colon (`:`) and a body of statements indented one level further than the line with the `if`. The structure for such a statement looks like this:

```python
if my_boolean_expression:
	statement_one
	statement_two
	...
	statement_last
```

For example, perhaps we want to write a program that helps us determine whether or not a variable `num` is divisible by `5`. We can start by assigning `num = 10` and observing the result.

```python
num = 10
print("Printing a message if {num} is divisible by 5...")
if num % 5 == 0:	# if, followed by our boolean expression defining the condition
	print("Yes!")	# the statement to be executed if condition is met
```

When the program is run, we get the following output:
```console
Printing a message if 10 is divisible by 5...
Yes!
```

Success! Since `10` is divisible by `5`, our boolean expression `num % 5 == 0` evaluates to `True`: our condition is met. So, we evaluate the statements in the indented block following the line with `if`. In this case, that is a single line: `print("Yes!")`. Our output consists of two printed lines.

We could change the value of `num`, thereby changing the state of our program, and observe the result.

```python
num = 11	# Trying again but changing 10 --> 11
print("Printing a message if {num} is divisible by 5...")
if num % 5 == 0:	# if, followed by our boolean expression defining the condition
	print("Yes!")	# the statement to be executed if condition is met
```

When the program is run, we get the following output:
```console
Printing a message if 10 is divisible by 5...
```

Only one line is printed! The condition is not met—`num % 5 == 0` evaluates to `False` this time—and so we skip all statements in the indented block. Remember: with an individual `if`, you are *choosing whether or not to do something*.
---

# Code Blocks


Code blocks are associated groups of statements that are executed together and that have the same level of *scope*.
  - Curly Braces (`{}`) denote the start and end of code blocks.
  - Scope refers to the region of the program where variables are able to be accessed after declaring


---

# Structure of If statement 

```java
// a single if statement
if (4 < 5 && !"Harry".equals("Smith")) { // start a new code block
  System.out.println("Drawing a circle if condition is true");
  PennDraw.circle(0.5, 0.5, 0.1);
}
// statements outside of if are run no matter what!
System.out.println("Drawing a square no matter what.");
PennDraw.square(0.5, 0.5, 0.1);
```



---

# Exercise: What Gets Printed?
![](../img/conditionals/267Picture4.png)

---

# Exercise: What Gets Printed?


```java
if (true) {
  System.out.println("Apple");
}
if (10 > 10) {
  System.out.println("Banana");
}
if (10 >= 10) {
  System.out.println("Cherry");
}
```



---

# [Poll Time!](https://www.polleverywhere.com/multiple_choice_polls/rEMiFXHtJn4Br9HkglfsD)



---

# The `else` Statement

<!--  -->

“Which **one** of these two options should I pick?”

![bg right:70% w:90%](../img/conditionals/268Picture4.png)



---

# Structure of If-else statement 

```java
if (4 < 5 && !"Harry".equals("Smith")) { 
  // start a new code block to run if condition is true
  System.out.println("Drawing a circle if condition is true");
  PennDraw.circle(0.5, 0.5, 0.1);
} else { 
  // start a new code block to run if condition is false
  System.out.println("Drawing a line if condition is false");
  PennDraw.line(0, 0, 1, 1);
}
// statements outside of if-else are run no matter what!
System.out.println("Drawing a square no matter what.");
PennDraw.square(0.5, 0.5, 0.1);
```



---
# [Poll Time!](https://www.polleverywhere.com/multiple_choice_polls/Ww0qdeTgmHsGrLQluP71i)

---

# Nested if statements

The body of a conditional contains a sequence of statements

The **if** statement is, itself, a statement!

- So: you can put a conditional inside of another.
- “Only If **X** is true, then I’ll check if **Y** is true...”



---

# Nested if statements

![](../img/conditionals/308Picture2.png)



---

# Nested if statements

Follow the curly braces to figure out which “if” the “else” belongs to!

(in this case, it’s the first one)

![bg right:65% width:80%](../img/conditionals/280Picture3.png)



---

# [Poll Time!](https://www.polleverywhere.com/multiple_choice_polls/hNtXaMpFGoC4EUAv5KYx9)

---

# `if`-`else if`-`else` statements

A conditional with three or more mutually exclusive options



Of the statement blocks, exactly one will execute

- (if you leave off the last **else**, then exactly 0 or 1 will execute)



---

# `if`-`else if`-`else` statement 

![height:70%](../img/conditionals/270Picture4.png)


---

# Can you go to see your friend at the park?

```java
boolean isNearby = true;
boolean haveHomework = true;
if(!isNearby) {
  System.out.println("no, too far");
} else if (haveHomework) {
  System.out.println("no, do HW");
} else {
  System.out.println("yes, go see them");
}
```

---
## The Grammar of the Conditional

A conditional statement consists of one essential part—the `if`—and several optional parts.

1. Begin with an `if` statement. The `if` statement must include a boolean expression to test.
2. Optionally, include any number of `else if` statements. Each `else if` statement must include a boolean expression to test. Any conditional may include zero or more `else if` statements.
3. Optionally, include an `else` statement. The `else` statement does not include a boolean expression to test. Any conditional may include zero or one `else` statements.

---
## Some Examples



```java
if (x > y && x > z) {
  System.out.println("x is the largest");
} else if (y > x && y > z) {
  System.out.println("y is the largest");
} else if (z > x && z > y) {
  System.out.println("z is the largest");
} else {
  System.out.println("two or more variables are tied for largest");
}
```


```java
if (a > b && a % b == 0) {
  System.out.println("a is divisible by b");
} else if (b > a && b % a == 0) {
  System.out.println("b is divisible by a");
}
```


---

# Live Coding: Parking Sign

<!--  -->

![bg vertical right](../img/conditionals/293Picture2.png)

