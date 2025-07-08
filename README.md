## Gear Design Assistant Tool

A simple Python-based module that calculates key gear design parameters using standard mechanical formulas. Supports both interactive input and batch mode via CSV files. Built to demonstrate foundational understanding of software design for gear machine applications.

## Features
- Calculates:
  - Pitch Circle Diameter
  - Addendum
  - Dedendum
  - Whole Depth
- Supports single input and CSV batch input
- Outputs results to terminal and optional CSV file

## Formulae Used
- Pitch Circle Diameter = Module × Number of Teeth
- Addendum = Module
- Dedendum = 1.25 × Module
- Whole Depth = 2.25 × Module

**Sample output**

| Teeth | Module | Pitch Diameter (mm) | Addendum (mm) | Dedendum (mm) | Whole Depth (mm) |
| ----- | ------ | ------------------- | ------------- | ------------- | ---------------- |
| 20    | 2.5    | 50.00               | 2.5           | 3.12          | 5.62             |



