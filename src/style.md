# Code Style

Programming languages are challenging to learn. They each have a brand new **syntax** (an arrangement of characters, punctuation, and words) that must be adhered to in order to be properly interpreted by the computer running the program. It's important to recognize that programming languages are designed to be comprehensible to computers and people alike, and so it is considered best practice to write your programs in a way that is as straightforward and easy to read as possible. 

Consider the following example of a Python program that draws a few shapes:

```python
import penndraw as                pd
pd.filled_rectangle(0.5,.5, 0.1,  0.3)





pd.set_pen_color( pd.HSS_ORANGE )
pd.filled_circle(  0.5, .5, 0.1)
```

This is a functioning program, but... well, it's ugly! We have a bunch of unnecessary whitespace throughout the program: extra space between `as` and `pd` within the first line and several unnecessary lines between the calls to `filled_rectangle()` and `set_pen_color()`. Sometimes we have spaces before and after our parentheses characters but sometimes we do not. Sometimes we have spaces after commas and sometimes we do not. Sometimes we write our number values with a leading `0` and sometimes we do not. 

It's hard enough at the outset of your programming journey to create programs that run at all, so we want to avoid as much unpredictability in the presentation as possible. Observe the following code, which takes the program from above, rewrites it with consistent spacing and formatting, and adds some comments.

```python
import penndraw as pd

#draws a background rectangle
pd.filled_rectangle(0.5, 0.5, 0.1, 0.3)

# draw an orange circle overtop the original rectangle
pd.set_pen_color(pd.HSS_ORANGE)
pd.filled_circle(0.5, 0.5, 0.1)
```

This program behaves in exactly the same way as its original version, but now it is formatted for consistency and clarity. The measure of a program's comprehensibility and presentation is called its **style,** and learning how to write programs with good style is essential for learning how to write programs at all. By following consistent style guidelines, you will be able to more quickly learn and recognize patterns of correct syntax and spot bugs when they occur. Additionally, by having your programs formatted neatly and in conventional ways, it will be easier for members of the course staff to quickly understand your code and to spot errors in the syntax. You can read the full course style guide [here](https://www.cis.upenn.edu/~cis110/current/resources/style.html) (TKTKTK!), although it does cover a number of features of the language that we have not yet introduced. For now, here are a few important points to follow:
- Place only one space between tokens (words, numbers, characters) when a space is required
- Limit your line length to 80 characters at the most; any longer and the line is both hard to read and to understand
- Add comments to specify the purpose of each logical block of code. It is possible to write too many comments as well as too few comments, but you should err on the side of "overcommenting" as a beginner.
- Start each file that you submit with a header comment including your name, PennKey, recitation number, example program execution, and a description of the purpose of the program.
  - The example program execution is often just `python my_file_name.py`, but we will see in a few chapters how program executions can vary.
  - The description of the program does not need to be verbose; a short explanation of what happens when the program is run is sufficient.
- When providing arguments to a function (e.g. specifying dimensions and positions for drawing shapes or choosing RGB values for colors in PennDraw),
  -  provide a single space after each comma before the next argument.
  -  do not add a space after the open parenthesis (`(`) or before the close parenthesis (`)`).
-  Numbers between -1 and 1 should always have a leading `0` provided for clarity (i.e. write `0.7` instead of `.7`)