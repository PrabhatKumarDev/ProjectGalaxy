# This module is used to extract colors from the image and those colors are stored in the color_list
# import colorgram

# rgb_colors=[]
# colors=colorgram.extract("Day 17\image.jpg",30)

# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
import turtle as turtle_module
import random
color_list=[(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]


turtle_module.colormode(255)
screen=turtle_module.Screen()
tim=turtle_module.Turtle()


tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.setheading(230)
tim.forward(320)
tim.setheading(0)
for j in range(10):
    for i in range(10):
        tim.dot(20,random.choice(color_list))
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

# This method helps to exit the turtle graphics screen on click
screen.exitonclick()