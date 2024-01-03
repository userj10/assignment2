import datetime as dt

def greeting(name):
    now = dt.datetime.now()
    hour = now.hour
    if 5<=hour<12:
        print(f"Hello, {name}\nGood morning")
    elif 12<=hour<17:
        print(f"Hello, {name}\nGood afternoon")
    elif 17<=hour<=21:
        print(f"Hello, {name}\nGood evening")
    else:
        print(f"Hello, {name}\nIt's late Good Night")

greeting("Purva")