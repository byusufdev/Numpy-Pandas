import numpy as np
# ----------------- CONTENTS -----------------
    # ----------------- generating -----------------
    # ----------------- concatenating -----------------
    # ----------------- sorting -----------------
    # ----------------- reshaping -----------------
    # ----------------- dimension maniupulation -----------------
    # ----------------- indexing/copying/slicing/conditional slicing -----------------
    # ----------------- array from existing data -----------------
    # ----------------- basic array operations -----------------
    # ----------------- higher dimensional manipulation -----------------




# ----------------- GENERATING ARRAYS -----------------
a_arr = np.empty(1) # generate an empty 1d/vector array with a single element (contains arbitrary uninitialised data), can also use np.zeros (array of 0s) or np.ones (array of 1s) 
# print(a_arr)

rng = np.random.default_rng()
random_array = rng.random((3, 2))
# print(random_array)
random_int = rng.integers(78, size = (2, 15))
# print(random_int)

ones3d = np.ones((4, 3, 2)) # generaters a 3d array of ones --> 4 matrices arranged in a 3x2
# print(ones3d)

b_arr = np.array([[2, 10, 3], [9, 13, 8], [1,1,1]]) # 2d array
c_arr = np.linspace(2, 10, num = 3, dtype=np.int64) # linearly spaced, integer only, 1d array between 2 and 10 --> [2, 6, 10]




# ----------------- CONCATENATING ARRAYS -----------------
# np.concatenate only works if both arrays have the same number of dimensions
# Can dimension match by using np.newaxis (see below) or enclosing an array into a list e.g., [c_arr] --> turns 1d array into a 2d row vector then use concatenate
# An alternative approach if dimension match: a = np.append(b_arr, [c_arr], axis = 0) ------ axis = 0 adds as row, axis = 1 adds as column

# OR
# To join as a row, use np.vstack ------ Note: number of elements in 1d array must match number of columns in 2d array
# To join as a column, use np.column_stack ----- Note: number of elements in 1d array must match number of rows in 2d array
# No need to dimension match with these ---- note: this doesnt work for arrays above 2d

a_arr = np.vstack((b_arr, c_arr))
# print(a_arr)




# ----------------- SORTING -----------------
# numerically sorts elements along each row 
a_arr = np.sort(a_arr) 
# print(" ")
# print(a_arr)

# Other types: argsort, lexsort, searchsort, partition


# ----------------- RESHAPING -----------------
# .ndim = number of dimensions
# .size = total number of elements in the array 
# .shape = tuple showing the size of each dimension --> (rows, columns)

# print(a_arr.size, a_arr.shape)

# np.reshape() can change shape of array 
# i.e., d = a_arr.reshape(6,2) ------- Provided the elements match i.e, (4,3) --> (6,2). Each have a total of 12 elements
# to specify reading order, use "C" to go row by row (all elements on row first) and "F" to go column by column (all elements on column first)
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




# ----------------- INDEXING/COPYING/SLICING/CONDITIONAL SLICING -----------------
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

op_slice = b_arr[(b_arr <= 3) | (b_arr %2 == 0)] # Elements within b_arr <= 3 OR divisible by 2 
# print(b_arr)
# print(op_slice)

op_slice_bool = (b_arr <= 3) | (b_arr %2 == 0) # Same as above but returns boolean values for each element in b_arr
# print(b_arr)
# print(op_slice_bool)

# Can use np.nonzero() function to select elements or indices within an array that meet certain conditions
b2_arr = np.nonzero(b_arr < 5) # returns a tuple of two arrays, first array = row indices and second array = column indices, of all elements in b_arr < 5
# print(b_arr)
# print(b2_arr)
# If there are no elements that meet the condition, the arrays will be empty

# Can print as below
# print(b_arr[b2_arr])

# Or: To generate a list of coordinates, use zip function to pair relevant indicies together and compile them into a list
list_of_coordinates = list(zip(b2_arr[0], b2_arr[1]))
# print(b_arr)
# for coord in list_of_coordinates:
    # print(coord)




# ----------------- ARRAY FROM EXISTING DATA -----------------
f_arr = np.array([1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
f2_arr = f_arr[3:8]
# print(f_arr)
# print(f2_arr)

cc_stack = np.column_stack((c_arr, c_arr)) # column_stack with 1d arrays creates a 2d array
# print(cc_stack)
cc_flat = np.hstack((c_arr, c_arr)) # hstack maintains a 1d array when joining the two arrays 
# print(cc_flat)

bb_stack = np.hstack((b_arr, b_arr)) # hstack works similar to column_stack when working with 2d arrays
# print(bb_stack)

bb_split = np.hsplit(bb_stack, [1]) # used to split arrays at a specific column (after first). Not using square brackets splits into 'n' number of arrays
# print(bb_split)



# ----------------- BASIC ARRAY OPERATIONS -----------------
# addition, subtraction, multiplication, division
data = np.array([1, 2])
ones = np.ones(2, dtype=int)
# print(data + ones)
# print(data - ones)
# print(data * ones)
# print(data / ones)

# Operations between scalar and array
# print(data * 10)

# sum()
dones = np.vstack((data, ones))
# print(data.sum())
# print(dones.sum(axis = 0))
# print(dones.sum(axis = 1))

# min, max
# print(dones.min())
# print(dones.max())
# print(dones.min(axis = 1))
# print(dones.max(axis = 0))


# ----------------- HIGHER DIMENSIONAL MANIPULATION -----------------
# On arrays > 1d, can use indexing across rows/columns
inarray = np.array([[1,2], [3,4], [5,6]])
# print(inarray)
# print(inarray[0,1]) #print element on row 1, column 2
# print(inarray[1:3]) #print row 2 and row 3
# print(inarray[0:2, 0]) #print all elements on column 1 that are on row 1 and row 2

# print(inarray.min(axis = 0))
# print(inarray.min(axis = 1))
# print(inarray.max(axis = 0))
# print(inarray.max(axis = 1))

multi_array = np.array([[11, 11, 12, 13, 14], [11, 11, 12, 13, 14], [15, 16, 17, 12, 13], [11, 14, 18, 19, 20]])
# print(np.unique(multi_array, return_index = True, return_counts=True))

unique_values, occurence_count, indices = np.unique(multi_array, axis=0, return_counts = True, return_index = True) # returns unqiue values within the array + their index + frequency
# print(unique_values)
# print(indices)
# print(occurence_count)

unique_rows, row_count = np.unique(multi_array, axis=0, return_counts=True)
# print(unique_rows)
# print(row_count)
unique_columns, column_count = np.unique(multi_array, axis=1, return_counts=True)
# print(unique_rows)
# print(column_count)



# more functions
#np.where
#np.clip
#np.min, np.max, np.mean, np.std, np.median