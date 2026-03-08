# type_explorer.py
# Uzdevums 1: Tipu pētnieks
# Mērķis: iepazīt Python datu tipus, truthy/falsy uzvedību un tipu konversijas.
print("=== 1) PAMATA DATU TIPI (2 mainīgie katram tipam) ===")

name = "Raimonds"
city = "Riga"
# INT (vesels skaitlis)
age = 25
year = 2000
# FLOAT (decimālskaitlis)
height = 1.87
weight = 72.7
# BOOL (True/False)
is_student = True
is_adult = True
# NONE (nav vērtības)
data = None
result = None
print("\n=== 2) KATRAS VĒRTĪBAS TIPS, IZMANTOJOT type() ===")

print(type(name))  # <class 'str'>
print(type(city))  # <class 'str'>
print(type(age))   # <class 'int'>
print(type(year))  # <class 'int'>
print(type(height))  # <class 'float'>
print(type(weight))  # <class 'float'>
print(type(is_student))  # <class 'bool'>
print(type(is_adult))  # <class 'bool'>
print(type(data))  # <class 'NoneType'>
print(type(result))  # <class 'NoneType'>
print("name:", name, type(name))
print("city:", city, type(city))
print("age:", age, type(age))
print("year:", year, type(year))
print("height:", height, type(height))
print("weight:", weight, type(weight))
print("is_student:", is_student, type(is_student))
print("is_adult:", is_adult, type(is_adult))
print("data:", data, type(data))
print("result:", result, type(result))
print("\n=== 3) Truthy / Falsy piemēri ===")

# 0 is falsy
if 0:
    print("0 is True")
else:
    print("0 is False")
# Empty string is falsy
if "":
    print("Empty string is True")
else:
    print("Empty string is False")
# None is falsy
if None:
    print("None is True")
else:
    print("None is False")
# Non-empty string is truthy
if "Labdien!":
    print("Non-empty string is True")
else:
    print("String is False")
print("\n=== 4) EXPLICIT KONVERSIJAS + ROBEŽGADĪJUMI ===")

# string -> int (izdodas)
s = "25"
n = int(s)
print('int("25") ->', n, type(n))
# int -> float (izdodas)
i = 10
f = float(i)
print("float(10) ->", f, type(f))
# float -> int (izdodas, bet NOGRIEŽ decimāldaļu, nenoapaļo)
x = 9.99
y = int(x)
print("int(9.99) ->", y, type(y), "(nogriež aiz komata)")
# Robežgadījums A: string nav skaitlis -> int() neizdodas (ValueError)
bad = "abc"
try:
    int_bad = int(bad)
    print("int('abc') ->", int_bad)
except ValueError:
    print("int('abc') -> neizdevās (ValueError), jo 'abc' nav skaitlis")
# Robežgadījums B: string ir decimālskaitlis -> int() neizdodas
# int("3.14") nestrādā, jo tas nav vesels skaitlis teksta formā.
bad2 = "3.14"
try:
    int_bad2 = int(bad2)
    print("int('3.14') ->", int_bad2)
except ValueError:
    print("int('3.14') -> neizdevās (ValueError). Pareizi būtu float('3.14')")
# Papildpiemērs: pareiza ķēdīte "3.14" -> float -> int
good = "3.14"
as_float = float(good)
as_int = int(as_float)
print("float('3.14') ->", as_float, type(as_float))
print("int(float('3.14')) ->", as_int, type(as_int), "(vispirms float, tad int)")

# Virkņu savienošana — Python neveic automātisku tipu konversiju

print("7" + "2")  # "72" (virkņu savienošana)

# print("7" + 2)  # TypeError! Python nevar savienot str ar int

print(int("7") + 2)  # 9 (explicit konversija)


# Robežgadījumi

# print(int("xyz"))  # ValueError — tekstu nevar pārvērst par skaitli

print(float("6.28"))  # 6.28


# Truthy / falsy

print(bool(""))   # False (tukša virkne)

print(bool("Python"))  # True (netukša virkne)

print(bool(" "))  # True (atstarpe arī ir simbols)

print(bool(0))    # False

print(bool(15))   # True

print(bool({}))   # False (tukšs dictionary)

print(bool(None)) # False

print(True + False)  # 1 (True=1, False=0)


# Jauktā aritmētika

print(True * 5)   # 5 (True ir 1)

print(False + 8)  # 8 (False ir 0)

print(20 / True)  # 20.0


# Skaitļu pārveidošana

print(int(7.91))  # 7 (nogriež decimāldaļu)

# print(int("7.91"))  # ValueError — int() nepieņem decimālskaitli tekstā

print(int(float("7.91")))  # 7

print(float("2e3"))  # 2000.0

# Explicit konversijas

print(int(True))       # bool -> int
print(str(45) + str(10))  # int -> str
print(bool("Hello"))   # str -> bool

# Robežgadījums

print(bool("False"))   # True, jo virkne nav tukša