#!/usr/bin/env python

__author__ = 'Timothy La (tla111)'

import requests
import turtle


def main():

    r = requests.get("http://api.open-notify.org/astros.json")
    print(r.json())

    coords = requests.get(
        'http://api.open-notify.org/iss-now.json').json()
    print(coords)
    # return coords

    turtle_screen = turtle.getscreen()
    turtle_screen.bgcolor("black")
    # turtle_screen.setworldcoordinates(-51.5177, 114.3406)
    # turtle_screen.setworldcoordinates(-1, -1, 20, 20)
    # t = turtle.Turtle()
    # for i in range(3):
    #     for colors in ["red", "magenta", "blue", "cyan", "yellow", "white"]:
    #         t.pen(pencolor=colors, pensize=2, speed=9)
    #         t.circle(90)
    #         t.left(10)
    return turtle_screen


if __name__ == '__main__':
    main()
