import penndraw as pd

pd.set_canvas_size(500, 500)

# draw a blue background
pd.clear(pd.BLUE)

# draw a green field
pd.set_pen_color(0, 170, 0)
pd.filled_rectangle(0.5, 0.25, 0.5, 0.25)

# change the pen color to a shade of yellow
pd.set_pen_color(200, 170, 0)

# draw a filled triangle (roof)
pd.filled_polygon(0.255, 0.70, 0.745, 0.70, 0.49, 0.90)

# draw the house
pd.filled_rectangle(0.5, 0.52, 0.24, 0.18)

pd.set_pen_radius(0.005)  # thicken the pen for outline drawing
pd.set_pen_color(pd.BLACK)  # make the pen black

# draw the roof, house, and door outlines with non-filled rectangles
pd.polygon(0.255, 0.70, 0.745, 0.70, 0.49, 0.90)  # roof
pd.rectangle(0.5, 0.52, 0.24, 0.18)  # house
pd.rectangle(0.596, 0.44, 0.08, 0.1)  # door

pd.point(0.54, 0.44)  # draw a doorknob
