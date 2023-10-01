import random
import numpy as np

with open("test.txt", "w") as writefile:
    # Produce the numbers
    for count in range(15):
        num = (
            str(random.randint(45, 100))
            + "\t"
            + str(random.randint(45, 100))
            + "\t"
            + str(0)
            + "\n"
            + str(random.randint(1, 55))
            + "\t"
            + str(random.randint(1, 55))
            + "\t"
            + str(1)
            + "\n"
        )
        writefile.write(num)


data = np.loadtxt("test.txt")
print(num)
