<!-- image -->
<div align="center" id="top"> 
  <img src=images/header_image.jpg width="400" />
  &#xa0;
</div>

<h1 align="center"> courier-problem-optimization </h1>
<h2 align="center"> Solving the courier problem which packages should be picked up to maximise the number of packages in the truck  </h2>

<!-- https://shields.io/ -->
<p align="center">
  <img alt="Top language" src="https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python">
  <img alt="Status" src="https://img.shields.io/badge/Status-done-green?style=for-the-badge">
  <img alt="Code size" src="https://img.shields.io/github/languages/code-size/KamilGos/courier-problem-optimization?style=for-the-badge">
</p>

<!-- table of contents -->
<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0;
  <a href="#package-content">Content</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#eyes-implementation">Implementation</a> &#xa0; | &#xa0;
  <a href="#microscope-tests">Tests</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="#technologist-author">Author</a> &#xa0; | &#xa0;
</p>

<br>


## :dart: About ##

This repository contains two Python scripts for soling the courier problem. The courier optimisation problem is a known problem about which packages should be picked up to maximise the number of packages in a truck. This project take into account also the 'high priority' packages, that should be packed first. 

## :package: Content
* [packages_both.py](packages_both.py) - both priority and non-priority packages are considered together
* [packages_divided.py](packages_divided.py) - the priority packages were packed first and then the rest of space and weight were moved for non-priority packages

## :checkered_flag: Starting ##
```bash
# Clone this project
$ git clone https://github.com/KamilGos/courier-problem-optimization

# Access
$ cd courier-problem-optimization

# Run the relevant script
$ python3 packages_both.py
$ python3 packages_divided.py
```

## :eyes: Implementation ##
The problem is to find the best solution of which of waiting packages should be packed first to a finite-space bus to deliver as many packages as possible at once. 

Let's consider some transit company that operates buses between major cities and carries commercial packages on a space-available basis. A departing bus has room for up to **650** cubic feet of packages. Also, the packages that are included cannot exceed a total weight of **750** pounds. Finally, it has to be taken into account that **half** of the space is reserved for the priority packages. The problem is to formulate and solve an integer programming model for selecting packages to be included in the shipment. Packages awaiting shipment are described in the table: 

<div align="center" id="put_id"> 
  <img src=images/data.png width="400" />
  &#xa0;
</div>


**The goal:** Maximize the total number of packages shipped provided all the constraints are satisfied.

The problem has been solved using [Mixed Integer Programming](https://www.gurobi.com/resource/mip-basics/) approach. 

## :microscope: Tests ##
<h2>The priority and non-priority packages are considered together<h2>

<div align="center" id="put_id"> 
  <img src=images/test1.png width="300" />
  &#xa0;
</div>

<h2>The priority packages were packed first</h2>

<div align="center" id="put_id"> 
  <img src=images/test2.png width="300" />
  &#xa0;
</div>

In such a simple example, the results can be calculated manually. They confirm the correctness of the above obtained results from the algorithm. 

## :memo: License ##

This project is under license from MIT.

## :technologist: Author ##

Made with :heart: by <a href="https://github.com/KamilGos" target="_blank">Kamil Goś</a>

&#xa0;

<a href="#top">Back to top</a>

