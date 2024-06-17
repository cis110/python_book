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

## All This Explanation for One Line of Code?

We wrote our first program using just one line of code, and yet we had a lot to break down and discuss. Programming languages are remarkably dense with meaning and computers are very uncharitable in how they try to read your programs: diverge from the expected syntax by even one character and your program will crash! When you learn to program, there are two significant challenges you face: becoming familiar with the rules and constraints of a programming language, and thinking with abstractions. Be patient, and pay careful attention to each line of code that you write so that you start to get familiar with the requirements of Python! You will make mistakes, but the course staff is here to help you get unstuck.
