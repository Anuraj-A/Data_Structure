import matplotlib.pyplot as plt
import numpy as np

# Set a different Matplotlib style
plt.style.use("seaborn-darkgrid")

# Full CPU model names for each test
cpus = [
    "i5-4460S (1)", "i5-4460S (2)", "i5-4460S (3)", "i5-4460S (4)", "i5-4460S (5)",
    "i5-4460S (6)", "i5-4460S (7)", "i5-4460S (8)", "i5-4460S (9)", "i5-4460S (10)",
    "i5-4460S (11)", "i3-9100 (12)", "i3-2120 (13)", "i3-2120 (14)", "i3-2120 (15)"
]

# O(n) and O(n^2) execution times
o_n_times = [
    0.000989, 0.000959, 0.000865, 0.000249, 0.000328,
    0.000320, 0.000894, 0.000775, 0.000908, 0.000881,
    0.000354, 0.000177, 0.000244, 0.000243, 0.000322
]

o_n_squared_times = [
    21.552000, 20.889201, 22.387099, 24.798328, 21.399481,
    21.599269, 21.408919, 20.887022, 20.849592, 21.301035,
    21.548860, 19.329474, 21.442800, 21.472854, 21.519772
]

# X-axis positions
x = np.arange(len(cpus))

def plot_execution_times(x, o_n_times, o_n_squared_times, cpus):
    plt.figure(figsize=(12, 6))
    
    # Plotting O(n) and O(n^2) execution times
    plt.plot(x, o_n_times, marker="o", linestyle="-", color="blue", markersize=6, label="O(n) Time (log scale)")
    plt.plot(x, o_n_squared_times, marker="s", linestyle="-", color="red", markersize=6, label="O(n²) Time")

    # Apply logarithmic scale to the Y-axis for better visualization of O(n)
    plt.yscale("log")
    
    # Labeling the axes and adding title
    plt.xticks(x, cpus, rotation=45, ha="right", fontsize=10)
    plt.xlabel("CPU Models", fontsize=12, fontweight="bold")
    plt.ylabel("Execution Time (s)", fontsize=12, fontweight="bold")
    plt.title("Execution Time Comparison of O(n) and O(n²) Algorithms", fontsize=14, fontweight="bold")
    
    # Displaying legend, grid, and improving layout
    plt.legend(loc="upper left", fontsize=10, frameon=True, shadow=True)
    plt.grid(True, linestyle="--", alpha=0.6)
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    
    # Save the plot to a file
    plt.savefig("cpu_execution_time_comparison.png", dpi=300, bbox_inches="tight")
    
    # Show the plot
    plt.show()

# Call the function to generate the plot
plot_execution_times(x, o_n_times, o_n_squared_times, cpus)
