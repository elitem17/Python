#!/usr/bin/env python
import re

greedyHaRegex = re.compile(r"(Ha){3,5}")
mo1 = greedyHaRegex.search("HaHaHaHaHa")
print(mo1.group())

nonGreedyHaRegex = re.compile(r"(Ha){3,5}?")
mo2 = nonGreedyHaRegex.search("HaHaHaHaHa")
print(mo2.group())
