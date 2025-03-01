# Distributed N-Queens Solver

A solution to the [N-Queens problem (LC 51)](https://leetcode.com/problems/n-queens/) expanded into a small application. Place `N` queens on an `NxN` board with no mutual attacks, solved efficiently with backtracking and distributed task processing.

## Overview

This project implements N-Queens problem and extends to include the possibility of pre-placed queens and adds an api that can query the solver (/solve?n=9&preplaced=0,1) such that specific starting positions can be entered. In the case of large N the original solution becomes inpractical quickly. To counteract this I intend to use RabbitMQ to queue tasks for multiple workers to calculate concurrently

## Getting Started

1. **Clone the repo**:
   ```bash
   git clone https://github.com/<your-username>/distributed-n-queens.git
   cd distributed-n-queens
