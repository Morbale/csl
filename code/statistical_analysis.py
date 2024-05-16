from scipy.stats import mannwhitneyu
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def perform_statistical_analysis(normalized_thickness_distributions):
    results = {}
    significant_count = 0  # Initialize a counter for significant results
    total_comparisons = 0  # Initialize a counter for total comparisons

    keys = list(normalized_thickness_distributions.keys())
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            total_comparisons += 1  # Increment total comparisons for each test
            key_i = keys[i]
            key_j = keys[j]
            sample_i = normalized_thickness_distributions[key_i]
            sample_j = normalized_thickness_distributions[key_j]
            u_statistic, p_value = mannwhitneyu(sample_i, sample_j, alternative='two-sided')
            results[(key_i, key_j)] = {'U-Statistic': u_statistic, 'p-Value': p_value}
            if p_value <= 0.05:
                significant_count += 1  # Increment significant results counter if p-value is <= 0.05

    # Creating a DataFrame to display the results neatly as a matrix
    results_df = pd.DataFrame(index=keys, columns=keys)

    # Fill the DataFrame with the p-values of the Mann-Whitney U test
    for (key_i, key_j), test_results in results.items():
        results_df.at[key_i, key_j] = test_results['p-Value']
        results_df.at[key_j, key_i] = test_results['p-Value']  # The matrix is symmetrical

    # Replace NaN with dashes for a cleaner look since these are comparisons of the same images
    results_df.fillna('-', inplace=True)

    # Calculate and print the percentages
    significant_percentage = (significant_count / total_comparisons) * 100
    non_significant_percentage = 100 - significant_percentage

    print(f"Percentage of p-values <= 0.05: {significant_percentage:.2f}%")
    print(f"Percentage of p-values > 0.05: {non_significant_percentage:.2f}%")

    # Convert DataFrame to float and replace non-numeric entries with NaN
    results_df = results_df.apply(pd.to_numeric, errors='coerce')

    # Plot the results
    plt.figure(figsize=(12, 10))
    sns.heatmap(results_df, annot=True, cmap='coolwarm', cbar=True)
    plt.title('Mann-Whitney U Test p-Values Heatmap')
    plt.xlabel('Sample')
    plt.ylabel('Sample')

    # Ensure the output directory exists
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    output_path = os.path.join(base_dir, "csl/data/processed/contour_analysis/statistical_testing")
    os.makedirs(output_path, exist_ok=True)
    
    # Save the plot
    output_image_path = os.path.join(output_path, 'mann_whitney_u_test_results.png')
    plt.savefig(output_image_path)
    plt.close()

    print(f"Statistical analysis results saved to: {output_image_path}")

    return results_df
