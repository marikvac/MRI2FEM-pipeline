# MRI2FEM - pipeline
An end-to-end workflow, tutorial series, and collection of example scripts for converting MRI scans into computational meshes.

## Overview

This repository consists of example scripts and also readable tutorials focusing mainly on description of steps, that are needed to do,
in order to turn MRI images into computational mesh files.


In order to do this, one needs to use the following:
1. **FreeSurfer** – MRI processing and brain segmentation
2. **SVMTK** – Surface extraction and processing of segmented brain structures
3. **MeshLab** – STL surface cleaning, repair, and remeshing
4. **Gmsh** – Volumetric computational mesh generation

In this workflow, there are many problematic parts, which we try overcome.

***
> **NOTE**:
If you have a STL file and want to turn it into a computational mesh, you can start with MeshLab step.


## How to use this repository

### 1. Follow the Step-by-Step Tutorials
The `tutorial-text/` directory contains sequential guides structured like chapters in a book. Each chapter builds directly on the output of the previous stage, so the steps should be followed in order without skipping ahead.

### 2. Run the Example Scripts
Alongside the written tutorials, this repository provides standalone example scripts. Each script is intentionally focused on demonstrating a single feature or specific library operation needed in the pipeline.

### 3. Strip Comments for Clean Code
The example scripts are heavily commented for educational clarity. If you prefer clean, ready-to-copy code without inline explanations, use the included comment-stripping utility script in this repository.

---


## Used software and useful links
- For working with MRI images and segmentation of the brain, we use [FreeSurfer](https://surfer.nmr.mgh.harvard.edu/)
- For working with brain segments, we use [SVMTK](https://github.com/SVMTK/SVMTK)
- For working with STL files, we use [MeshLab](https://www.meshlab.net/)
- For creating the computational mesh itself, we use [GMSH](https://gmsh.info/), precisely the  [Python](https://www.python.org/) API

## Acknowledgments

This project was supported by the **Student Faculty Grant (SFG)** of the **Faculty of Mathematics and Physics, Charles University** (*Matematicko-fyzikální fakulta Univerzity Karlovy*). We gratefully acknowledge their financial and institutional support.