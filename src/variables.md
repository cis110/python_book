# Variables

## Learning Objectives
- To know what a variable is
- To be able to declare variables
- To be able to solve problems using expressions of variables & data values


## Overview
Now that we have a good understanding of data types, we have a picture of some of the kinds of information that a computer can represent and manipulate. As we saw in `leap_year.py`, however, even simple questions can be unwieldy when we have to answer them with long expressions written in a single line. We will now introduce **variables**, which allow us to organize the information in our program by giving names to pieces of data.

---


<!-- TODO: Write this up, probably somewhere in datatypes.md since I use the term there a ton. 
# Expressions


A sequence of _**operators**_ and their _**operands**_ (values to act on) that specifies a computation. **Has a resulting value.**

Examples:

- `1 + 2 + 3`
- `240 != 240`
- `(-4 + (4 * 4 – 4 * 1 * 6)) / (2 * 6) >= 0`
- `3.14 * 6.02 - 1000.00`
- `!false && true == false`
--->


## Variables

A **variable** is a **named portion of computer memory used to store a data value**. In this way, a variable is like a box with a name. The box can store any kind of data within it, but it only ever stores one piece of data at a time. The box is given a name, like a label pasted to the front, and placed on a shelf. Whenever we want to use the data stored in the variable, we refer to it by name. This is like searching for the box with the matching label on our shelf and pulling out whatever is contained inside. 

Variables, as the name suggests, are allowed to *vary* overtime. Their contents can be written and overwritten as many times as we like. To continue the analogy, we're allowed to replace the contents of our boxes with something new whenever we need: we simply find the box by name, remove its previous contents, and add something new instead.

Variables allow us to have the computer "remember" data between different lines of our program. We can do our computation in stages now, writing an expression to calcluate an intermediate result and then saving that result inside of a variable for later use. 

To summarize:
- Variables are portions of computer memory that always store a data value.
- Variables have names, which allow us to refer to them throughout a program.
- Variables can have their contents updated throughout a program.

### Declaring Variables

In order to use a variable in Python, it must first be **declared**. **Variable declaration** is the process of creating a variable by giving it a name and an initial value. This is pretty simple to do in Python:

```python
year = 2024
```

In this example, we declare a variable called `year`. It contains the `int` value `2024`. The general pattern for variable declaration is `new_variable_name = <expression>` where the left-hand side contains any valid identifier and the right-hand side consists of any expression, the resulting value of which will be stored inside of the variable. 

Between the name and the initial value of the expression, we have a single equals sign (`=`). This is called the assignment operator, and it should be read as a *assertive statement* rather than a question. When you write the following line, you are putting on your royal crown and waving your golden scepter around, *proclaiming, insisting, demanding that the variable called `first_name` shall absolutely, decisively, incontrovertibly store the value `"Harry"` until further notice.* 

```python
first_name = "Harry"
```

I am being dramatic here for emphasis about something that is often confusing. In algebra, the equals sign is often used as part of a question: "what value or values of `x` make the left- and right-hand sides equal?" That is not what is happening here! We are putting a value in a box, not asking about truth values (that would be done with `==`) or solving equations. 

#### Naming Conventions

In Python, we use `snake_case` to name our variables. Variables should consist only of lowercase letters, underscores (`_`), and digits. Variables should start with a lowercase letter. In order to break up variable names that consist of multiple words, we separate those words with underscores. Variable names should be chosen to be descriptive. There is a tension between being descriptive and being verbose, but editor tools like autocomplete make it easier to stomach longer variable names by preventing you from having to type them out completely. Let's look at a few more variable declarations and observe the style used:

| Declaration                | Comment                                                                 |
| -------------------------- | ----------------------------------------------------------------------- |
| `score = 99.9`             | valid                                                                   |
| `last_name = "Smith"`      | valid                                                                   |
| `is_mouse_pressed = False` | valid                                                                   |
| `isMousePressed = False`   | invalid — use `_` to separate words                                     |
| `avg_pt_ht = 180`          | technically valid, but the use abbreviations make it very hard to read! |
| `avg_patient_height = 180` | a better compromise for the row above                                   |
| `color_2 = "red"`          | valid, although ugly to the author's eye 🤷                              |


### Using Variables

