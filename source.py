# import statements
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon

fig, ax = plt.subplots()

gold_rect = Rectangle((0.5, 0.5), width=2, height=3, facecolor:'yellow')
ax.add_patch(gold_rect)



plt.show()