#!/usr/bin/env python
# -*- coding:utf-8 -*-

#       Copyright 2015 Francisco Carrillo (https://github.com/pacocp)
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.

#----------------------------------------------------------------------
# Francisco Carrillo Pérez <carrilloperezfrancisco@gmail.com>
#----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
#  This script is used to change the size of a bunch of images in Linux
#
#------------------------------------------------------------------------

from sys import argv
import subprocess
import os

images = []
first_answer = "Z"
while first_answer != "Y" and first_answer != "N":
    first_answer = input("Are all the images that you want to resize in the same path?(Y/N): ")

if first_answer == "Y":
    second_answer = input("Want you to resize all of them?(Y/N): ")

    if second_answer == "Y":
        # code here
        path = input(
            "Type the path of all your images(for example: /my_images/): ")
        size = input(
            "Please insert the size of the resize(for example: 217x185): ")

        for root, dirs, files in os.walk(path):
            for image in files:
                try:
                    subprocess.call(
                        ['convert', path + image, "-resize", size, path + image])
                except CantConvert:
                    print("Can't convert the image " + path + image)
    else:
        number_of_images = input("Type the number of images you want to resize: ")
        path = input(
            "Type the path of all your images(for example: /my_images/): ")

        size = input(
            "Please insert the size of the resize(for example: 217x185): ")

        for i in range(int(number_of_images)):
            image = input(
                "Please type the name of the image(include the extension please): ")
            images.append(image)
            for i in range(int(number_of_images)):
                try:
                    subprocess.call(
                        ['convert', path + images[i], "-resize", size, path + images[i]])
                except CantConvert:
                    print("Can't convert the image " + path + images[i])
else:
    for i in range(int(number_of_images)):
        path_and_image = input(
            "Please type the path and the image(for example: /my_images/image1.png): ")
        images.append(path_and_image)
    size = input(
        "Please insert the size of the resize(for example: 217x185): ")
    for i in range(int(number_of_images)):
        try:
            subprocess.call(['convert', images[i], "-resize", size, images[i]])
        except CantConvert:
            print("Can't convert the image " + images[i])

print("All have been converted!\n")