Once a variable has been brought into existence by declaring it, we can use its value inside of other expressions. In this first example, we declare the variable `three`, put the `int 3` inside it, and then immediately print out its value.
```python
three = 3
print(three) # prints out 3
```

We can use variables as part of other expressions. Here, we calculate the value of \\(1.6^2\\) by multiplying `x` with itself:

```python
x = 1.6
print(x * x) # prints out 2.5600000000000005 due to some rounding error.
```

Indeed, we can even declare variables in terms of other variables!

```python
a = 10
b = 20
c = a + b
print(c) # prints out 30
```

It's important to note that the value stored inside of a variable during declaration and assignment is the result of evaluating the right-hand side expression at the moment the assignment is done. That means that on the third line of the previous snippet, we calculate the value of `a + b` based on the values stored inside of `a` and `b`—`10` and `20`—at that time, and then store the result (`30`) inside of `c`. If we later changed the values of `a` or `b`, the value of `c` would **not** be changed as a result. Only an assignment to `c` can change the value of `c`.[^lie]

#### Reassigning Variables
As referenced above, it is possible to change the value stored inside of a variable. The syntax for doing so is actually identical to the syntax for declaring a variable, since in Python we declare a variable by assigning a value to it.

```python
coin = "heads"
print(coin) # prints heads
coin = "tails"
print(coin) # prints tails
```

Updating a variable lets us do things like keep count of how many times an event has occurred or change a person's personal details in a dataset. A general rule of thumb that you will want to keep in mind, though, is that it's not a good idea to change the *type* of information that a variable stores over time. This makes it hard to keep track of what you can and can't do with a variable throughout your program, and it means that probably the name of the variable no longer describes its contents. 

```python
my_name = "Harry Smith"
print("My name is:")
print(my_name)
my_name = 27
print("In three years, I will be:")
print(my_name + 3)
```

The above program *runs*, although it is quite confusing. If you were to write this code and then come back to it a few days late, you might find yourself asking: "Why is `my_name` 27? Shouldn't a name be a string?"

### Leap Year, Redux

Let's use what we know about variables to improve our `leap_year.py` program. We want to make it easier to read, and we want to make it so that we can easily adapt it to test different years without having to change the year number in several different places. To refresh your memory, here is where we left off with `leap_year.py`:

```python
{{#include ../programs/variables/leap_year.py::8}}
```

In order to calculate whether a year is a leap year, we needed to do three divisibility checks on the year number. This means that any time we want to test whether a different year is a leap year, we have to remember to change three different numbers in the same line. This is a bit tedious, and can be remedied by declaring a variable to store the year that we're testing.

```python
{{#include ../programs/variables/leap_year.py:12:13}}
```

Now, if we want to test the year 2023 or 1900 or 200 or 2000, all we need to do is change the value stored inside of the variable `year` and that updated value will be used in the calculation. 

In this case, we are still fitting all three divisibility checks on the same line. In my opinion, this makes the line very hard to read and understand: it's too long, and there are too many different numbers presented without explanation. Instead, we could take each of the divisibility tests and write them as their own individual boolean expressions, saving the result of each in its own variable with a descriptive name:

```python
{{#include ../programs/variables/leap_year.py:20:22}}
```

Finally, we can rewrite the full test in terms of the new variables that we've declared:

```python
{{#include ../programs/variables/leap_year.py:23}}
```

Thanks to our descriptive variable naming scheme, the full leap year calculation is now written in code in almost exactly the same way we would describe it in plain, natural English. Putting all of this together and adding print statements, we now have the following program:

```python
{{#include ../programs/variables/leap_year.py:16:24}}
```

We have spread the program over more lines, but each individual line is now a bit easier to understand. We have generated a program that is *self-commenting*, meaning that it is written in a way that makes the purpose of the code clear without much additional explanation required. This is one of the benefits of Python as a language and it is something that we should strive for in the programs that we write throughout this course.

- Creates a variable
- Associates a variable to a type
  - The type determines how much space (bits) the computer will use to store the value associated with the variable.

Examples
```java
// declaring the variable score
double score;

// declaring the variable age
int age;
```








---

# Variable initialization

<!-- Move to demo of creating a class with variables. Re-emphasize main
Show that variables have to have unique names* -->

Assigns a value to a variable: using the `=` sign
- The value and the type of the variable must be compatible

