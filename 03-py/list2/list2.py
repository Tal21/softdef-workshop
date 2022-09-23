# Talia Hsia - Coding Bat - List2

#count evens
def count_evens(nums):
  count = 0
  for i in range(len(nums)):
    if(nums[i]%2 == 0):
      count += 1
  return count

print(count_evens([2, 1, 2, 3, 4]))
print("ans: 3")
print(count_evens([2, 2, 0]))
print("ans: 3")
print(count_evens([1, 3, 5]))
print("ans: 0")

#big diff
def big_diff(nums):
  maxi = 0
  mini = nums[0]
  for i in range(len(nums)):
    maxi = max(maxi, nums[i])
    mini = min(mini, nums[i])
  return maxi - mini

print(big_diff([10, 3, 5, 6]))
print("ans: 7")
print(big_diff([7, 2, 10, 9]))
print("ans: 8")
print(big_diff([2, 10, 7, 2]))
print("ans: 8")

# centered average
def centered_average(nums):
  maxi = nums[0]
  mini = nums[0]
  sums = 0
  for i in range(len(nums)):
    if(i == 0):
      nums[i]
    elif(maxi <= nums[i]):
      sums += maxi
      maxi = nums[i]
    elif(mini >= nums[i]):
      sums += mini
      mini = nums[i]
    else:
      sums += nums[i]
  sums -= nums[0]
  return sums/(len(nums)-2)
  
print(centered_average([1, 2, 3, 4, 100]))
print("ans: 3")
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print("ans: 5")
print(centered_average([-10, -4, -2, -4, -2, 0]))
print("ans: 3")


# sum13
def sum13(nums):
  sum = 0
  if(len(nums) == 0):
    return sum
  for i in range(len(nums)):
    if(nums[i] != 13):
      sum+= nums[i]
    else:
      if(i < len(nums)-1):
        nums[i+1] = 0
  return sum

print(sum13([1, 2, 2, 1]))
print("ans: 6")
print(sum13([1, 1]))
print("ans: 2")
print(sum13([1, 2, 2, 1, 13]))
print("ans: 6")

#sum67
def sum67(nums):
  count = True
  sums = 0
  for i in range(len(nums)):
    if (count == True):
      if(nums[i] == 6):
        count = False
      else:
        sums += nums[i]
    else:
      if(nums[i] == 7):
        count = True
  return sums

print(sum67([1, 2, 2]))
print("ans: 5")
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print("ans: 5")
print(sum67([1, 1, 6, 7, 2]))
print("ans: 4")

#has22
def has22(nums):
  for i in range(len(nums)-1):
    if(nums[i] == 2 and nums[i+1] == 2):
      return True
  return False

print(has22([1, 2, 2]))
print("ans: True")
print(has22([1, 2, 1, 2]))
print("ans: False")
print(has22([2, 1, 2]))
print("ans: False")
