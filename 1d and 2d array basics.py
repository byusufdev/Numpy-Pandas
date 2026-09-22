import numpy as np
# ----------------- CONTENTS -----------------
    # ----------------- generating -----------------
    # ----------------- concatenating -----------------
    # ----------------- sorting -----------------
    # ----------------- reshaping -----------------
    # ----------------- dimension maniupulation -----------------
    # ----------------- indexing/copyingslicing -----------------


# ----------------- GENERATING ARRAYS -----------------
a_arr = np.empty(1) # generate an empty 1d/vector array with a single element (contains arbitrary uninitialised data)
# print(a_arr)

b_arr = np.array([[2, 10, 3], [9, 13, 8], [1,1,1]]) # 2d array
c_arr = np.linspace(2, 10, num = 3, dtype=np.int64) # linearly spaced, integer only, 1d array between 2 and 10 --> [2, 6, 10]




# ----------------- CONCATENATING ARRAYS -----------------
# np.concatenate only works if both arrays have the same number of dimensions
# Can dimension match by using np.newaxis (see below) or enclosing an array into a list e.g., [c_arr] --> turns 1d array into a 2d row vector then use concatenate or append
# An alternative approach: a = np.append(b_arr, [c_arr], axis = 0) ------ axis = 0 adds as row, axis = 1 adds as column

# OR
# To join as a row, use np.vstack ------ Note: number of elements in 1d array must match number of columns in 2d array
# To join as a column, use np.column_stack ----- Note: number of elements in 1d array must match number of rows in 2d array
# No need to dimension match with these ---- note: this doesnt work for arrasy above 2d

a_arr = np.vstack((b_arr, c_arr))
# print(a_arr)




# ----------------- SORTING -----------------
# numerically sorts elements along each row 
a_arr = np.sort(a_arr) 
# print(" ")
# print(a_arr)

# Other types: argsort, lexsort, searchsort, partition


# ----------------- RESHAPING -----------------
# ndim = number of dimensions (2)
# size = total number of elements in the array (9)
# shape = tuple showing the size of each dimension (rows, columns) -> (3, 3)

# print(a_arr.size, a_arr.shape)

# np.reshape() can change shape of array 
# i.e., d = a_arr.reshape(6,2) ------- Provided the elements match i.e, (4,3) --> (6,2). Each have a total of 12 elements
# to specify reading order, use "C" for row by row (all elements on row first) and "F" for column by column (all elements on column first)
d_arr = np.reshape(a_arr, (6, 2), order='C')
e_arr = np.reshape(a_arr, (6, 2), order='F')
# print(" ")
# print(d_arr)
# print(" ")
# print(e_arr)




# ----------------- DIMENSION MANIPULATION -----------------
# Can increase dimension by using np.newaxis. note: ':' denotes where the original elements go
c2_arr = c_arr[:, np.newaxis] # create a new 2d column vector with all original elements on a separate row ------- c[np.newaxis, :] creates a 2d row vector
# print(c_arr, c2_arr)
# print(c_arr.shape, c2_arr.shape)
# print("")

# or can use np.expand_dims to choose where to insert axis, better for higher dimension arrays
c3_arr = np.expand_dims(c_arr, axis = 0) # axis = 1 creates a column vector, axis = 0 creates a row vector
# print(c3_arr)
# print(c3_arr.shape)
# print("")




# ----------------- INDEXING/COPYING/SLICING -----------------
# Indexing works the same as python lists
data1 = c_arr[0]         # --> 2
data2 = c_arr[0:3]       # --> [2, 6, 10]
data3 = c_arr[:2]        # --> [2, 6]
data4 = c_arr[-2:]       # --> [6, 10]

# However creates a 'view' instead of a copy. Changing value of that index in the view will affect the intial array
# Note: this doesnt work for scalar i.e., data1[0] = 3 throws error as cant use list operations on a scalar 
slice_num = c_arr[1:] # assigns second index number and beyond '[6, 10]' ---- slice_num[0] = 5 will also change c_arr to [2, 5, 10]
# print(slice_num)
# Note: directly reassigning slice_num --- i.e., slice_num = [0, 3] --- wont change values within c_arr, will just become a standard python list


# To create a copy instead of a view, use the .copy() suffix
slice_num2 = c_arr[1:].copy()


# Conditional Slices
three_down = b_arr[b_arr <= 3] # Elements within b_arr <= 3
# print(b_arr)
# print(three_down)

divisible_by_2 = b_arr[b_arr%2 == 0]  # Elements within b_arr divisible by 2
# print(b_arr)
# print(divisible_by_2)

op_slice = b_arr[(b_arr <= 3) & (b_arr %2 == 0)] # Elements within b_arr <= 3 AND divisible by 2 
# print(b_arr)
# print(op_slice)

op_slice_bool = (b_arr <= 3) & (b_arr %2 == 0) # Same as above but returns boolean values for each element in b_arr
# print(b_arr)
# print(op_slice_bool)

