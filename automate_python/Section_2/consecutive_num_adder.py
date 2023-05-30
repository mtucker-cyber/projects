total = 0

print('Input bottom value of range:')
bottomvalue = input()

print('Input top value of range:')
topvalue = input()

bv = int(bottomvalue)
tv = int(topvalue) + 1
for num in range(bv, tv):
    total = total + num
print(total)