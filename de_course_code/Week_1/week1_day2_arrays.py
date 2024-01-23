import numpy as np

# An array is very similar to a list.
# To a degree professor would almost say the opposite.
# arrays are more specialized. You can enlarge them in numpy but 
# that is not the intended usage.


phi = np.array([1,6,8,0,3,3,9,8,8,7,4,9,8,9,5], dtype='float_')
# print(f'Phi is an array of length {phi.size} containing {phi}.')

phi = phi.astype(int)
# print(f'Phi is an array of length {phi.size} containing {phi}.')

strs = np.array(['fee', 'fi', 'fo', 'fum'])
# print(strs)

# phi_str = np.array([1,6,8,0,3,3,9,8,8,7,4,9,8,9,5], dtype='str_')
# print(f'Phi is an array of length {phi.size} containing {phi}.)

phi_nums_div_2 = phi / 2
print(phi_nums_div_2)