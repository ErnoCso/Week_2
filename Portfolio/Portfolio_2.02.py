#!/usr/bin/env python 3

# Task 2

# Write a program that prompts a user to enter a temperature in Celsius, and then
# displays the corresponding temperature in Fahrenheit, like so:
# Enter a temperature in Celsius: 32.5
# 32.5C is equivalent to 90.5F.

if __name__ == "__main__":

    def main():
        ans1 = ["Yes", "yes", "YES", "Y", "y", "Yeah", "YEAH", "yeah"]
        ans2 = ["No", "no", "NO", "N", "n", "Nope", "NOPE", "nope"]
        celsius = float(input("Enter a temperature in Celsius: "))
        fahrenheit = float(celsius * 1.8000) + 32
        print(f"{celsius} \N{DEGREE SIGN}C is equivalent to {round(fahrenheit,2)} \N{DEGREE SIGN}F ")

        def question():
            q = input("Would you like to enter another number? Y/N ")
            if q in ans1:
                main()
            if q in ans2:
                print("Goodbye!")
                exit()
            else:
                print("Invalid data, please try again ")
                question()

        question()


    main()


# Output:
#  Enter a temperature in Celsius: 40
# 40.0 °C is equivalent to 104.0 °F
# Would you like to enter another number? Y/N y
# Enter a temperature in Celsius: 40.2
# 40.2 °C is equivalent to 104.36 °F
# Would you like to enter another number? Y/N n
# Goodbye!

