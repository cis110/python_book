# Command Line Arguments

We learned [earlier](./chapter_1.md) about `input()`, which allows us to prompt the person running the program to type something into the computer while the program is running. In this section, we will introduce **command line arguments** as a way to pass information into a program at the very beginning of its execution.

## Running Programs from the Terminal

Remember that we can run any Python file from the terminal by typing `python <filename>.py`. 

For example, we have the following program, `random_color.py`, that displays a color chosen at random by selecting its `red`, `green`, and `blue` components. We can run it with `python random_color.py`.

```python
# random_color.py
import random
import penndraw as pd

red = random.randint(0, 255)
green = random.randint(0, 255)
blue = random.randint(0, 255)

pd.text(0.5, 0.2, f"({red}, {green}, {blue})")

pd.set_pen_color(red, green, blue)
pd.filled_square(0.5, 0.5, 0.2)

pd.run()
```

## From Random to Chosen

What if we wanted to write a program that displayed a specific color instead of a random one? We could try this with `input()`, as we do below. Keep in mind that the data typed by the user will always be stored as a `str` by default. In order to convert this information to a useable form, we'll need to call `int()` on the provided red, green, and blue values.

```python
# input_color.py
import penndraw as pd

# prompt the user for the color choices
red = input("Choose red: ")
green = input("Choose green: ")
blue = input("Choose blue: ")

# convert the inputs to int values before using them

red = int(red)
green = int(green)
blue = int(blue)

pd.text(0.5, 0.2, f"({red}, {green}, {blue})")

pd.set_pen_color(red, green, blue)
pd.filled_square(0.5, 0.5, 0.2)

pd.run()
```

Now, when we run the program, we see the following behavior when we want to visualize the color `(100, 40, 180)`:

```console
$ python input_color.py
Choose red: 100
Choose green: 40
Choose blue: 180
```

This allows us to choose our color, but it does require us to enter all three values on different lines, being prompted each time. This is not a problem, but if we are willing to decide on the color that we want to see by the time we run the program, we have another potential solution.

## Command Line Arguments

**Command Line Arguments** are parameters passed along to the program at the time that it is being executed. These arguments are provided at the **command line**, or terminal, when the program is run. Any information placed on the execution line after the initial `python <filename>.py` portion is considered to be a command line argument. For example, we could run a program like so:

```console
$ python cla_color.py 100 40 180
```

Python still runs the program `cla_color.py`—the difference is that the values of `"100", "40", and "180"` are available within your program by accessing the `sys.argv` list. `sys` is the name of a built-in Python library that handles "system" stuff, most of which is actually exceedingly complicated and beyond the scope of our course. `argv` is the one member of the `sys` library that is useful for our purposes. Short for "(command line) argument vector", `argv` is a list that stores all of the values passed in after `python` when the program is run from the command line. In general, we can inspect the command line arguments by using the following pattern, encapsulated here in `echo_argv.py`:

```python
# echo_argv.py

import sys
print(sys.argv)

```

Then, we can run this program with several different command line arguments passed in at execution:

```console
$ python echo_argv.py
["echo_argv.py"]
$ python echo_argv.py 100 40 180
["echo_argv.py", "100", "40", "180"]
$ python echo_argv.py yes True 14.9 -101-09
["echo_argv.py", "yes", "True", "14.9", "-101-09"]
```

A few things to note:
- The values passed in as command line arguments are stored in the same order in `sys.argv`
- Values are always interpreted and stored as strings—not numbers or booleans
- The first command line argument is actually the name of the file itself!
  - This is kind of annoying and useless most of the time
  - Sometimes can be helpful for a program to know its own name, though
- There is (practically) no limit to the number of command line arguments you can provide
  - This is true no matter how many arguments you expect your user to provide...

Circling back to our color demonstration example, we can ask the user to provide the colors as command line arguments and handle them like so: 

```python
# cla_color.py
import penndraw as pd
import sys

# prompt the user for the color choices
red = int(sys.argv[1]) # CLA at position 0 is filename, so position 1 is red
green = int(sys.argv[2])
blue = int(sys.argv[3])

pd.text(0.5, 0.2, f"({red}, {green}, {blue})")

pd.set_pen_color(red, green, blue)
pd.filled_square(0.5, 0.5, 0.2)

pd.run()
```

## Summary

Both `input()` and command line arguments are valid ways of making a program vary its execution based on information provided by a user. Whereas `input()` allows a program to ask for user input while it is running, command line arguments are decided upon and provided before the program starts to execute.

To access command line arguments inside of a program, you must `import sys` so that you have access to the list `sys.argv`. This list stores all of the command line arguments as strings in the order in which they were provided in the execution command. 