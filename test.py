#!/usr/bin/env python


from __future__ import print_function


from cmd import Cmd
import gnureadline  # noqa


class Zoo(Cmd):

    def __init__(self, animals):
        Cmd.__init__(self)

        self.animals = animals

    def do_add(self, animal):
        print("Animal {0:s} added".format(animal))

    def completedefault(self, text, line, begidx, endidx):
        tokens = line.split()
        if tokens[0].strip() == "add":
            return self.animal_matches(text)
        return []

    def animal_matches(self, text):
        matches = []
        n = len(text)
        for word in self.animals:
            if word[:n] == text:
                matches.append(word)
        return matches


animals = ["Bear", "Cat", "Cheetah", "Lion", "Zebra"]
zoo = Zoo(animals)
zoo.cmdloop()
