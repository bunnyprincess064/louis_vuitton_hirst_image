# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)

import turtle as turtle_module
import random

tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.penup()
tim.hideturtle()

color_list = [
    (241, 221, 72), (33, 110, 171), (180, 45, 99), (12, 11, 35), (220, 154, 90), (35, 6, 22), (200, 141, 172),
    (49, 46, 117), (123, 170, 200), (176, 189, 28), (22, 159, 215), (233, 163, 196), (18, 128, 74),
    (163, 66, 38), (131, 192, 125), (196, 73, 133), (216, 90, 55), (149, 30, 66), (239, 164, 157),
    (11, 105, 59), (226, 210, 8), (70, 164, 117), (186, 187, 207), (96, 28, 6), (135, 38, 24), (160, 213, 167)
]

tim.setheading(225)
tim.speed('fastest')
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
