import numpy as np

""" Write a NumPy program to create an array of all even integers from 30 to 70. """
print('Write a NumPy program to create an array of all even integers from 30 to 70.')
arr = np.arange(30,71,2)
print(arr)

""" Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution. """
print('\nWrite a NumPy program to generate an array of 15 random numbers from a standard normal distribution.')
random_numbers = np.random.normal(0, 1, 15)
print(random_numbers)

""" How to compute the cross-product of two matrices in NumPy? """
print("\nHow to compute the cross-product of two matrices in NumPy? ")
# Create two matrices
mat1 = np.array([[1, 2],
                 [3, 4]])
mat2 = np.array([[1, 4],
                 [2, 5]])

# Print the result
print("Matrix 1:")
print(mat1)
print("Matrix 2:")
print(mat2)

# Using @ operator (Python >= 3.5)
cross_product = mat1 @ np.cross(mat1, mat2, axis=1)
print("Cross Product:")
print(cross_product)  

""" How to compute the determinant of an array using NumPy? """
print("\nHow to compute the determinant of an array using NumPy?")
arr = np.array([[1, 2],
                [4, 5]])
determinant = np.linalg.det(arr)
print('Array:')
print(arr)
print(f"Determinant: {determinant}")  # Output: 6.66133814775094e-16

""" How to create a 3x3x3 array with random values using NumPy? """
print('\nHow to create a 3x3x3 array with random values using NumPy?')
arr = np.random.rand(3,3,3)
print(arr)

""" How to create a 5x5 array with random values and find the minimum and maximum values using NumPy? """
print('\nHow to create a 5x5 array with random values and find the minimum and maximum values using NumPy?')
arr = np.random.rand(5,5)
minimum = arr.min()
maximum = arr.max()
print('Array:\n',arr)
print(f"Min: {minimum}")
print(f"Max: {maximum}")

""" How to compute the mean, standard deviation, and variance of a given array along the second axis in NumPy? """
print("\nHow to compute the mean, standard deviation, and variance of a given array along the second axis in NumPy?")
# Sample array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Calculate mean along the second axis
mean = np.mean(arr, axis=1)

# Calculate standard deviation along the second axis
std = np.std(arr, axis=1)

# Calculate variance along the second axis
var = np.var(arr, axis=1)

# Print the results
print("Mean:", mean)
print("Standard deviation:", std)
print("Variance:", var)
