"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""


def is_on_list(daysList=[], date=""):
    return date in daysList


def get_x(daysList=[], index=0):
    return daysList[index]


def add_x(daysList=[], newDate=""):
    daysList.append(newDate)


def remove_x(daysList=[], tobeDeleted=""):
    daysList.remove(tobeDeleted)

# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #


days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)


# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #
