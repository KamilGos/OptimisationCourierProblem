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

# Priority packages
names_p = [i for i in range(len(priorities)) if priorities[i] == 1]
w_p = [weights[i] for i in range(len(priorities)) if priorities[i] == 1]
v_p = [volumes[i] for i in range(len(priorities)) if priorities[i] == 1]

volume_p = 325
weight_p = 750
I = range(len(w_p))

m = Model("priority")

x_p = [m.add_var(var_type=BINARY) for i in I]

m.objective = maximize(xsum(x_p[i] for i in I))

m += xsum(v_p[i] * x_p[i] for i in I) <= volume_p
m += xsum(w_p[i] * x_p[i] for i in I) <= weight_p

m.optimize()

selected_p = [i for i in I if x_p[i].x >= 0.99]
selected_p_names = [names_p[i]+1 for i in selected_p]
print("selected priority packages: {}".format(selected_p_names))

# LEFTOVERS CALCULATION
used_volume = 0
used_weight = 0
for i in selected_p_names:
    used_volume += volumes[i-1]
    used_weight += weights[i-1]

volume_left = volume_p - used_volume
weight_left = weight_p - used_weight

print("Volume left: {}\nWeight left: {}".format(volume_left, weight_left))


# NON PRIORITY PACKAGES
names_np = [i for i in range(len(priorities)) if priorities[i] == 0]
print(names_np)
w_np = [weights[i] for i in range(len(priorities)) if priorities[i] == 0]
v_np = [volumes[i] for i in range(len(priorities)) if priorities[i] == 0]

volume_np = 325 + volume_left
weight_np = weight_left

I = range(len(w_np))

m = Model("non-priority")

x_np = [m.add_var(var_type=BINARY) for i in I]

m.objective = maximize(xsum(x_np[i] for i in I))

m += xsum(w_np[i] * x_np[i] for i in I) <= weight_np
m += xsum(v_np[i] * x_np[i] for i in I) <= volume_np

m.optimize()

selected_np = [i for i in I if x_np[i].x >= 0.99]
selected_np_names = [names_np[i]+1 for i in selected_np]
print("selected non-priority packages: {}".format(selected_np_names))

# LEFTOVERS CALCULATION
used_volume = 0
used_weight = 0
for i in selected_np_names:
    used_volume += volumes[i-1]
    used_weight += weights[i-1]

volume_left = volume_np - used_volume
weight_left = weight_np - used_weight

print("Volume left: {}\nWeight left: {}".format(volume_left, weight_left))

# SUMMARY
print("*"*30, "\nSUMMARY")
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
print("*"*30)