## CPU Performance Analysis: O(n) vs O(n²)

This project compares the execution times of two different algorithms with time complexities of O(n) and O(n²) across various CPUs. 
The goal is to visualize and analyze the performance differences between these two types of algorithms as the input size increases.

### Project Structure

- cpu_analysis.py : Python script containing the code to plot the execution times of O(n) and O(n²) algorithms across different CPUs.
- cpu_execution_time_comparison.png : Output plot showing the execution times for the O(n) and O(n²) algorithms.
- README.md : This file.

### Requirements

To run this project, you need to have the following Python packages installed:

- matplotlib - For creating visualizations.
- numpy - For handling numerical data and arrays.

You can install these dependencies using `pip`:

```bash
pip install matplotlib numpy
```
##### How to Run

Clone the repository to your local machine:

    git clone https://github.com/Anuraj-A/Data_Structure.git

Navigate into the project directory:

    cd Data_Structure

Run the cpu_analysis.py script to generate the plot:

    python cpu_analysis.py

The execution times for the O(n) and O(n²) algorithms will be plotted, and the plot will be saved as cpu_execution_time_comparison.png.

#### Analysis

The project compares the execution times of the following algorithms:

O(n): A linear algorithm where the execution time grows linearly with the input size.    
O(n²): A quadratic algorithm where the execution time grows quadratically with the input size.  

#### CPUs Tested

i5-4460S (Multiple configurations)  
i3-9100  
i3-2120  

#### Visualization

The results are visualized using a line plot with logarithmic scaling on the y-axis to better highlight the differences in execution time between the O(n) and O(n²) algorithms. The O(n) times are plotted in blue, and the O(n²) times are plotted in red.
Graph Insights

The graph will show how the execution times of both algorithms vary across different CPUs, with a clear distinction between the linear and quadratic time complexities.

The O(n) algorithm's execution time increases linearly with the input size, while the O(n²) algorithm's execution time increases much faster, which is especially visible for larger input sizes.
Conclusion

This analysis demonstrates the significant difference in performance between linear and quadratic time complexities. The results highlight how important it is to choose the right algorithm for large input sizes, as algorithms with higher time complexity can significantly impact performance, especially when processing large datasets.
