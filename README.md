# Distributed N-Queens Solver

A solution to the [N-Queens problem (LC 51)](https://leetcode.com/problems/n-queens/) expanded into a small application. Place `N` queens on an `NxN` board with no mutual attacks, solved efficiently with backtracking and distributed task processing.

## Overview

This project implements a Minimum Viable Product (MVP) for solving the N-Queens problem, with plans for an interactive dashboard extension. The MVP focuses on a distributed solver using RabbitMQ for task queuing, a REST API, and console output of solutions.

### MVP Features
- **Input**: CSV format (e.g., `n, preplaced` like `8, [(0,1)]`).
- **API**: `/solve?n=8&preplaced=0,1` returns solutions as JSON.
- **Output**: Console prints boards (e.g., `Q . . .` for each row).
- **Distributed Solving**: RabbitMQ queues tasks for large `N` (e.g., split rows across workers).
- **Tech Stack**:
  - Python: Backtracking solver.
  - Go: API server (`net/http`), CSV parsing, RabbitMQ producer/consumer.
  - Docker: Deployment.

### Planned Extension (Option)
- **Interactive Dashboard**: Pygame 2D board to preplace queens and animate solutions.
- **Caching**: Redis for storing common `N` solutions (e.g., `N=8`).
- **Timeline**: 3–4 weeks.

## Getting Started

1. **Clone the repo**:
   ```bash
   git clone https://github.com/<your-username>/distributed-n-queens.git
   cd distributed-n-queens
