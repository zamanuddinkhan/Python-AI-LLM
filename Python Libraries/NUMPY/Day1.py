"""
What is the difference between list and numpy array
Hetrogenous: A Heterogeneous collection can store different types of data together.
Hetrogenous = List
Homogenous: A Homogeneous collection stores only one type of data.
Homogenous = Array
Which one is faster? = Array
Types of Array: 1D, 2D ,3D
"""
# 1D: A 1D array is a list of items in a single line.
import numpy as np
arr1 = np.array([1,2,3,4,5,6])
print("1D ARRAY: ",arr1,"\n")

# 2D: Combination of 1D array known as 2D array.
arr2 = np.array([[1,2,3],[4,5,6]])
print("2D ARRAY: ",arr2,"\n")

# 3D: A 3D array is a list of 2D arrays stacked together.
arr3= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("3D ARRAY: ",arr3,"\n")

# To check data types
print("Data Type of ARRAY 1: ",arr1.dtype)

# To Check Dimention of Array
print("Dimention of 2D ARRAY: ",arr2.ndim)

# To Check Shape of Array
print("Shape of 3D ARRAY: ",arr3.shape)

#To Check Size of Array
print("Size of 3D ARRAY: ",arr3.size)

# To Check Item Size of Array
print("ItemSize of 3D ARRAY: ",arr3.itemsize)

# Create Array with Zeroes
arr_zeros = np.zeros((2,3)) #2D
print("For 2D Zero's Array: ",arr_zeros,"\n")

arr_zeros=np.zeros((2,3,3)) #3D
print("For 3D Zero's Array: ",arr_zeros,"\n")

# Create Array With Ones
arr_once = np.ones((2,3,3)) #3D
print("Array With Ones: ",arr_once,"\n")

# Create Array with Random Values - rand() values between 0 and 1.
arr_random = np.random.rand(10)
print("values Between 0 and 1: ",arr_random,"\n")

# randn() = Values Between Negative to Positive Values.
arr_random=np.random.randn(10)
print("Values Between Negative to Positive",arr_random,"\n")

# randint() = Integer Values Between Given Range.
arr_int = np.random.randint(1,100, size=(3,4))
print("Integer Values Between Given Range: ",arr_int,"\n")

# Create array with specific Range.
arr_range = np.arange(1,20,5) #(START,STOP,STEP)
print("Array with Specific Range: ",arr_range,"\n")

# Array Reshaping
arr_reshaped = arr_int.reshape(4,3)
print("Reshaped Array: ",arr_reshaped,"\n")

# Array Indexing
print("Indexing of Array: ",arr_reshaped[1,2],"\n")

# Array Slicing
print("Slicing of Array: ",arr_reshaped[0:2,1:3],"\n")

#Array Iteration: Iteration means repeating a block of code multiple times.
print("Iteration of Array: ")
for i in arr_reshaped:
    print(i)
    
# Array Math Operations[+,-,*,/]
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

print("\nAddtion: ",arr1 + arr2)
print("Subtration: ",arr1 - arr2)
print("Multiplication: ",arr1 * arr2)
print("Division: ",arr1 / arr2)

# Statistics Operations
print("Mean: ",np.mean(arr1))
print("Sum: ",arr1.sum())
print("Median: ",np.median(arr2))
print("Standard Deviation: ",np.std(arr2))
#Variance is the average of squared differences from the mean.
#Standard deviation is the square root of variance.
print("Variance: ",np.var(arr2))
print("Minimum: ",np.min(arr2))
print("Maximum: ",np.max(arr1))
print("Percentile: ",np.percentile(arr2,50))
print("Sorted: ",np.sort(arr2))
print("Square: ",np.sqrt(arr2))
print("Unique: ",np.unique(arr2))
print("Natural Logarithm: ",np.log(arr1))
print("Exponential: ",np.exp(arr1))
print("Power: ",np.power(arr1, 2),"\n")

#Search And Filter
print(np.where(arr1>3)) # Gives the positions (indexes) where values in arr1 are greater than 3.
print(arr2[arr2>4]) # Gives the actual values from arr2 that are greater than 4.

# Copy can not change the original object but View can.
arr_copy = arr1.copy() # Makes a new separate array. Changing arr_copy will not change arr1.
arr_view = arr1.view() # Makes a view of the same data. Changing arr_view will change arr1 because they share memory.

# arr_copy[0] = 40
# print(arr1)
# print(arr_copy)

arr_copy[0] = 500
print(arr1)
print(arr_view)
