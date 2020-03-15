#!/usr/bin/env python3


def main():
    for i in range(1,11):
        for j in range(1,11):
            if(j==10):
                print(i*j)
            else:
                print(i*j, end=" ")

if __name__ == "__main__":
    main()
