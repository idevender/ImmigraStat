#chi-squared test by devendersingh 2023
import scipy.stats as stats
import pandas as pd

# Import the survey response data into a pandas DataFrame.
df = pd.read_csv('immigration_response.csv')

# Checking the number of observations in the dataset
n = len(df)
print('Number of observations:', n)

# Determining the proportion of graduates who possess permanent residency.
pr_proportion = df[df['immigration_status'] == 'PR'].shape[0] / n
print('Proportion of graduates with PR:', pr_proportion)

# Checking the proportion of graduates with work permit
wp_proportion = df[df['immigration_status'] == 'work permit'].shape[0] / n
print('Proportion of graduates with work permit:', wp_proportion)

# Checking the proportion of employed graduates
employed_proportion = df[df['employed'] == 'yes'].shape[0] / n
print('Proportion of employed graduates:', employed_proportion)

# Conducting a chi-squared test to compare the distribution of immigration status and employment status
observed = pd.crosstab(df['immigration_status'], df['employed'])
chi2, p, dof, expected = stats.chi2_contingency(observed)      #takes in an argument of observed, which is a contingency table representing the observed frequency of each combination of the two variables. The function returns four values: chi2 (chi-squared statistic), p (p-value), dof (degrees of freedom), and expected (expected frequency under the assumption of independence).
print('Chi-squared statistic:', chi2)
print('p-value:', p)

#Printing result
if p < 0.05:
    print('There is evidence of a significant association between immigration status and employment status.')
else:
    print('There is no evidence of a significant association between immigration status and employment status.')