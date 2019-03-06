def is_even():
    num = int(input("Please enter a number: "))
    if num %2 == 0:
        return True
    else:
        return False


is_even()


def is_lunchtime(hour, is_am):
    if (hour== 11 and is_am) or (hour == 12 and not is_am):
        return True
    else:
        return False


is_lunchtime(12, False)
is_lunchtime(11, True)
is_lunchtime(11, False)
is_lunchtime(12, True)


def is_leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False


is_leap_year(2004)
is_leap_year(2013)
is_leap_year(2016)


def name_and_age(name, age):
    if age > 0:
        return "%s is %d years old." % (name, age)
    else:
        return " Error: Invalid age"


name_and_age("Peter", 30)
name_and_age("Jack", 54)
name_and_age("Ketan", 0)
name_and_age("Mrunal", -1)

def print_digits(number):
    if 0 < number > 100:
        print("Error: Input is not a two-digit number.")
    else:
        tenth_digit = number / 10
        ones_digit = number % 10
        print("The tens digit is %d and the ones digit is %d." % (tenth_digit, ones_digit))


print_digits(19)
print_digits(-1)
print_digits(0)
print_digits(105)
print_digits(40)


def pig_latin(word):
    if word[0] == 'a' and 'e' and 'i' and 'o' and 'u':
        word = word + 'way'
        print(word)
    else:
        word = word[1:] + 'ay'
        print(word)


pig_latin("pig")
pig_latin("apple")




