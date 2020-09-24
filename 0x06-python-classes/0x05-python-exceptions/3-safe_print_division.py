#!/usr/bin/python3
def safe_print_division(a, b):
    ab = None
    try:
        ab = a/b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(ab))
        return ab
