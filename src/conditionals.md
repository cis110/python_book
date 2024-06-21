# Conditionals

## Learning Objectives

- Create and evaluate boolean expressions that answer questions about the state of a program's data
- Use `if`, `elif` and `else` keywords to build conditional statements that control the flow of a program 
- Choose among several enumerated possibilities using the `match` & `case` keywords

## Overview

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

As an exercise, you should take a moment to think of

*Boolean expressions* evaluate to `true` and `false` and allow us to test conditions.

*Relational operators* (less than, equals to, greater than, etc.) are used in boolean expressions to compare numeric values or arithmetic expressions
  - `compareTo()` and `equals()` methods are used to compare String variables

*Logical operators* (`&&`, `||`, `!`) are used to combine boolean expressions to build more complex and detailed boolean expressions.



---

# The Boolean Expression Toolkit

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
| `false` | `false` | `false` | `false`  | `true`  |



---

# [Poll Time!](https://www.polleverywhere.com/multiple_choice_polls/6w6yzHnrkrucL5xlTB8iy)




---

# Conditionals

- So far, programs have always executed one statement after another, top to bottom.

- Conditionals allow us to **control the ﬂow of a program** based on the values in the program
  - We say that the `if` statement is a **flow control structure**







---

# If statement

The `if` statement:

- Evaluates a `boolean` expression
- If `true`, executes some statements
- If `false`, skips those statements


> “Choose whether or not to execute a set of statements.”





---

# Flow of Control Using `if`

![bg right:70% w:90%](image-8.png)

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

