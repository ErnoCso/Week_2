#!/usr/bin/env python 3

# Task 1

# Last week you wrote a program that printed out a cheery greeting including your
# name. Take a copy of it, and modify it so that the user enters their name at the
# keyboard, and then receives a greeting. For example:
# Hello, what is your name? Mr Apricot
# Hello, Mr Apricot. Good to meet you!


if __name__ == "__main__":
    name = input("Hello, what is your name? ")
    if name != "":
        print(f"Hello {name}! Good to meet you!")
    else:
        print("Hello you have not entered any names!")


# Output:
# Hello, what is your name? Joey
# Hello Joey! Good to meet you!