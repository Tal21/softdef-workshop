# Talia Hsia - Coding Bat - Warmup1

#sleep_in
def sleep_in(weekday, vacation):
  if weekday == False or vacation == True:
    return True
  return False
  
#monkey trouble
def monkey_trouble(a_smile, b_smile):
  if a_smile == True and not b_smile == True:
    return False
  elif b_smile == True and not a_smile == True:
    return False
  return True

#sum double
def sum_double(a, b):
  if a == b:
    return 4*a
  return a+b

#diff21
def diff21(n):
  if n > 21:
    return 2 * abs(n - 21)
  return abs (n - 21)

# parrot trouble
def parrot_trouble(talking, hour):
  if talking == True:
    if hour < 7 or hour >20:
      return True;
  return False

#makes 10
def makes10(a, b):
  if a == 10 or b == 10:
    return True
  if a + b == 10:
    return True
  return False

#near hundred
def near_hundred(n):
  if abs(100 - n) <= 10 or abs(200 - n) <= 10:
    return True
  return False

#pos neg
def pos_neg(a, b, negative):
  if negative == True:
    return a < 0 and b < 0
  elif a * b < 0:
    return True
  return False

#not string
def not_string(str):
  if str[0:3] == "not":
    return str
  return "not "+ str


#missing char
def missing_char(str, n):
  return str[0:n] + str[n+1: len(str)]

#front back
def front_back(str):
  if len(str) > 1:
    return str[len(str)-1:len(str)] + str[1:len(str)-1] + str[0:1] 
  return str

#front3
def front3(str):
  if len(str) > 2:
    return str[0:3] *3
  return str *3

