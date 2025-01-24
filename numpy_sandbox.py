import numpy as np

height = [188, 178, 164, 192, 157, 170]
weight = [88, 68, 72, 60, 60, 73]

np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_height / ((np_weight / 100) ** 2)

print(bmi)