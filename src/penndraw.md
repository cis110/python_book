# PennDraw

As we move beyond `hello_world.py` and printing text, we will begin to write programs for drawing images and animations. We want you to get more comfortable with both reading and writing programs, and computational art is a good place to start. It allows us to get familiar with writing programs where each line executes an individual instruction that has a visible effect. You will learn to reason about the behavior of existing code and you will be able to actually *see* the effects that result from changing or adding lines of code to an existing program.

We will start in this section by discussing concepts that are generally important for computational drawing: the canvas, coordinates, drawing settings, and screen ordering. After that, we’ll learn how to write code in Python that uses PennDraw to make our own drawings. PennDraw is the name of a group of related drawing tools available for you to use. Any time we need to draw to the computer’s screen in CIS 1100, we’ll use PennDraw.

You can access a full listing of PennDraw’s features on the [PennDraw Documentation](#) (LINK TKTKTK) page of the course website. This will be important for completing HW00. For now, we’ll step through some basic principles of drawing through programming.

## The Canvas & Coordinate Systems

### The Canvas

The *canvas* refers to the window of space on which PennDraw can do its drawing. It has a width and a height, both defined in pixels. We usually express the size of the canvas as *"width x height"*.

> If a canvas has dimension 800x400, then we say it has a width of 800 pixels and a height of 400 pixels, and it would look like this:  
> 
> ![Canvas](img/penndraw/canvas.png)

The dimension of the screen going from left-to-right (along the width) is called the *x dimension*. The up-and-down direction (along the height) is called the *y dimension*. This keeps us consistent with conventions in mathematics.

### Coordinate Systems

Although it’s important to keep in mind that the canvas has dimensions expressed in pixels, PennDraw allows us to define coordinates on the screen however we’d like. *By default, the coordinates of a canvas range from 0 to 1 in both the x dimension and the y dimension.*
Thus, the coordinate `(0, 0)` refers to the bottom left position of the canvas. Coordinate `(1, 1)` is found at the top right of the canvas. 

![Coordinate Grid](img/penndraw/coordinates.png)

For most of the work that we do in this course, we will keep the coordinate system set in the range from 0 to 1. You should get used to referring to screen positions in this way. Here are a few important things to understand about this coordinate system:
- The "origin" is the bottom left of the canvas.
- Larger values of x coordinates refer to positions further to the right.
- Larger values of y coordinates refer to positions higher up.
- Negative coordinates or coordinates with values greater than 1 are technically valid but refer to positions not visible on the canvas.

Sometimes it also makes sense to discuss the height and width of shapes instead of just the positions of points. We can refer to these dimensions in coordinate space as well. For example, a horizontal line spanning between the left side of the canvas and the center point of the canvas would have a *coordinate width* of `0.5` since its width would be exactly half of the screen. 

### Relating Coordinates to the Canvas (Example)

First, we can set up a canvas of square dimensions, setting the width and height to the same number of pixels. Then, we can draw a rectangle with its top left vertex at `(0.1, 0.8)` and its bottom right vertex at `(0.5, 0.6)`. The resulting image would look like this:

![Example Rectangle](img/penndraw/example.png)

In this example, the following are true:
- The rectangle has a *coordinate width* of `0.4`; that is, the distance in coordinate space between the right side of the rectangle at `0.5` and the left side of the rectangle at `0.1` is `0.4`.
- The rectangle has a *coordinate height* of `0.2`; that is, the distance in coordinate space between the top side of the rectangle at `0.8` and the bottom side of the rectangle at `0.6` is `0.2`. 

Can you work out what the center point of the rectangle would be? If the left side of the rectangle is at x-coordinate \\(0.1\\) and its full width is \\(0.4\\), then the x-center of the rectangle would be at \\(0.1 + \frac{0.4}{2} = 0.3\\). If the bottom side of the rectangle is at y-coordinate \\(0.6\\) and its full width is \\(0.2\\), then the y-center of the rectangle would be at \\(0.6 + \frac{0.2}{2} = 0.7\\). Take a look at the image above—can you see that the center of the rectangle is at the point \\(\(0.3, 0.7\)\\)?

## Pen Settings

PennDraw works in a model where the programmer (you!) gives a series of instructions, one by one, to a computer that uses an abstract "pen" to draw shapes on the screen. Some instructions that you write will directly result in a new shape appearing on the screen, and others are responsible for changing how those shapes will be drawn by changing the settings of the pen. This section will explain some basics behind instructions of this second kind. For all of these instructions that change the pen settings, all future shapes will be drawn with those most recent settings until new settings are made. 

### Pen Radius

Whenever we ask PennDraw to draw a point, line, or group of lines on the screen, these marks will appear with a certain thickness determined by the current setting for the radius of the pen. The following image is created using PennDraw with a default radius value of `0.002`, resulting in quite thin outputs:

![Thin line and thin point](img/penndraw/thin.png)

The above image has a line, which is quite readily visible, along with a single point drawn elsewhere on the screen. Can you spot the dot, or is that a speck of dust on your screen?
If we quadruple the thickness of the pen to `0.008`, the same commands to draw a line and a point result in the following:

![thick line and thick point](img/penndraw/thick.png)

Now that point is visible!

### Pen Color

It would be boring if the only images PennDraw could generate were in black and white. Fortunately, we can change the pen settings to draw in all sorts of colors. There are two primary ways to specify a color for drawing: by name, or by *RGB value*.

#### Colors by Name

PennDraw allows you to refer to a small set of colors by a direct name. Specifically, `PennDraw.BLUE` (read aloud like “PennDraw dot blue”) refers to this shade of blue:

And `PennDraw.MAGENTA` looks like this:

