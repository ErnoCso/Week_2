def main():
    ans1 = ["Yes", "yes", "YES", "Y", "y", "Yeah", "YEAH", "yeah"]
    ans2 = ["No", "no", "NO", "N", "n", "Nope", "NOPE", "nope"]
    celsius = float(input(" Enter a temperature in Celsius: "))
    fahrenheit = float(celsius*1.8000)+32
    print(f"{celsius} \N{DEGREE SIGN}C is equivalent to {fahrenheit} \N{DEGREE SIGN}F ")
    def question():
        q = input(" Would you like to enter another number? Y/N ")
        if q in ans1:
            main()
        if q in ans2:
            print("Good bye!")
            exit()
        else:
            print("Invalid data, please try again ")
            question()
    question()
main()