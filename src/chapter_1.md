# Hello, World!

## Our First Program

It's a longstanding tradition in introductory programming courses to start with one specific program: Hello, World. The purpose of this program will be to print out a message—`Hello, world!`—when the program is run. In some languages, this takes a fair amount of effort. Fortunately, Python makes it easy. Let's take a look. 

Filename: `hello_world.py`
```python
print("Hello, world!")
```

That's it! Now, let's see what it does. In order to run the program, you can either press the "Run" button at the top of Codio or navigate to the console, type `python hello_world.py`, and hit enter/return. When you run the program, you should see exactly the message `Hello, world!` displayed as output. 

```console
$ python hello_world.py
Hello, world!
```

Let's run through a very detailed breakdown of all of the different pieces that went into this short program. 

### Naming the File
We wrote our program in a file called `hello_world.py`. The name of the file doesn't matter so much, but you should name your programs in a way that indicates what they do! You'll also notice the unusual way we stylize certain names in Python programs. As a general rule, we'll name our files (and, later, variables & functions) all in lowercase with words separated by the underscore (`_`) character. This is called *"snake case"*; or, following its own rules: *snake_case.*

### 🖨️ Printing
When I wrote above that the program will "print out a message," you may have noticed that I didn't mean that we will literally be printing ink on paper. *Printing* in the context of programming refers to *displaying text on the computer screen.* 

Printing in Python is accomplished using the `print()` function. *Functions* are named pieces of code that can be invoked by writing their names. We will return in much greater detail to this topic later in the course. `print()` allows you to *pass in* (or specify) a piece of information that should be printed. 

### Text and `strings`
When we want to print a message, we surround the text of the message in quotes. This clarifies to Python that the stuff inside of the quotes should be treated as a sequence of characters called a `string`. The contents of the `string` will be interpreted literally rather than as other pieces of a program. In this case, Python recognizes `"Hello, world!"` as a message to display; without the double quotes character (`"`) at the start and end, Python's interpreter will assume that `Hello, world!` is some kind of instruction. Since this inadvertant instruction is nonsensical, the program will crash with an error! We can see an example of this below.

Filename: `hello_world_quoteless.py`
```python
print(Hello, world!)
```

Running the above program produces the following error message:
```console
$ python hello_world_quoteless.py
  File "/python-book/programs/hello_world/hello_world_quoteless.py", line 1
    print(Hello, world!)
                      ^
SyntaxError: invalid syntax
```

We'll take a more detailed look at error messages later on.

## All This Explanation for One Short Program?

We wrote our first program using just one line of code, and yet we had a lot to break down and discuss. Programming languages are remarkably dense with meaning and computers are very uncharitable in how they try to read your programs: diverge from the expected syntax by even one character and your program will crash! When you learn to program, there are two significant challenges you face: becoming familiar with the rules and constraints of a programming language, and thinking with abstractions. Be patient, and pay careful attention to each line of code that you write so that you start to get familiar with the requirements of Python! You will make mistakes, but the course staff is here to help you get unstuck.

## Comments

Here is a modification of our `hello_world.py` program:

```python
# displays a greeting message
print("Hello, world!")
```

If you make this modification and run it for yourself, you'll observe that the output of the program is...

```console
$ python hello_world.py
Hello, world!
```

...exactly the same as it was before! That's because the stuff we added above is an example of a **comment.** A comment is a portion of a program denoted with the `#` character that is ignored by the computer when the program is run. Comments are exclusively for human usage and they do not affect how the program behaves. Common uses for comments include:
- Writing a "header" for your program that marks who the author is, how the program is intended to be used, and a listing of all of the features it contains.
- Explaining the purpose of an individual piece of code for another programmer or for yourself in the future.
- Marking a portion of code as "TODO", i.e. to be fixed or finished at a later time.
- Taking notes about things that aren't working or questions you have so that you can get help on them from the course staff in the future.

Any text following a `#` character on a line (and the `#` character itself) are ignored by the program. Comments can be left above the code they are referencing or at the end of the lines they are explaining. You will be required to use comments throughout this course.

```python
# Name: Harry Smith
# Pennkey: sharry
# Execution: python hello_world.py
# This is a program that prints a simple greeting message.

# This next line of code does the printing.
print("Hello, world.") # This is a print statement.
```

This example above is vastly "overcommented"—you will never need to write so many comments that they outnumber the lines of code in your program—but it shows an example of a program header (the block of comments at the top of the program), a comment placed before a line of code, and a comment placed at the end of a line of code. 

## Order of Execution

The order in which the statements inside of a Python program are executed is referred to as the **control flow**. Although we will eventually be able to manipulate control flow in some fairly complex ways, our first programs in Python will always exhibit the default control flow. Lines of code in your program will be executed one at a time from top to bottom. We could write a new program inside of the file `hello_everybody.py` that looks like this:

```python
{{#include ../programs/hello_world/hello_everybody.py}}
```

Each line of the program is a single print statement that will display a message on its own line of the output. If we run the program, we'll see the messages printed in the following order:

```console
I'd like to say hello to my friends.
I'd like to say hello to my family.
I'd like to say hello to my fans.
I'd like to say hello to you.
```

The first line of code in the program is executed first, and so `I'd like to say hello to my friends.` appears on the first line of the printed output. The second line is executed next, and so `I'd like to say hello to my family.` appears on the second line of the printed output. This pattern continues; to reiterate, Python programs are executed from top to bottom, one line at a time, starting at the top of the file.

As an exercise, can you rearrange the lines of the program `hello_everybody.py` so that the messages are printed in the following order instead? This is good practice not just for understanding control flow but also for making sure that you can modify a program and run it after you've made your changes.

```console
I'd like to say hello to my family.
I'd like to say hello to you.
I'd like to say hello to my fans.
I'd like to say hello to my friends.
```


## Reading User Input

These two previous programs—`hello_world.py` and `hello_everybody.py`—behave the same way each time they're run, but programs don't always need to work this way. Much of the software that will be most familiar to you (social networks, streaming services, messaging apps) is useful because you can interact with it. To write a program of our own that works in this way, we can introduce the `input()` command.

```python
# Execution: hello_input.py
print("Who would you like to say hello to?")
name = input(">")         # Reads message from user, saves it
print("Hello, ", name)    # Prints the user's message out again
```

`input()` prints out whatever prompt is provided between the parentheses, pauses the program, and waits for the user to type in some information and then press return/enter. Then, whatever message the user typed in is saved within the program to be used later. When we want to see what information the user provided, we can do so by printing out `name`. `name` is a **variable**, which is a concept we will introduce in far greater detail soon. Try running `hello_input.py` and then typing your own name into the terminal while the program is running:

```console
$ python hello_input.py
Who would you like to say hello to?
> Harry
Hello, Harry
```

Each time you run the program, you can provide a different name to be greeted. While simple, this is the first program that provides a meaningful example of an **algorithm**. In traditional Computer Science, an algorithm is a finite set of steps that takes in some input information or data and produces some value as an output. Here, we have a very short algorithm that takes in a name from a user and produces a greeting for that name. As we proceed through this course, we will learn to write programs that represent much more complicated algorithms. We will also discuss how these traditionally defined algorithms compare to those algorithms that are defined in a more contemporary sense of the term, as in "the algorithm" or "AI algorithms."