## -*- coding: utf-8 -*-
##
## interface.py
##
## Author:   Toke Høiland-Jørgensen (toke@toke.dk)
## Date:     26 April 2012
## Copyright (c) 2012, Toke Høiland-Jørgensen
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

from console import Console

class Interface(Console):

    def __init__(self):
        Console.__init__(self)
        self.prompt = ">> "
        self.intro = "Welcome to the CBR system. Type 'help' for a list of commands."

    def default(self, line):
        print "Invalid command. Type 'help' for a list of commands."


if __name__ == "__main__":
    interface = Interface()
    interface.cmdloop()
