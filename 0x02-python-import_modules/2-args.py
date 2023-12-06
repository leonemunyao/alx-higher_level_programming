#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    my_count = len(sys.argv) - 1
    if my_count == 0:
        print("0 arguments.")
    elif my_count == 1:
        print("1 argument:")
    else:
        print("{} arguements:".format(my_count))
    for j in range(my_count):
        print("{}: {}".format(j + 1, sys.argv[j + 1]))