#!/usr/bin/env python3


def main():
    for i in range(1,11):
        tripled = triple(i)
        squared = square(i)
        if squared > tripled:
            break
        print(f"triple({i})=={tripled} square({i})=={squared}")

def triple(value):
    return value*3
def square(value):
    return value**2

if __name__ == "__main__":
    main()
