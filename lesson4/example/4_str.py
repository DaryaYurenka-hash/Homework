# str.find()
# len("Hello") # функция

# # print("Hello pytllhon".find("ll")) # метод

# b = "Hello python".lower()
# a = "HeLLo".lower()

# c = input()
# c_low = c.lower()

# c = input().lower().find()

# print(b.find(a))

# a = "Hello"
# print(a.lower())
# print(a)


# print("123hfgвап!".isalnum())


# ---------------------------

# a = "0123456789"

# b = a[6]
# b = a[-1]
# b = a[-6]
# b = a[5:8]
# b = a[5:]
# b = a[:4]
# b = a[:-3]
# b = a[-5:-3]
# b = a[-3:-5]
# b = a[-3:-5:-1]
# b = a[::-1]
# b = a[:]
# b = a[::3]
# b = a[::-3]
# print(b)
# ----------------------------



# name = "Vasya"
# age = 22

# template = "Привет я {} мне {} года"

# print("Привет я %s мне %d года" % (name, age))
# print(template.format(name, age))
# print("Привет я {1} мне {0} года".format(age, name))
# print("Привет я {name1} мне {age1} года".format(name1=name, age1=age))

# print(f"Привет я {name} мне {age} года")
# print(f"Привет я {name:*^15} мне {age} года")
# print(f"Привет я {name:*<15} мне {age} года")
# print(f"Привет я {name:*>15} мне {age} года")

# b = 12_345_678
# b = 12345678

# print(f"Сумма: {b:_}")
# print(f"Сумма: {b:,}")
# print(f"Сумма - {12.12992876:.2f}")
# print(f"Сумма - {323123:010}") # дополнят нулями до 10 знаков
# print(f"Сумма - {323123:010d}") # дополнят нулями до 10 знаков
# print("{}:{:02}:{:02}".format(12, 1, 2)) # время
# print(f"{12}:{1:02}:{2:02}") # время

# ----------------------------

a = "Hello pytllhon !"
# b = a.find('l')
# print(b)
# print(a.find('l', b+1))
# print(a.find('l', 4, 6))

# print(a.isalnum())
# print("12212".isdigit())
# print("12384568789".count("8"))

# print(a.replace("ll", "L"))
# print(a.replace("ll", "L", 1))
# print(a.replace(" ", ""))

# b = a.split()
# print(b)
# print(b[0])

# a = "11, 55, 99"
# a = a.replace(" ", "")
# print(a)
# b = a.split(",") # -> список
# print(b)
# d1, d2, d3 = a.split(",")
# print(d1, d2, d3)

# c = list(map(int, b))
# print(c)

# a, b, c = map(int, b)
# print(a, b, c)

# a, b, c = map(int, input("3 числа через зпт").replace(" ", "").split(","))

# print(a, b, c)
# print(a+b+c)

# -----------------------------------------


# a = b"Hello"
# print(a)
# # a = a.decode()
# a = a.decode("utf-8")
# print(a)
# b = "Hello Пайтон"
# b = b.encode()
# # b = b.encode("utf-8")
# print(b)
# c = b.decode()
# print(c)


# print(ord("A"))
# print(chr(65))


# ------------------------------

# множественная замена подстрок
a = "Однажды, в студеную зимнюю пору"
b = a.maketrans({"а":"А","у":"У","и":"И"})
b = a.translate(b)
print(b)

# -----------------------------
max()
min()
sum()
len()