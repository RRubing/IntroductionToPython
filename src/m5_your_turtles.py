"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Rubing Wu.
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

Teemo = rg.SimpleTurtle('turtle')
Teemo.pen = rg.Pen('Orange', 5)
Teemo.speed = 1

Yasuo = rg.SimpleTurtle('turtle')
Yasuo.pen = rg.Pen('blue', 5)
Yasuo.speed = 2

size = 150

for k in range (10):

    Teemo.draw_square(size)
    Yasuo.draw_square(size)

    Teemo.pen_up()
    Teemo.left(10)  # degree angle
    Teemo.forward(45)
    Teemo.right(45)  # degree angle
    Teemo.pen_down()

    Yasuo.pen_up()
    Yasuo.left(10)
    Yasuo.forward(45)
    Yasuo.right(45)
    Yasuo.pen_down()

    size = size - 12

window.close_on_mouse_click()