# Animations & Interactivity in PennDraw

> *"There was some projection, constant in the back of his mind, of this consistent inescapable play of light."*
> -- Eugene Lim, *Fog and Car*

We've used PennDraw to draw plenty of static images. We've learned how to use conditionals to influence the control flow of a program. Now, we can put these ideas together! First, we'll introduce a new keyword—`while`—to further expand our control flow toolkit and allow us to created animated drawings. Then, we'll integrate a few PennDraw tools that allow us to write conditions based on mouse and keyboard input. These will be interactive programs that respond to users while the program is running. 

## Animation in PennDraw

To draw a static image, we chose a set of different marks to make on the canvas—points, lines, shapes, and text. For each mark we wanted to make, we chose position and size parameters so that these elements appeared where wanted. We ordered these drawing commands relative to other pen settings so that each mark appears with the proper color and thickness. All of these choices were made **once** to draw a single image. 

In order to create an animation, we need to be able to draw a new image many times per second. This is not unique to PennDraw; indeed, all computer animations work in this way, from cartoons to video games to CGI in movies. Even old-school movies use a physical version of the same scheme: analog film is a series of **frames**—still images—that get projected through a projector at a rate of 24 per second. Any rapid succession of images tricks our eyes into believing that we are seeing something that is actually moving. 

In a PennDraw animation, we use this old-school film term of **frame** to describe a single drawing that we show for one-thirtieth of a second. Our programs for drawing will be expanded in a way that allows us to decide upon a set of shapes to include in our animation, draw them for the current frame, and then decide how the shapes properties will change in advance of the next frame. It is this loop of drawing and changing that allows us to simulate motion.

## Basic Animation Recipe

The basic recipe for animation in PennDraw consists of a three-part process. The first part is the **setup**, wherein we choose initial settings for our drawing and declare variables that will be used in the drawing of our shapes.

### Setup

The setup of a PennDraw animation consists of steps that we need to take exactly one time before our program starts. This is where we import PennDraw, choose our canvas size, and decide on other settings for the program.

This preamble is also where we will want to declare any variables that we will use throughout the animation and give them their initial values. Variables allow us to specify the way in which we want our drawing to look in each frame without knowing the value that's stored in the variable, and so they're very useful for animation. This will make more sense when we look at the remaining components of the typical animation program. For now, take a look at an example of a setup for a program that defines an animation:

```python
import penndraw as pd
# SETUP: This code is run just one time!
pd.set_canvas_size(500, 500)
x_center = 0.5
pd.set_pen_color(pd.HSS_BLUE)
# ...
```

### The Animation Loop

Next up, we write the part of the program that decides how each frame of the animation gets drawn. This requires some new machinery.

#### `while`

In a future chapter, we will discuss looping and iteration in great detail. For now, we introduce the `while` loop in a limited context: the `while True` loop.

First, recall the structure of an `if` statement: we provide a condition to test, and when that condition evaluates to `True`, there is a series of statements we execute as a result. That condition that accompanies the `if` can be any expression that evaluates to a `bool` value, including the expression of just `True`:

```python
if True:
    print("This happens always.")
```

That's not a very useful conditional to write. In fact, you could just delete the conditional and put the print statement in its place, since it will always be executed. This is because conditionals are only tested *once* when they are reached for the first time.

`while` is a keyword that is also accompanied by a condition. They behave the same way the first time they are reached: in both cases, we test the condition and execute a corresponding body of statements in the event that the condition is `True`. The difference is that *we return to the condition of the `while` loop* when we finish executing the body of the loop.

```python
while True:
    print("I'm stuck!")
```

If you try to evaluate the program above, you'll see `I'm stuck!` printed over and over into infinity. The first time we reach the line with `while True:`, we find that `True` is `True`, and so we print the message. Since this is a `while` loop, we return to test the condition again. `True` will always be `True`, and so we print & test, print & test, print & test...

We'll discuss how to use `while` loops with different conditions, but it turns out that these infinite `while` loops actually come in handy for our goals with animation.

#### Loop Structure

The rest of our animation program will typically live inside of an infinite `while` loop. This allows our animation to proceed forever and ever until the program is manually halted. Within each **frame**—each execution of the `while` loop from top to bottom—we'll typically do the following in order:

1. Decide whether to clear the screen
2. Draw the next frame based on current properties of the shapes
3. Update the properties of the shapes
4. `pd.advance()`

Here's an example of a simple program that draws a square sliding from left-to-right across the screen:

```python
# SETUP
import penndraw as pd
pd.set_canvas_size(500, 500)
x_center = 0.5 
pd.set_pen_color(pd.HSS_BLUE)
while True: # ANIMATION LOOP
    pd.clear()                            # 1. clear the screen
    pd.filled_square(x_center, 0.5, 0.1)  # 2. draw this frame
    x_center += 0.01                      # 3. update shapes for next frame
    pd.advance()                          # 4. pd.advance()
```

The animation loop clears the previous drawing of the square, draws the square in its new location (in terms of the variable `x_center`), updates the value of `x_center` to be slightly bigger than it was before, and then calls `pd.advance()`.

By drawing the square each time in terms of the variable `x_center`, we are able to control how that square appears over time. In particular, with each passing frame, we make `x_center` slightly bigger than it was in the previous frame. Since the first argument passed to `pd.filled_square()` dictates the horizontal position of the square on the screen, this means that each passing frame will draw the square slightly further to the right. In fact, at some point, `x_center` will become so large that the square is drawn totally offscreen.

The last line of this loop (and any animation loop you write) is just `pd.advance()`. This tells PennDraw to draw everything for this frame all at once and then wait until the next call before updating the screen again. This is necessary to keep the animation smooth and steady. **Much like with `pd.run()`, your program will not draw anything if there is no call to `pd.advance()`** Relatedly, in programs with these infinite while loops, it is no longer necessary to include a call to `pd.run()` at the end of the program. 

This pattern of clear-draw-update enables us to describe each frame in general terms and define how the properties of the frame change over time.


#### Clearing the Screen

When we clear the screen at the start of the frame, that means that the previous frame's shapes will disappear. This is helpful in the case that we want to avoid leaving a "trail", but it may be useful in some applications to leave the previous frame's information on the screen. For simple animations without interaction (i.e. our first few programs in this genre), we'll usually clear the screen at the start of each frame.

Try running this program with and without `pd.clear()` commented out. What is the visual difference in the output?

```python
# SETUP
import penndraw as pd
pd.set_canvas_size(500, 500)
x_center = 0.5 
pd.set_pen_color(pd.HSS_BLUE)
while True: # ANIMATION LOOP
    # pd.clear()                            # 1. clear the screen
    pd.filled_square(x_center, 0.5, 0.1)  # 2. draw this frame
    x_center += 0.01                      # 3. update shapes for next frame
    pd.advance()                          # 4. pd.advance()
```