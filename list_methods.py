my_dict = {
    'name': 'Nick',
    'age':  31,
    'occupation': 'Dentist',
}

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

for key in my_dict:
    print(key, my_dict[key])


even_squares = [x ** 2 for x in range(1, 12) if x % 2 == 0]

print(even_squares)


cubes_by_four = [x ** 3 for x in range(1, 11) if x ** 3 % 4 == 0]

print(cubes_by_four)


cubes_by_four = [x ** 3 for x in range(1, 11) if x ** 3 % 4 == 0]

print(cubes_by_four)


# print backwords
my_list = range(1, 11)

backwards = my_list[::-1]

print(backwards)


to_one_hundred = range(101)

backwards_by_tens = to_one_hundred[::-10]

print(backwards_by_tens)


to_21 = range(1, 22)

odds = to_21[::2]

middle_third = to_21[7:14]

print(to_21)
print(odds)
print(middle_third)

my_list = range(16)

# functional
print(filter(lambda x: x % 3 == 0, my_list))

languages = ["HTML", "JavaScript", "Python", "Ruby"]

print(filter(lambda x: x == "Python", languages))


squares = [x ** 2 for x in range(1, 11)]

print(filter(lambda x: x > 29 and x < 71, squares))


threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]

print(threes_and_fives)


garbled_one = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled_one[::-2]

print(message)


garbled_two = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = filter(lambda x: x != 'X', garbled_two)

print(message)
