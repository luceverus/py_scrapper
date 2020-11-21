def sum(a, b):
    return int(a) + int(b)


def sub(a, b):
    return int(a) - int(b)


def div(a, b):
    return int(a) // int(b)


def reminder(a, b):
    return int(a) % int(b)


sum_result = sum(10, 3)
sub_result = sub(10, 3)
div_result = div(10, 3)
rem_result = reminder(10, 3)
results = [sum_result, sub_result, div_result, rem_result]

for i in results:
    print(i)
