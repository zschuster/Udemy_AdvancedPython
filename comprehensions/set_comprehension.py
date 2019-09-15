
x = {i * 2 for i in range(4) if i % 2 == 0}
print(x)

y = {i for i in [1, 2, 3, 4] if i % 2 == 0}
print(y)

# use tuple as variables within nested for loop
z = {(a, b) for a in range(2) for b in range(3)}
print(z)