def string_reversed(str):
    new_str = ""
    for n in str[::-1]:
        new_str += n
    print(new_str)

string_reversed("why")