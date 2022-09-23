# Talia Hsia - Coding Bat - Warmup2

#string times
def string_times(str, n):
  return str *n

print(string_times('Hi', 2))
print("ans: HiHi")
print(string_times('Hi', 3))
print("ans: HiHiHi")
print(string_times('Hi', 1))
print("ans: Hi")


#front times
def front_times(str, n):
  if len(str) > 2:
    return str[0:3] * n
  return str *n

print(front_times('Chocolate', 2))
print("ans: ChoCho")
print(front_times('Chocolate', 3))
print("ans: ChoChoCho")
print(front_times('Abc', 3))
print("ans: AbcAbcAbc")

#string bits
def string_bits(str):
  final = ""
  for i in range(len(str)):
    if (i%2) == 0:
      final += str[i:i+1]
  return final

print(string_bits('Hello'))
print("ans: Hlo")
print(string_bits('Hi'))
print("ans: H")
print(string_bits('Heeololeo'))
print("ans: Hello")

#string splosion
def string_splosion(str):
  final = ""
  for i in range(len(str)):
    final += str[0:i+1]
  return final

print(string_splosion('Code'))
print("ans: CCoCodCode")
print(string_splosion('abc'))
print("ans: aababc")
print(string_splosion('ab'))
print("ans: aab")

#last2
def last2(str):
  last = str[len(str)-2: len(str)]
  i = 0
  count = 0
  for i in range(len(str)-2):
    if (str[i: i+2] == last):
      count += 1
  return count


print(last2('hixxhi'))
print("ans: 1")
print(last2('xaxxaxaxx'))
print("ans: 1")
print(last2('axxxaaxx'))
print("ans: 2")

#array count9
def array_count9(nums):
  count = 0
  for i in range(len(nums)):
    if (nums[i] == 9):
      count += 1
  return count

print(array_count9([1, 2, 9]))
print("ans: 1")
print(array_count9([1, 9, 9]))
print("ans: 2")
print(array_count9([1, 9, 9, 3, 9]))
print("ans: 3")

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

print(array_front9([1, 2, 9, 3, 4]))
print("ans: True")
print(array_front9([1, 2, 3, 4, 9]))
print("ans: False")
print(array_front9([1, 2, 3, 4, 5]))
print("ans: False")

#array123
def array123(nums):
  i = 0
  for i in range(len(nums)-2):
    if (nums[i] == 1):
      if(nums[i+1] == 2 and nums[i+2] == 3):
        return True
  return False

print(array123([1, 1, 2, 3, 1]))
print("ans: True")
print(array123([1, 1, 2, 4, 1]))
print("ans: False")
print(array123([1, 1, 2, 1, 2, 3]))
print("ans: True")

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

print(string_match('xxcaazz', 'xxbaaz'))
print("ans: 3")
print(string_match('abc', 'abc'))
print("ans: 2")
print(string_match('abc', 'axc'))
print("ans: 0")
