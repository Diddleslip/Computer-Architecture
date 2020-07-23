#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

cpu.load("ls8/examples/call.ls8")
cpu.run()


numb = "00010001"
print("this is numb ",int(numb, 2))