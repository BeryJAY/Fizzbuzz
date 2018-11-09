#declaring the lists to be used
first_list=[10,11,15]
second_list=[1,3,5]
#defining the function that takes two arguments
def Fizzbuzz(list1,list2):
  #This calculates the totallength of the two lists 
  combined_length= len(first_list) + len(second_list)
  #print(combined_length)
  #The conditional logic 
  if combined_length % 3 ==0:
    print("fizz")
  elif combined_length % 5 ==0:
    print("Buzz")
  elif combined_length % 5 == 0 and combined_length % 3 == 0:
    print( "FizzBuzz")
  else:
    print("combined_length") 

Fizzbuzz(first_list,second_list)


 
