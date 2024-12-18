# Python Basics and Advanced Programming Examples

This repository offers a variety of Python programs ranging from fundamental concepts to advanced programming techniques, including parallel computing, threading, multiprocessing, and GPU utilization. These scripts serve as a learning resource for beginner and intermediate developers.

## Overview of Contents

### 1. **calculator.py**  
A simple program that allows users to perform basic arithmetic operations such as:  
- Addition  
- Subtraction  
- Multiplication  
- Division  
Users input two numbers and select an operation to get the result.

### 2. **data_structures.py**  
Provides examples of Python's key data structures, including:  
- Tuples  
- Lists  
- Dictionaries  
This script explores their features and showcases how to use them effectively in various scenarios.

### 3. **functions.py**  
A guide to creating and using functions in Python, covering:  
- Function definitions  
- Parameters and return values  
- Calling functions with different arguments  

### 4. **classes.py**  
Introduces the basics of object-oriented programming (OOP) in Python:  
- Defining classes and creating objects  
- Writing methods  
- Demonstrating inheritance to reuse and extend code  

### 5. **mpi_example.py**  
Explains distributed computing with **MPI** using the `mpi4py` library:  
- Sending and receiving messages between processes  
- Understanding process ranks and sizes in an MPI context  

### 6. **multiprocessing_vs_threading.py**  
A comparative script highlighting the differences between multiprocessing and threading in Python:  
- **Multiprocessing**: Runs tasks in separate processes to utilize multiple CPUs.  
- **Multithreading**: Shares memory space between threads for concurrent execution.  
Performance differences are analyzed using a basic list-processing task.

### 7. **gpu_computation.py**  
Showcases GPU acceleration using **Numba's CUDA JIT**:  
- Implements vector addition on a GPU for performance gains.  
- Includes validation of results using Numba’s CUDA functionality.

### 8. **num_parallel_computing.py**  
Demonstrates data parallelism with **NumPy**:  
- Performs vector addition using NumPy’s optimized array operations.  
- Measures execution times for large-scale computations.

### 9. **threadpool_executor.py**  
Explores task parallelism with `ThreadPoolExecutor`:  
- Manages a pool of threads to execute functions concurrently.  
- Executes tasks asynchronously, simplifying thread management.

### 10. **producer_consumer.py**  
Illustrates the classic producer-consumer problem using Python's **multiprocessing** module:  
- A `producer` generates items and adds them to a shared queue.  
- A `consumer` retrieves and processes items from the queue.

### 11. **semaphore_example.py**  
Demonstrates the use of **semaphores** in threading to control access to shared resources:  
- Limits the number of threads that can access a resource concurrently.

### 12. **multiprocessing_example.py**  
Explains the basics of Python’s **multiprocessing** module:  
- Runs two separate functions (e.g., square and cube calculations) in parallel.  
- Includes process synchronization and joining.

### 13. **fibonacci_threading.py**  
Calculates Fibonacci numbers using **multithreading**:  
- Distributes the computation across multiple threads to improve efficiency.  

### 14. **threading_event_example.py**  
Uses threading events for inter-thread communication:  
- A producer thread generates random numbers.  
- A consumer thread processes them, synchronized using an event.

### 15. **lock_example.py**  
Explains the use of thread locks for synchronization:  
- Prevents race conditions by ensuring only one thread accesses a shared resource at a time.

## Prerequisites  

To run the scripts, ensure you have Python 3.x and the following libraries installed:  
- `mpi4py` for MPI examples  
- `numba` and `numpy` for GPU and parallel computing examples  
- Core Python libraries like `threading` and `multiprocessing`  

Install the required dependencies with:  

```bash
pip install mpi4py numba numpy
```