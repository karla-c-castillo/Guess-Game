# Karla Carrillo Castillo
# Date Nov 19
# class Info Sys
# Program

# Create empty list to store nums
List = []

# intialize a max size of n = 3, no more entries allowed
n = 3;
for i in range(0,n): # loops an iterator < 3 
  # Prompt the user for a number
  print("Please enter user input num #",i+1) 
  user_input = input("Enter num: ") # recv and store user input
  user_input = int(user_input) # type cast to int n

  if(user_input > 0): # Must be a positive number
    List.append(user_input) # append to tail of list for each num > 0
  else: # Must be a negative number
    print("Try a whole number greater than 0. Non whole integers not accepted.")
    print("Please enter user input num #",i+1) 
    user_input = input("Enter num: ") # recv user str input
    user_input = int(user_input) # type cast to int, user input "n # value str" must turn into an integer with cast to int

    if(user_input > 0):
      List.append(user_input)
    else:
      print("\n")
      raise Exception("Detected multiple negative whole number value entries. Restart user application.")
      exit(1)

# Check each number in the list to see if they have duplicates
# List[n,n+1,...,n-1]
# list[0] index 0 element 0
# list[1] index 1 element 1
# list[2] index 2 element 2
# Store duplicates. count checks for duplicates of the indexed values
num_duplicates1 = List.count(List[0]) 
num_duplicates2 = List.count(List[1])
num_duplicates3 = List.count(List[2])

# If there are no duplicates in all 3 element indexes do
if(num_duplicates1 < 2 and num_duplicates2 < 2 and num_duplicates3 < 2):
  print("The smallest number is ",min(List),".")
  print("There are zero equal numbers.")
  print("\n")

# Else Must be dup values in the list
for i in (0,n):
  if(num_duplicates1 > 1):
    print("The smallest number is ",min(List))
    print("There are",str(num_duplicates1),"equal numbers.")
    print("\n")
    break
  if(num_duplicates2 > 1):
    print("The smallest number is ",min(List))
    print("There are",str(num_duplicates2),"equal numbers.")
    print("\n")
    break
  if(num_duplicates3 > 1):
    print("The smallest number is ",min(List))
    print("There are",str(num_duplicates3),"equal numbers.")
    print("\n")
    break
