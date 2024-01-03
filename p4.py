str = "Hello 123 world 456!"
list = []
for n in str:
    if n.isnumeric():
        list.append(n)

print(list)
