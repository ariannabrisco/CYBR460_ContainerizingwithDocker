# import statements
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# create figure
fig, ax = plt.subplots()

# create gold rectangle
gold_rect = Rectangle((0.5, 0.5), width=2, height=3, edgecolor='gold', facecolor='gold')
ax.add_patch(gold_rect)

# create blue rectangle
blue_rect = Rectangle((3, 0.5), width=1, height=4, edgecolor='blue', facecolor='blue')
ax.add_patch(blue_rect)

# Plot
plt.title("Blue Gold")
plt.xlim(0,5)
plt.ylim(0,5)
plt.show()