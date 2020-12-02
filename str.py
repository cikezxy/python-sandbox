# 格式化，C sprintf形式
name = "james"
number = 1035.569
print('Hey %(name)s, there is a %(num)+5.2f number!' % {"name": name, "num": number})
print('Hey %s, there is a %+5.2f number!' % (name, number))
# Hey james, there is a +1035.57 number!

# 格式化，format方法
print("Hey {}, there is a {} number!".format(name, number))
print("Hey {0}, there is a {1} number!".format(name, number))
print("Hey {name}, there is a {number} number!".format(**{"name": name, "number": number}))

print("Hey {0}, there is a {1:0>8,.2f} number!".format(name, number))
print("Hey {name}, there is a {number:0>8,.2f} number!".format(**{"name": name, "number": number}))
# Hey james, there is a 1,035.57 number!

# 格式化，f-string
print(f'Hey {name}, there is a {number:0>8,.2f} number!')

hw = "hello, world!"
assert "Hello, world!" == hw.capitalize()
assert "Hello, World!" == hw.title()
assert "hello, world!" == hw.lower()
assert "HELLO, WORLD!" == hw.upper()
assert "HELLO, WORLD!" == hw.swapcase()
print(hw.title())

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(mytable)
print(txt.translate(mytable))
# G i Joe!

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

txt = "apple, banana, cherry"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)
print(x)

str1 = "this is string example....wow!!!"
print(str1.rjust(50, 'a'))