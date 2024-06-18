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

The above program *runs*, although it is quite confusing. If you were to write this code and then come back to it a few days late, you might find yourself asking: "Why is `my_name` 27? Shouldn't a name be a string?" You should always make an effort to preserve the type of a variable over time.

Before we move on from updating variables, let's take a look at one last example.

```python
count = 0
count = count + 1
count = count + 2
count = count + 10
print(count) # What gets printed?
```

At a first glance, this might be quite confusing! How do we reassign a variable *in terms of itself?* The answer comes by following the rule described above: *the value stored inside of a variable during assignment is the result of evaluating the right-hand side expression at the moment the assignment is done.* On the first line, `count` is set to be `0`. When the second line is executed, we first evaluate the right-hand side. At this moment, `count` has the value `0` stored inside, so the value of `count + 1` is `1`. We store the value `1` inside of the variable on the left-hand side, which is `count`. After line 2, count now has the value `1`. We repeat the process on line 3: `count` is currently `1`, so we compute the value `3` on the right-hand side and store that inside of `count`, the variable on the left. Repeat once more, where the value of the expression on the right is `13`--can you see why?--and so when we get to line 5, `count` is finally storing the value of `13`, which is what gets printed. Verify this for yourself by running the program.

Reassigning a variable in terms of itself is a common practice. It allows us to count the number of times certain events happen, or to accumulate interest by repeatedly multiplying a quantity by an interest rate, or to run a timer counting down to zero with each passing second.

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

## More Powerful Printing 🖨️

As you've seen in the examples throughout this chapter, it's possible to use `print()` to view the contents of a variable. Want to know what a variable stores at some point in your program? Print it out!

```python
mystery = "hooooo egassem terces"[::-1]
print(mystery)
```

Now that we are capable of writing programs that manipulate data, it will be helpful to have concise but informative ways of printing out one or more values. To start, if you want to print out multiple pieces of information on a single line, each separated with a space, you can do so by interleaving commas (`,`) between the things you want to print.

```python
num_bottles = 99
print(num_bottles, "bottles of beer on the wall,", num_bottles, "bottles of beer...")
# prints out "99 bottles of beer on the wall, 99 bottles of beer..."
```

This is a nice, straightforward way of putting a bunch of different pieces of information on the same output line. Notice that while variables have their values printed, the strings that we put in (recognize them by the `"` characters that surround them) are printed literally. Nowhere in the printed output do we see the literal `n`, `u`, `m`, `_`... characters of `num_bottles`: the name of the variable is not printed.


Each time we write `print()`, the information inside of that print statement all goes on its own line. Modifying the previous program slightly, we see that the extended output is now spread across multiple lines:

```python
num_bottles = 99
print(num_bottles, "bottles of beer on the wall,", num_bottles, "bottles of beer...")
print("Take one down, pass it around!")
num_bottles = num_bottles - 1 # decrease the value stored in num_bottles by one
print(num_bottles, "bottles of beer on the wall.")
```
```
99 bottles of beer on the wall, 99 bottles of beer...
Take one down, pass it around!
98 bottles of beer on the wall.
```

We can take this a step further using *f-strings*. An f-string is a slight variation of a typical string that is denoted by placing an `f` right before the start of the string, as in:

```python
msg = f"this is a simple f-string. You can tell by the f."
```

If we printed out `msg`, the output would be exactly the content of the f-string seen in the example above; that is, on their own, f-strings behave exactly like other strings. The interesting extension that f-strings provide, however, is that we can leave *slots* inside of the f-string to be filled with the result of an expression. The slots are denoted with curly braces (`{}`) and they can be filled with any expression that you want to write. 

```python
age = 27
birthday = "August 29"
print(f"I'm {age}, and after {birthday}, I'll turn {age + 1}.")
```

If we run this program, we'll see the following message printed:

```
I'm 27, and after August 29, I'll turn 28.
```

How do we get that result? Notice that any characters *outside* of the curly brace pairs are printed literally (i.e. `"I'm"`, `", and after "`, `", I'll turn "`, `"."`). The stuff *inside* of the braces is treated as a normal Python expression that is not part of a string. The values of these expressions can be determined based on the variables that have been declared and assigned previously. So, the first slot is filled with the value of the expression `age`, which is `27`. The second is filled with the value of the expression `birthday`, which is `"August 29"`. Finally, the third is filled with `age + 1`, which has the value of `28`. These f-strings can take some getting used to, but they are just about the most concise way to pack a bunch of information into a single line of text. The equivalent way of doing this with commas in the print statement looks like this:

```python
print("I'm ", age, ", and after ", birthday, ", I'll turn ", age + 1, ".")
```

It's not so different, but there's a bit of *fussiness* involved in keeping track of all the quote pairs and commas. I recommend that you practice using f-strings.



[^lie]: This is only true for some data types in Python. Before long we will see examples where this does not hold when dealing with `list` or `dict` values.