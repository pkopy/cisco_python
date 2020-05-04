# flagReg = 0b00000100
# mask = 1
# if flagReg & mask:
#     print(flagReg)
# else:
#     flagReg | 1
#     print(flagReg)

var = 17
varRight = var >> 1
varLeft = var << 3
print(var, varLeft, varRight)

x = 15
y = 16

print(~x)