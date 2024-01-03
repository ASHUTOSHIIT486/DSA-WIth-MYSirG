#Question :1 :Given an array with some integer type values Write a python script to sort array values
from array import*
a1=array('i',[523,23,34,22,34])
print("Elements of original array: ");    
for i in range(0, len(a1)):    
    print(a1[i], end=" ");    
     
#Sort the array in ascending order    
for i in range(0, len(a1)):    
    for j in range(i+1, len(a1)):    
        if(a1[i] > a1[j]):    
            temp = a1[i];    
            a1[i] = a1[j];    
            a1[j] = temp;    
     
print();  
 
print("Elements of array sorted in ascending order: ");    
for i in range(0, len(a1)):    

    print(a1[i], end=" "); 

#Question :2:Given a list of hetrogeneous elements Write a python script to remove all the non int values from the list
# Given list with heterogeneous elements
mixed_list = [1, 'hello', 2.5, 3, 'world', True, 5]

# Use list comprehension to filter out non-integer values
filtered_list = [x for x in mixed_list if isinstance(x, int)]

# Print the filtered list
print(filtered_list)

#Question :3 :Write a Python script to calculate average of elements of a list
# Given list of numeric elements
numeric_list = [1, 2, 3, 21,12,223,11]

# Calculate the average
average = sum(numeric_list) / len(numeric_list)

# Print the result
print("Average:", average)

#Question :4 :write a Python script to create a list of first N tearms of a prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    prime_list = []
    num = 2
    while len(prime_list) < n:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    return prime_list

# Specify the value of N
N = 10

# Generate the list of first N prime numbers
prime_numbers = generate_primes(N)

# Print the result
print("First", N, "prime numbers:", prime_numbers)

#Question :5 :write a Python script to create a list of first N tearms of a Fibpnacci series
def generate_fibonacci(n):
    fibonacci_series = [0, 1]

    for i in range(2, n):
        next_term = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_term)

    return fibonacci_series[:n]

# Set the value of N
N = 10  # You can change N to any positive integer

# Generate the Fibonacci series
fibonacci_result = generate_fibonacci(N)

# Print the result
print("First", N, "terms of Fibonacci series:", fibonacci_result)





