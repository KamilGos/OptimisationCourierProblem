# OptimizationCourierProblem
Solveing the courier problem about which packages should be picked up to maximise the number of packages in truck

# Approaches
In both cases the 'mip' - mixed intiger programming library was used. 
* [packages_both.py](https://github.com/KamilGos/OptimisationCourierProblem/blob/main/packages_both.py) - both priority and non-priority packages are considered together
* [packages_divided.py](https://github.com/KamilGos/OptimisationCourierProblem/blob/main/packages_divided.py) - the priority packages were packed first and then the rest of space and weight were moved for non-priority packages

### Prerequisites
```
pip install mip
pip install prettytable
```

### Author
* **Kamil Goś** 
