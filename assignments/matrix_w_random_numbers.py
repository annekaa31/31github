import numpy
import numpy as np

r = int(input("Please type number if rows in your matrix: "))
c = int(input("Please type number if colomn in your matrix: "))
m = np.random.randint(100, size = (r,c))
print(m)
