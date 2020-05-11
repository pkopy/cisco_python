from sys import path

path.append('../packages/extrapack.zip')

# import extra.iota
#
# print(extra.iota.FunI())

from extra.iota import FunI

print(FunI())