day_of_the_week = input("What day of the week is it today? ").lower
print(day_of_the_week == "Monday")

if day_of_the_week == "monday":
    print("Have a great start of the week")
elif day_of_the_week == "sunday":
    print("It was a great week")
else:
    print("Its a great week")

print("This is always run")