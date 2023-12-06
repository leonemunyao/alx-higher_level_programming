#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    my_name = dir(hidden_4)
    for my_name in my_names:
        if my_name[:2] != "__":
            print(my_name)