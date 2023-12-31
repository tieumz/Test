# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:31:40 2023

@author: mathi
"""

#NumPy_Exercises_2

import numpy as np

#1: Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.


v = np.arange(0,21)

v[9:16]=-v[9:16]

print(v)

#2: Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.

v = np.arange(15,56)

print(v[1:])


#3: Write a NumPy program to create a 3X4 array and iterate over it.

a = np.array([[1,92,3,0],
             [5,9,7,8],
             [91,10,1,2]])

for row in a:
    for element in row:
        print(element)



#4: Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.

v = np.linspace(5,50,10)
print(v)

#5: Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.

v = np.random.randint(0,11,5)
print(v)

#6: Write a NumPy program to multiply the values of two given vectors.

v1 = np.random.randint(0,15,6)
v2 = np.random.randint(38,7839,6)

print(f"vector 1: {v1} and vector 2 : {v2}")

new_v = v1*v2
print(new_v)

#7 : Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.

v = np.arange(10,22).reshape(3,4)
print (v)

#8 : Write a NumPy program to find the number of rows and columns in a given matrix.

m = np.array([[8, 82, -2],
              [4, 5, 3]])

num_rows, num_columns = m.shape

print(f"Number of rows : {num_rows}, Number of columns : {num_columns}")

#9 : Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal.

matrice = np.zeros((4,4))

matrice[1::2, ::2]=1
matrice[::2, 1::2]=1

print(matrice)

#10: Write a NumPy program to find common values between two arrays.
#Expected Output:
#Array1: [ 0 10 20 40 60]
#Array2: [10, 30, 40]
#Common values between two arrays:
#[10 40]

Array1 = [ 0, 10, 20, 40, 60]
Array2 = [10, 30, 40]
Array3 = []

for i in Array1:
    for j in Array2:
        if i==j:
            Array3.append(i)

print(Array3)

#11: Write a NumPy program to get the unique elements of an array.
#Expected Output:
#Original array:
#[10 10 20 20 30 30]
#Unique elements of the above array:
#[10 20 30]
#Original array:
#[[1 1]
#[2 3]]
#Unique elements of the above array:
#[1 2 3]

v = [10, 10, 20, 20, 30, 30]

v_unique = np.unique(v)

print(v_unique)

#12: Write a NumPy program to compute the cross product of two given vectors.
      
v1 = np.array([33, -2, 3])
v2 = np.array([6, 6, 7])

cross_product = np.cross(v1, v2)

print(cross_product)

#13: Write a NumPy program to convert cartesian coordinates to polar coordinates of a random 10x2 matrix representing cartesian coordinates.

coord = np.random.rand(10, 2)

x = coord[:, 0]
y = coord[:, 1]
radius = np.sqrt(x**2 + y**2)
theta_radians = np.arctan2(y, x)  

print(np.round(radius, 8))
print(np.round(theta_radians, 8))

#14: Write a NumPy program to find the closest value (to a given scalar) in an array.

a= np.arange(100)

value_to_compare = 34.99062268928913

closest_value = a.flat[np.abs(a - value_to_compare).argmin()]

print(f"The closest value is {closest_value:.2f}")