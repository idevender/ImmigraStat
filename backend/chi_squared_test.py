import sys
import json
import scipy.stats as stats
import pandas as pd
import math

# Get the file path from command line arguments
file_path = sys.argv[1]

# Import the survey response data into a pandas DataFrame
df = pd.read_csv(file_path)

# Checking the number of observations in the dataset
n = len(df)

# Determining the proportion of graduates who possess permanent residency
pr_count = df[df['immigration_status'] == 'PR'].shape[0]
pr_proportion = pr_count / n

# Checking the proportion of graduates with work permit
wp_count = df[df['immigration_status'] == 'work permit'].shape[0]
wp_proportion = wp_count / n

# Checking the proportion of employed graduates
employed_count = df[df['employed'] == 'yes'].shape[0]
employed_proportion = employed_count / n

# Conducting a chi-squared test to compare the distribution of immigration status and employment status
observed = pd.crosstab(df['immigration_status'], df['employed'])
chi2, p, dof, expected = stats.chi2_contingency(observed)


# Format the p-value for output
formatted_p_value = (
    f'{p:.4f}' if p >= 0.0001 else f'{p:.2e}'
)

# Preparing the results
results = {
    'number_of_observations': n,
    'pr_proportion': pr_proportion,
    'wp_proportion': wp_proportion,
    'employed_proportion': employed_proportion,
    'chi_squared_statistic': round(chi2, 4),
    'chi_squared_p_value': formatted_p_value,
    'significant_association': bool(p < 0.05),
    'chi_squared_message': (
        'There is evidence of a significant association between immigration status and employment status.'
        if p < 0.05 else
        'There is no evidence of a significant association between immigration status and employment status.'
    )
}

# Output results in JSON format
print(json.dumps(results, indent=2))
