import sys

# pārbauda vai ir ievadīts N
if len(sys.argv) < 2:
    print("Lietošana: python fizzbuzz.py N")
    sys.exit()

# mēģina pārvērst argumentu par skaitli
try:
    N = int(sys.argv[1])
except ValueError:
    print("Kļūda: N jābūt skaitlim!")
    sys.exit()

# cikls no 1 līdz N
for i in range(1, N + 1):

    # vispirms pārbauda abus
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=", ")

    # tad katru atsevišķi
    elif i % 3 == 0:
        print("Fizz", end=", ")

    elif i % 5 == 0:
        print("Buzz", end=", ")

    # bonuss – ja dalās ar 7
    elif i % 7 == 0:
        print("Jazz", end=", ")

    else:
        print(i, end=", ")