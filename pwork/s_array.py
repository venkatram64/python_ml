import numpy as np

print(np.__version__)

person_data_def = [('name', '55'), ('height', '56'), ('weight', '72'), ('age', '50')]

print(person_data_def)

people_array = np.zeros(4, dtype=person_data_def)

print(people_array)