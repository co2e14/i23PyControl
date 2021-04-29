import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import time
from random import seed, random
import numpy as np

data = [
    (1, 1, 3),
    (1, 2, 4),
    (1, 3, 3),
    (1, 4, 3),
    (1, 5, 2),
    (2, 1, 5),
    (2, 2, 12),
    (2, 3, 15),
    (2, 4, 12),
    (2, 5, 4),
    (3, 1, 6),
    (3, 2, 17),
    (3, 3, 23),
    (3, 4, 21),
    (3, 5, 12),
    (4, 1, 3),
    (4, 2, 7),
    (4, 3, 13),
    (4, 4, 10),
    (4, 5, 8),
    (5, 1, 3),
    (5, 2, 4),
    (5, 3, 3),
    (5, 4, 3),
    (5, 5, 5),
]

df = pd.DataFrame(data, index=None, columns=("X", "Y", "D2"))
df = df.pivot("X", "Y", "D2")
sns.heatmap(df, cmap="coolwarm")
plt.show()

seed(3234)
x_y_d2cur = []
for y in np.around(np.linspace(-1, 2, 20, endpoint=True), 3):
    print("moving y to", y)
    for x in np.around(np.linspace(-1, 2, 21, endpoint=True), 3):
        print("moving x to", x)
        #time.sleep(2)
        x_aim = x
        while float(x_aim) != float(x):
            print("Moving X centre...")
            #time.sleep(2)
        else:
            print("X in place, reading D2 current...")
            d2c2 = random()
            x_y_d2cur.append((x, y, d2c2))
            print(str(d2c2))
            pass

df = pd.DataFrame(x_y_d2cur, columns=("X", "Y", "D2"))
df.to_json("now" + ".json")
df.to_csv("now" + ".csv")
df = df.pivot("X", "Y", "D2")
print(df)
beam_profile = sns.heatmap(df, cmap="coolwarm")
fig = beam_profile.get_figure()
fig.savefig(("now.png"))
plt.show()