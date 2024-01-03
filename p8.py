def message(day):
    if day == "monday" or "tuesday" or "wednesday" or "thursday" or "friday" or "saturday":
        print(f"Happy {day}")
    elif day == "sunday":
        print(f"Relaxing {day}")
    else:
        print("invalid input")
day = input("Enter your fav day")
message(day)