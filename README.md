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

### Problem description
**Motivation:** The problem is to find the best solution of which of waiting packages should be packed first to a finite-space bus to deliver as many packages as possible at once. 

**Problem description:** Let's consider some transit company that operates buses between major cities and carries commercial packages on a space-available basis. A departing bus has room for up to **650** cubic feet of packages. Also, the packages that are included cannot exceed a total weight of **750** pounds. Finally, it has to be taken into account that **half** of the space is reserved for the priority packages. The problem is to formulate and solve an integer programming model for selecting packages to be included in the shipment. Packages awaiting shipment are described in the table: 

![table](https://user-images.githubusercontent.com/44849247/102329607-e3824680-3f88-11eb-91e1-0ec323b0d704.png)

**The goal:** Maximize the total number of packages shipped provided all the constraints are satisfied.
