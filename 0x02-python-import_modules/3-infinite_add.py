#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    my_addition  = 0
    for a in range(len(sys.argv) -1):
        my_addition += int(sys.argv[a + 1])
    print("{}".format(my_addition))