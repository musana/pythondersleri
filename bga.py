from matplotlib import pyplot as plt
import numpy as np

hours = [6,1,2,2,3,2,3,3,2]

lbl = ("Sleep", "Eating", "Vulnhub Challenges", "Web Surf and Reading", \
        "Python Practices", "Learning", "Tasks", "Other", "School Lessons")

exp = (0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015)

colors = ("#335577", "#9988cc", "y", "b", "m", "#11aadd", "#99aa99", "#332288", "#117755")

a, x = plt.subplots()

_, _, d = x.pie(hours, colors=colors, center=(0,0), counterclock=True, 
                labels=lbl, explode=exp, shadow=False, autopct='%1.1f%%')
for i in d:
    i.set_color('white')

x.axis('equal')
plt.title("WHAT AM I DOING IN A DAY 'MOSTLY' ?*\n\n")
plt.text(1.8,-1.3, "*When there is no school")
plt.legend()
plt.show()
