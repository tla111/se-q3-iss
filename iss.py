#!/usr/bin/env python

__author__ = 'Timothy La (tla111)'
'Received help from John W'

import requests
import turtle
import time


def iss_location():
    r = requests.get("http://api.open-notify.org/astros.json")
    print(r.json())

    coords = requests.get(
        'http://api.open-notify.org/iss-now.json').json()
    return coords


def main():
    iss_loc = iss_location()
    risetime = passover()
    turtle_location(iss_loc, risetime)


def passover():
    indy_location = requests.get(
        "http://api.open-notify.org/iss-pass.json?lat=40.2672&lon=86.1349").json()
    indy_risetime = indy_location["response"][0]["risetime"]
    return time.ctime(indy_risetime)


def turtle_location(loc, time):
    turtle_screen = turtle.Screen()
    turtle_screen.bgcolor("black")
    turtle_screen.setup(width=720, height=360, startx=None, starty=None)
    turtle_screen.setworldcoordinates(-180, -90, 180, 90)
    turtle_screen.bgpic("map.gif")
    turtle_screen.register_shape("iss.gif")
    # ISS Setup
    iss = turtle.Turtle()
    iss.shape("iss.gif")
    longitude = loc["iss_position"]["longitude"]
    latitude = loc["iss_position"]["latitude"]
    iss.penup()
    iss.goto(float(longitude), float(latitude))
    # Indiana Location
    indiana = turtle.Turtle()
    indiana.shape("circle")
    indiana.color('red')
    indiana.penup()
    indiana.goto(-86.1349, 40.2672)
    indiana.write(time)
    turtle.done()


if __name__ == '__main__':
    main()
