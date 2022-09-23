# Talia Hsia - Coding Bat - Warmup1

#sleep_in
def sleep_in(weekday, vacation):
  if weekday == False or vacation == True:
    return True
  return False

print(sleep_in(False, False))
print("ans: True")
print(sleep_in(True, False))
print("ans: False")
print(sleep_in(False, True))
print("ans: True")


#monkey trouble
def monkey_trouble(a_smile, b_smile):
  if a_smile == True and not b_smile == True:
    return False
  elif b_smile == True and not a_smile == True:
    return False
  return True

print(monkey_trouble(True, True))
print("ans: True")
print(monkey_trouble(False, False))
print("ans: True")
print(monkey_trouble(True, False))
print("ans: False")

#sum double
def sum_double(a, b):
  if a == b:
    return 4*a
  return a+b

print(sum_double(1, 2))
print("ans: 3")
print(sum_double(3, 2))
print("ans: 5")
print(sum_double(2, 2))
print("ans: 8")

#diff21
def diff21(n):
  if n > 21:
    return 2 * abs(n - 21)
  return abs (n - 21)

  print(diff21(19))
  print("ans: 2")
  print(diff21(10))
  print("ans: 11")
  print(diff21(21))
  print("ans: 0")

# parrot trouble
def parrot_trouble(talking, hour):
  if talking == True:
    if hour < 7 or hour >20:
      return True;
  return False

print(parrot_trouble(True, 6))
print("ans: True")
print(parrot_trouble(True, 7))
print("ans: False")
print(parrot_trouble(False, 6))
print("ans: False")

#makes 10
def makes10(a, b):
  if a == 10 or b == 10:
    return True
  if a + b == 10:
    return True
  return False

print(makes10(9, 10))
print("ans: True")
print(makes10(9, 9))
print("ans: False")
print(makes10(1, 9))
print("ans: True")

#near hundred
def near_hundred(n):
  if abs(100 - n) <= 10 or abs(200 - n) <= 10:
    return True
  return False

print(near_hundred(93))
print("ans: True")
print(near_hundred(90))
print("ans: True")
print(near_hundred(89))
print("ans: False")

#pos neg
def pos_neg(a, b, negative):
  if negative == True:
    return a < 0 and b < 0
  elif a * b < 0:
    return True
  return False

print(pos_neg(1, -1, False))
print("ans: True")
print(pos_neg(-1, 1, False))
print("ans: True")
print(pos_neg(-4, -5, True))
print("ans: True")

#not string
def not_string(str):
  if str[0:3] == "not":
    return str
  return "not "+ str

print(not_string('candy'))
print("ans: not candy")
print(not_string('x'))
print("ans: not x")
print(not_string('not bad'))
print("ans: not bad")

#missing char
def missing_char(str, n):
  return str[0:n] + str[n+1: len(str)]

print(missing_char('kitten', 1))
print("ans: ktten")
print(missing_char('kitten', 0))
print("ans: itten")
print(missing_char('kitten', 4))
print("ans: kittn")

#front back
def front_back(str):
  if len(str) > 1:
    return str[len(str)-1:len(str)] + str[1:len(str)-1] + str[0:1]
  return str

print(front_back('code'))
print("ans: eodc")
print(front_back('a'))
print("ans: a")
print(front_back('ab'))
print("ans: ba")

#front3
def front3(str):
  if len(str) > 2:
    return str[0:3] *3
  return str *3

print(front3('Java'))
print("ans: JavJavJav")
print(front3('Chocolate'))
print("ans: ChoChoCho")
print(front3('abc'))
print("ans: abcabcabc")
