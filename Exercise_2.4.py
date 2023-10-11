sweets = int(input("Please enter how many sweets there are in total: "))
pupils = int(input("Please enter number of pupils: "))
if sweets < pupils:
    print("You can't distribute the sweets fairly, because there are fewer sweets than there are students.")
elif sweets % pupils == 0 and sweets // pupils == 1:
    print(f"Each student gets exactly {sweets // pupils} sweet, no no remains.)")
elif sweets % pupils == 0:
    print(f"Each student gets exactly {sweets // pupils} sweets, no remains.)")
elif sweets // pupils == 1:
    print(f"Each pupil gets {sweets // pupils} sweet and has {sweets % pupils} left over ")
else:
    print(f"Each pupil gets {sweets // pupils} sweets and has {sweets % pupils} left over ")