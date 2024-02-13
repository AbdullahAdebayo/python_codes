# def my_name(name,age,school):
#     print(name ,"is", age , "and he attends" , school)
# my_name("Abdullah",21,"Obafemi Awolowo University")
#   A leap year calculation


year = int(input("Enter year of test: "))

if year %  4 ==  0:
    if year %  100 !=  0 or year %  400 ==  0:
        print("The calendar year", year, "is a leap year.")
    else:
        print("The calendar year", year, "is not a leap year.")
else:
    print("The calendar year", year, "is not a leap year.")

#OR
def is_leap(year):
    if year %  4 ==  0:
        if year %  100 ==  0:
            if year %  400 ==  0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year =  int(input("Enter a year: "))
if is_leap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")