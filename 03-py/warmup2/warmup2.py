# Talia Hsia - Coding Bat - Warmup2

#string times
def front3(str):
  if len(str) > 2:
    return str[0:3] *3
  return str *3

#front times
def front_times(str, n):
  if len(str) > 2:
    return str[0:3] * n
  return str *n

#string bits
def string_bits(str):
  final = ""
  for i in range(len(str)):
    if (i%2) == 0:
      final += str[i:i+1]
  return final

#string splosion
def string_splosion(str):
  final = ""
  for i in range(len(str)):
    final += str[0:i+1]
  return final

#last2
def last2(str):
  last = str[len(str)-2: len(str)]
  i = 0
  count = 0
  for i in range(len(str)-2):
    if (str[i: i+2] == last):
      count += 1
  return count

#array count9
def array_count9(nums):
  count = 0
  for i in range(len(nums)):
    if (nums[i] == 9):
      count += 1
  return count

#array front9
def array_front9(nums):
  i = 0
  j = 0
  if (len(nums) < 4):
    for i in range(len(nums)):
      if (nums[i] == 9):
        return True
  else:
    for j in range(3):
      if (nums[j] == 9):
        return True
  return False

#array123
def array123(nums):
  i = 0
  for i in range(len(nums)-2):
    if (nums[i] == 1):
      if(nums[i+1] == 2 and nums[i+2] == 3):
        return True
  return False

#string match
def string_match(a, b):
  count = 0
  i = 0
  if (len(a) < len(b)):
    length = len(a)
  else:
    length = len(b)
  for i in range(length-1):
    if(a[i] == b[i] and a[i+1] == b[i+1]):
      count += 1
  return count


