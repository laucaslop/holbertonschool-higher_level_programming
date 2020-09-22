#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    p = 0
    new_list = []
    while(p < list_length):
        div = 0
        try:
            div = my_list_1[p] / my_list_2[p]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
            return new_list
        finally:
            new_list.append(div)
        p += 1
    return new_list
