import numpy as np
import matplotlib.pyplot as plt

# Setting the true values of the normal distribution.
MEAN = 5
STANDARD_DEVIATION = 2
X_AXIS_SIZE = 500

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


# Creating a gaussian graph
def normal_probability_density(x_axis, mean, standard_deviation):
    """
    Returns the values resulting from the probability density function for given x_axis, mean and standard deviation.
    """
    return (1 / (np.sqrt(2 * np.pi * standard_deviation ** 2))) * np.exp(
        -((x_values - mean) ** 2) / (2 * standard_deviation ** 2))


# creating the x-axis's values.
x_values = np.linspace(0, 10, X_AXIS_SIZE)
# probability density of the real normal distribution.
real_probability_density = normal_probability_density(x_values, MEAN, STANDARD_DEVIATION)

# setting the graph size to be bigger and adding the real gaussian for reference.
plt.figure(figsize=(10, 6), dpi=100)
plt.plot(x_values, real_probability_density, 'k--', label='Real Normal', linewidth=5)

# for each sample size, create a plot of normal distribution graph.
for index in range(len(sample_sizes)):
    plt.plot(
        x_values,
        normal_probability_density(x_values, estimated_means_list[index], estimated_standard_deviations_list[index]),
        label=f'Gaussian for Sample Size: {sample_sizes[index]}'
    )

plt.title("MLE probability density function for different sample sizes")
plt.xlabel("X value")
plt.ylabel("Probability Density")
plt.legend()
plt.show()
