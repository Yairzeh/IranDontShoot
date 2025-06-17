import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# setting the values of w and b for the real sigmoid and the size of the x-axis.
WEIGHT = 2
BIAS = 1
X_AXIS_SIZE = 500

sample_sizes = [5, 10, 20, 50, 100, 500, 1000]

# creating the functions used to create a sigmoid function and calculate the best w and b estimate.
def create_sigmoid(score_z):
    """
    create sigmoid function based on the score z (z = w * x + b)
    """
    return 1 / (1 + np.exp(-score_z))


def negative_log_likelihood(parameters_w_b, input_parameter_x, result_y):
    """
    calculates the negative log likelihood (we use it to find the closest value for b and w) given parameters w, b, x, y
        * clips both ends by 10** to prevent math errors caused by probability = 0 or 1.
    """
    weight_w, bias_b = parameters_w_b
    score_z = weight_w * input_parameter_x + bias_b
    probability = create_sigmoid(score_z)

    # creating and clipping a very small  value to prevent undefined results caused by log(1- [p = 1]) or log(p = 0).
    clip_value = 10 ** -15
    probability = np.clip(probability, clip_value, 1 - clip_value)

    # creating the negative log likelihood results and returning it.
    log_likelihood_values = result_y * np.log(probability) + (1 - result_y) * np.log(1 - probability)
    return -np.sum(log_likelihood_values)


# Using the functions to create an estimated sigmoid for each sample size and create a graph.

# creating our x values amd the real sigmoid, adding a reference plot for comparisons later.
x_values = np.linspace(-5, 5, X_AXIS_SIZE)
real_sigmoid = create_sigmoid(WEIGHT * x_values + BIAS)
plt.plot(x_values, real_sigmoid, 'k--', label='Real Sigmoid', linewidth=5)

# for each sample size, estimate the weight w and bias b, add a plot of the sigmoid created from the estimated results.
for sample in sample_sizes:
    sample_parameter_x = np.random.uniform(-5, 5, size=sample)
    sample_score_z = WEIGHT * sample_parameter_x + BIAS
    sample_probability_p = create_sigmoid(sample_score_z)
    # generates binary output from binomial distribution with the sample's probabilities.
    sample_result_y = np.random.binomial(1, sample_probability_p)
    # minimizes differences to find the best results, starting from b=0, w=0.
    minimize_result = minimize(negative_log_likelihood, [0, 0], args=(sample_parameter_x, sample_result_y))
    estimate_weight, estimate_bias = minimize_result.x
    estimated_sigmoid = create_sigmoid(estimate_weight * x_values + estimate_bias)
    plt.plot(x_values, estimated_sigmoid, label=f'Sample size: {sample}')

# create titles and labels for axes and shows graph.
plt.title("Sigmoid Estimates by Sample Size")
plt.xlabel("Variable x")
plt.ylabel("Probability for y = 1")
plt.legend()
plt.grid(True)
plt.show()
