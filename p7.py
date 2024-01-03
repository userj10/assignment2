def square_pattern(size):
    for i in range(size):
        for j in range(size):
            print("* ", end=" ")
        print()


try:
    size = int(input("Enter size of square"))
    if size<=0:
        raise ValueError("invalid size")
except ValueError as e:
    print(f"Error {e}")
else:
    square_pattern(size)

