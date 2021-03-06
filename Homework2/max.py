def maximum(*args):
    if args:
        current_maximum_value = -float("inf")
        for arg in args:
            if arg > current_maximum_value:
                current_maximum_value = arg
        return current_maximum_value
    else:
        return "no numbers given"
print(maximum(1,2,3,4,5))