```java
// declaring and initializing the variable name (one line)
double score = 98.3;
// declaring the variable age (two lines)
int age; 
age = 14;
// declaring and initializing variable isTakingCIS1100 (one line)
boolean isTakingCIS1100 = true;
```



---

# Operations on variables

<!--  -->

- Assignment statement (`=`) initializes or changes the value of a variable previously declared
- Operators can be applied to values to perform computation
	- Variables store values!

```java
// initialize variable x and put the value 1100 in it.
int x = 1100;

// update the value of x to be the result of 2400 + 1400.
x = 2400 + 1400;
```




---

# Variables in Expressions

Variables can be named in expressions, which will use the value stored in the variable as part of the computation:


```java
int x = 12;
int y = x * 30;  // results in y being 360
int z = 20 + y;  // z equals 380
x = x + 1;	    // x equals 13
```




---

# Compound Assignment Operators

<!-- TODO: animate these so only the first row shows up, then the second, then third -->

Shortcuts that do a math operation and assignment in one step!

<!-- ![bg vertical right](../img/variables_types/280Picture4.png)


![bg vertical right](../img/variables_types/280Picture8.png) -->

![](../img/variables_types/280Picture7.png)



---

# Printing a variable

<!-- Go back to codio demo and show how you can print variables -->

Put the variable name without the quotes in the print command


```java
double score = 43.5;
System.out.print(score);
```
Prints `43.5`

---

# Printing a variable
Use the `+` operator to  append the value of a variable to a text in the print command 
```java
System.out.print("Score in game: " + score);
```

Prints `Score in game: 43.5`





---

# Operator Type Errors

<!-- Want to end L1 about here -->

Sometimes mixing variable types and values will result in compiler errors:



`// Wrong value for the specified variable type`

`int pi = 3.14159;`

`double x = true;`



`// Using operators with incompatible/mismatching types`

`int y = 1 + false;`

`boolean z = 110 && 120;`




<!-- ---

# Casting


Type casting converts a variable from one type to another

`(int) `is used to cast a value to `int`

`(int) 3.5 ` `3`

`(double) `is used to cast a value to  `double`

`(double) 3/2 ` `1.5`



Casting applies only to the closest operand

`(double) 3/2` is the same as `((double) 3)/2` or `3.0/2` -->



---

# Live Coding DEMO (Part 2) w/ Variables!

<!-- Should take ~10 minutes

Prints true if N corresponds to a leap year, and false otherwise.
Assumes N >= 1582, corresponding to a year in the Gregorian calendar.
A leap year takes place every four years.
BUT! If the year is divisible by * 100, it's not actually a leap year.
BUT! If the year is divisible by 400, it * is again a leap year! -->

LeapYear.java



Program that will determine if a year is a leap year.


<!-- ---

# Definitions


A **variable** helps us capture and store details about the problem or entity  we are solving or modeling

A **variable** is a **name** that is associated with a **value (data)**

The **value** is stored in a **memory** location in the computer

The **value** can **change** 

A **variable** (value)  must have a **type**

A **type** defines the possible values and the operations that can be performed on those values -->



---

# Modeling with Variables

<!-- Note, for future people working on the slides: the table is animated by having 3 separate tabled layered next to and on top of each other
The top table is just the “information” column
The second from the top is just the “examples” table
And the bottom table contains all three columns (all three instead of just the type column so that the table can be used as a reference for where the other columns should go) -->

| Information / variable | Examples             | Type   |
| ---------------------- | -------------------- | ------ |
| Name                   | Malcom, Maya, Toni,… | Text   |
| Age                    | 13, 15, …            | Number |
| Is a CIS major?        | True , False         | Text   |
| Height                 | 5.7. 6.0, 4.2, …     | Number |



---

# Modeling with variables and Java types

<!--  -->

We are building a program to keep track of the **CIS 1100 students**; we need to record information about them

We update our table to use Java types


What is the Java type of the information you added?

| Information / variable | Examples           | Java Type |
| ---------------------- | ------------------ | --------- |
| Name                   | Malcom, Maya, Toni | `String`  |
| Age                    | 17, 15             | `int`     |
| Is a CIS major?        | True, False        | `boolean` |
| Height                 | 5.7. 6.0, 4.2      | `double`  |


[^lie]: This is only true for some data types in Python. Before long we will see examples where this does not hold when dealing with `list` or `dict` values.