import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Setting the true values of the normal distribution.
MEAN = 5
STANDARD_DEVIATION = 2

# Creating the sample sizes and empty lists that will contain the estimated results.
sample_sizes = [5, 10, 20, 50, 100, 500, 1000]
estimated_means_list = []
estimated_standard_deviations_list = []

for sample in sample_sizes:
    # For each sample size, generates amount of results from normal distribution
    samples = np.random.normal(loc=MEAN, scale=STANDARD_DEVIATION, size=sample)
    # Calculate the Mean and Standard Deviation from the samples results, and add them to the corresponding lists.
    mean_estimate = np.mean(samples)
    standard_deviation_estimate = np.std(samples)
    estimated_means_list.append(mean_estimate)
    estimated_standard_deviations_list.append(standard_deviation_estimate)

# First graph of the estimated mean as a function of sample size with a reference line representing the true mean.
plt.plot(sample_sizes, estimated_means_list, marker='o', label='MLE Mean')
plt.axhline(MEAN, color='r', label='Real Mean')
plt.title("Mean Estimate by Sample Size")
plt.xlabel("Sample Size")
plt.ylabel("Mean Estimate")
plt.legend()
plt.show()

# Second graph of the estimated standard deviation as a function of sample size, and a reference line for true mean.
plt.plot(sample_sizes, estimated_standard_deviations_list, marker='o', label='MLE Standard Deviation')
plt.axhline(STANDARD_DEVIATION, color='r', label='Real Standard Deviation')
plt.title("Standard Deviation Estimate by Sample Size")
plt.xlabel("Sample Size")
plt.ylabel("Standard Deviation Estimate")
plt.legend()
plt.show()
