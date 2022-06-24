#*********** Find out if number on array is divisible by 10
def divisible_by_ten (nums) :
    counter = 0
    for num in nums:
        if num % 10 == 0 :
            counter += 1
    return counter

print(divisible_by_ten([20, 25, 30, 35, 40]))
#returns 3



#*********** GREETINGS - Insert Hello before each name and spit out new array
def add_greetings(names) :
    new_arr = []
    for name in names:
        new_arr.append('Hello, ' + name)
    return new_arr

print(add_greetings(["Owen", "Max", "Sophie"]))
#returns ['Hello, Owen', 'Hello, Max', 'Hello, Sophie']



#*********** Delete Starting Even Numbers
#remove elements from the front of lst until the front of the list is not even.
def delete_starting_evens(lst):
    while( len(lst) > 0 and lst[0] %2 ==0 ):
        lst = lst[1:]
    return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
#returns [11, 12, 15]



#*********** Collect Odd Indices - give us the values from a list at every odd index
# range(1, len(lst), 2) -- returns a list of numbers starting at 1, ending at the length of len, and incrementing by 2.
def odd_indices(lst):
    new_arr = []
    for index in range(1, len(lst), 2):
        new_arr.append(lst[index])
    return new_arr
print(odd_indices([4, 3, 7, 10, 11, -2]))
#returns [3, 10, -2]



#*********** Exponents - raise a list of numbers to the power of a list of other numbers
def exponents(bases, powers):
    new_arr = []
    for num in bases:
        for power_num in powers:
            new_arr.append(num ** power_num)
    return new_arr
print(exponents([2, 3, 4], [1, 2, 3]))



#*********** Return larger sum list
def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for num1 in lst1:
        sum1 += num1
    for num2 in lst2:
        sum1 += num2
    
    if sum1 >= sum2:
        return lst1
    else:
        return lst2

#OR
def larger_sum(lst1, lst2):
    sum1 = sum(lst1)
    sum2 = sum(lst2)
    
    if sum1 >= sum2:
        return lst1
    else:
        return lst2
print(larger_sum([1, 9, 5], [2, 3, 7]))
#returns [1,9,5]



#*********** Break sum if list sum is greater than 9000
def over_nine_thousand(lst):
    sum = 0
    for i in lst:
        sum += i 
        if sum >= 9000:
            break
    return sum
print(over_nine_thousand([8000, 900, 120, 5000]))
#returns 9020



#*********** Max Sum - find the maximum number in a list of numbers
def max_num (nums):
    maximum = nums[0]
    for num in nums:
        #*maximum = nums[0]
        if num > maximum:
            maximum = num
    return maximum

print(max_num([50, -10, 0, 75, 20]))
#returns 75



#***********  find the indices in two equally sized lists where the numbers match.
def same_values(lst1 , lst2):
    new_arr = []
    for i in lst1:
        for j in lst2:
            if i == j:
                new_arr.append(i)



#***********  Same Values
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
#returns [0, 2, 3]
#a loop that iterates using the range of the len of our list. This generates the indices we need to iterate through. 



#***********  Reversed List
def reversed_list(lst1, lst2):
    for index in range(len(lst1)):
        if lst1[index] != lst2[len(lst2) - 1 - index]:
            return False
    return True
