x = int(input())

i = 1

while x > 0:
    x -= i
    i += 1

j = i + x - 1

if i % 2:
    print(f'{j}/{i - j}')
else:
    print(f'{i - j}/{j}')