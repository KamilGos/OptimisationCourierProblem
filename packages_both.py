# Theory and Methods of Optimization
# Embedded Robotics
# Computer assignments. Problem 3 - "packages problem"
# Author: Kamil Goś

from mip import Model, xsum, maximize, BINARY
from prettytable import PrettyTable
# packages awaiting shipment
priorities = [ 1,   0,   0,   1,   0,   0,  0,   1]
volumes =    [40,  25, 130, 180,  70, 200, 35,  90]
weights =    [60, 120, 210, 240, 100, 320, 90, 150]

# extracting priority packages
names_p = [i for i in range(len(priorities)) if priorities[i] == 1]
w_p = [weights[i] for i in range(len(priorities)) if priorities[i] == 1]
v_p = [volumes[i] for i in range(len(priorities)) if priorities[i] == 1]
# extracting non-priority packages
names_np = [i for i in range(len(priorities)) if priorities[i] == 0]
w_np = [weights[i] for i in range(len(priorities)) if priorities[i] == 0]
v_np = [volumes[i] for i in range(len(priorities)) if priorities[i] == 0]

# quantitative restrictions
volume_np = 325
weight = 750

# iterators
I_p = range(len(w_p))
I_np = range(len(w_np))

# creating new model
m = Model("packages")

# creating binary variables [0-DO NOT PACK, 1-PACK]
x_p = [m.add_var(var_type=BINARY) for i in I_p]
x_np = [m.add_var(var_type=BINARY) for i in I_np]

# objective function
m.objective = maximize(xsum(x_p[i] for i in I_p) + xsum(x_np[j] for j in I_np))

# limitations
m += xsum(v_np[i] * x_np[i] for i in I_np) <= volume_np
# m += xsum(v_p[i] * x_p[i] for i in I_p) <= volume_np
m += (xsum(w_p[i] * x_p[i] for i in I_p) + xsum(w_np[j] * x_np[j] for j in I_np)) <= weight

# run the optimization process
m.optimize()

# print the results
selected_p = [i for i in I_p if x_p[i].x >= 0.99]
print(selected_p)
selected_p_names = [names_p[i]+1 for i in selected_p]
print("selected priority packages: {}".format(selected_p_names))
selected_np = [i for i in I_np if x_np[i].x >= 0.99]
selected_np_names = [names_np[i]+1 for i in selected_np]
print("selected non-priority packages: {}".format(selected_np_names))

# SUMMARY
print("*"*40, "\n", " "*15, "SUMMARY")
pt = PrettyTable()
pt.field_names = ["Package", "Priority", "Volume", "Weight"]
volume_p_sum = 0
volume_np_sum = 0
weight_p_sum = 0
weight_np_sum = 0
for i in selected_p_names:
    pt.add_row([str(i), "yes", volumes[i-1], weights[i-1]])
    volume_p_sum += volumes[i-1]
    weight_p_sum += weights[i-1]
for i in selected_np_names:
    pt.add_row([str(i), "no", volumes[i-1], weights[i-1]])
    volume_np_sum += volumes[i - 1]
    weight_np_sum += weights[i - 1]
print(pt)
print("Volume SUM: {}, Left: {}".format(volume_p_sum+volume_np_sum, 650-(volume_p_sum+volume_np_sum)))
print("Weight SUM: {}, Left: {}".format(weight_p_sum+weight_np_sum, 750-(weight_p_sum+weight_np_sum)))
print("*"*40)
