# Talia Hsia - Coding Bat - List 1

#first last
def first_last6(nums):
  return nums[0] == 6 or nums[len(nums)-1] == 6

print(first_last6([1, 2, 3]))
print(first_last6([13, 6, 1, 2, 3]))


#same first last
def same_first_last(nums):
  if (len(nums) > 0):
    return nums[0] == nums[len(nums)-1]
  return False

print(same_first_last([1, 2, 3]) )
print(same_first_last([1, 2, 3, 1]) )
print(same_first_last([1, 2, 1]))

#make pi
def make_pi():
  return [3, 1, 4]

print(make_pi())


#common end
def common_end(a, b):
  return a[0] == b[0] or a[len(a)-1] == b[len(b)-1]

print(common_end([1, 2, 3], [7,3]))
print("ans: True")
print(common_end([1, 2, 3], [7,3, 2]))
print("ans: False")
print(common_end([1, 2, 3], [1,3]))
print("ans: True")

# sum3
def sum3(nums):
  counter = 0
  for i in range(len(nums)):
    counter += nums[i]
  return counter

print(sum3([1, 2, 3]))
print("ans: 6")
print(sum3([5, 11, 2]))
print("ans: 18")
print(sum3([7, 0, 0]))
print("ans: 7")


#rotate left3
def rotate_left3(nums):
  first = nums[0]
  second = nums[1]
  third = nums[2]
  return [second, third, first]

print(rotate_left3([1, 2, 3]))
print("ans: [2,3,1]")
print(rotate_left3([5, 11, 9]))
print("ans: [11,9,5]")

#reverse3
def reverse3(nums):
  new = []
  for i in range(len(nums)):
    new.append(nums[len(nums)-1-i]);
  return new

print(reverse3([1, 2, 3]))
print("ans: [3,2,1]")
print(reverse3([5, 11, 9]))
print("ans: [9,11,5]")
print(reverse3([7, 0, 0]))
print("ans: [0,0,7]")

#maxend3
def max_end3(nums):
  if(nums[0] > nums[len(nums)-1]):
    high = nums[0]
  else:
    high = nums[len(nums)-1]
  for i in range(len(nums)):
    nums[i] = high
  return nums

print(max_end3([1,2,3]))
print("ans: [3,3,3]")
print(max_end3([11,5,9]))
print("ans: [11,11,11]")
print(max_end3([2,11,3]))
print("ans: [3,3,3]")

# sum2
def max_end3(nums):
  if(nums[0] > nums[len(nums)-1]):
    high = nums[0]
  else:
    high = nums[len(nums)-1]
  for i in range(len(nums)):
    nums[i] = high
  return nums

print(sum2([1,2,3]))
print("ans: 3")
print(sum2([1,1]))
print("ans: 2")
print(sum2([1,1,1, 1]))
print("ans: 2")

#middle way
def middle_way(a, b):
  return [a[1], b[1]]

print(middle_way([1, 2, 3], [4, 5, 6]))
print("ans: [2,5]")
print(middle_way([7, 7, 7], [3, 8, 0]))
print("ans: [7,8]")
print(middle_way([5, 2, 9], [1, 4, 5]))
print("ans: [2,4]")

#make ends
def make_ends(nums):
  return [nums[0], nums[len(nums)-1]]

print(make_ends([1, 2, 3]))
print("ans: [1,3]")
print(make_ends([1, 2, 3, 4]))
print("ans: [1,4]")
print(make_ends([7, 4, 6, 2]))
print("ans: [7,2]")


#has23
def has23(nums):
  for i in range(len(nums)):
    if(nums[i] == 2 or nums[i] == 3):
      return True
  return False

print(has23([2, 5]))
print("ans: True")
print(has23([4, 3]))
print("ans: True")
print(has23([4, 5]))
print("ans: False")
