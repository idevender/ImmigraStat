# Examining the Relationship Between Immigration Status and Employment Outcome of Recent Graduates using a Chi-Squared Analysis

## Overview
This project investigates the potential impact of immigration status on the employment outcomes of recent graduates. Using a Chi-Squared analysis, we aim to identify if there's a significant association between the immigration status (Permanent Residency or Work Permit) and employment status (Employed or Not Employed) of individuals. The analysis is based on survey responses from international graduates, leveraging statistical methods to assess the relationship between these categorical variables.

## Introduction
A Chi-Squared test is a statistical tool used to examine if there is a significant association between two categorical variables. It compares the observed frequencies of categories with expected frequencies if there were no association between the variables. This project applies the Chi-Squared test to investigate the relationship between immigration status and employment outcomes among recent graduates.

## Installation
To run the analysis, you will need Python and several libraries. First, ensure Python is installed on your system. Then, install the required libraries using the following commands:

```bash
pip install pandas
pip install scipy
```

These libraries are crucial for performing data manipulation and conducting the Chi-Squared test.

## Data
The analysis uses the immigration_response.csv file, which contains survey responses from 500 international graduates. This dataset includes information on each graduate's immigration and employment status. For the purpose of this analysis, a subset of 75 responses was used.

## Running the Analysis
1. Ensure the Python script `chi_squared_test.py` and the dataset `immigration_response.csv` are saved in the same directory (e.g., Desktop or Downloads).
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script and dataset.
4. Run the script using the command: `python chi_squared_test.py`

The script will perform the Chi-Squared test on the data, comparing the distribution of immigration status and employment status among the surveyed graduates.

## Results
The analysis concludes that there is evidence of a significant association between immigration status and employment status based on the 75 surveyed responses. This suggests that immigration status may play a role in the employment outcomes of recent graduates.

## Conclusion
The Chi-Squared analysis provides valuable insights into the relationship between immigration status and employment outcomes among recent graduates. By identifying a significant association, this research underscores the importance of considering immigration status in discussions about employment prospects for international graduates.

For detailed analysis and code, please refer to the attached `chi_squared_test.py` file and the `immigration_response.csv` dataset. For sample code , refer below.

## Output Example
The script output, validates our analysis with concrete figures. Here is a summary of the results:

- Number of observations: 75
- Proportion of graduates with Permanent Residency (PR): 30.67%
- Proportion of graduates with a work permit: 68%
- Proportion of employed graduates: 84%
- Chi-squared statistic: 76.01720530109277
- p-value: 1.2140427994934637e-15

With a p-value significantly less than 0.05, the results indicate a statistically significant association between immigration status and employment status. This supports the hypothesis that immigration status may influence employment outcomes for recent graduates. The detailed output provides evidence of this association and underscores the relevance of the Chi-Squared test in our analysis.

## Note
This project provides a foundation for further research into the impact of immigration status on employment outcomes.