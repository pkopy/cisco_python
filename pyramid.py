blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#
x = blocks
count = 0
while True:
    count += 1
    x -= count
    print(x)
    if x < 0:
        count -= 1
        break

print("The height of the pyramid:", count)