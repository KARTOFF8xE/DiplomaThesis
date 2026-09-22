# Aggregation and Pre-Processing of Network and Process Data for Monitoring Purposes in ROS2 Applications

This repository contains the working material for my diploma thesis at TU Bergakademie Freiberg.

The thesis focuses on monitoring and observability in ROS2 systems: collecting runtime data from processes and the network, aggregating it meaningfully, and turning it into a useful basis for operational insight, debugging, and system analysis.

In short: this is the messy-but-honest combination of research notes, LaTeX sources, figures, measurements, and prototype ideas that eventually became the thesis.

## Why this project exists

ROS2 applications can become surprisingly hard to understand once they grow beyond a toy demo. Multiple nodes, topics, DDS communication, process lifecycles, and runtime behavior all interact in ways that are not always obvious from logs alone.

This thesis explores how network and process data can be aggregated and pre-processed for monitoring purposes, with a focus on ROS2 applications. The goal is to make system behavior more transparent, easier to debug, and more actionable for engineers working with distributed robotic software.

## Thesis at a glance

- Topic: Aggregation and Pre-Processing of Network and Process Data for Monitoring Purposes in ROS2 Applications
- Author: Georg Muck
- Institution: TU Bergakademie Freiberg
- Faculty: Faculty of Mathematics and Computer Science
- Degree: Diploma Thesis
- Date: 07.07.2025

The project is about closing the gap between raw runtime signals and meaningful monitoring data. In ROS2, that includes things like:

- node and topic activity
- process-level resource usage
- network communication patterns
- DDS behavior and message flow
- runtime traces and observability metadata

The work is not just about collecting more data — it is about aggregating the right information in a useful way so that it becomes understandable and operationally valuable.

## Building the thesis

The recommended way to build the thesis is through the included VS Code Dev Container and the tasks in `.vscode/tasks.json`. This keeps the LaTeX toolchain and its dependencies in one reproducible environment instead of requiring a local TeX installation.

### Dev Container

Open the repository in VS Code and run **Dev Containers: Reopen in Container**. The setup is defined in `.devcontainer/devcontainer.json` and provides the TeX Live environment used by the project.

### Use VS Code tasks to build the thesis

After opening the Dev Container, use **Terminal: Run Task** in VS Code. **building the nomenclature** is responsible for building the project

> Be aware that a DIN-A2 figure is appended as one of the last pages of the thesis, it is not compiled with this step but has to be build manually from `figures/bigfigs/graph2/` (simply use `pdflatex main.tex` there)

## Implementation

The theoretical stuff was also implemented within a POC. Check out this REPO: [STREAM-DSM](https://github.com/KARTOFF8xE/STREAM-DSM)

## Final note

tl;dr:

> This thesis is about making ROS2 systems observable by aggregating network and process data into something that is actually useful for monitoring, debugging, and understanding runtime behavior.
