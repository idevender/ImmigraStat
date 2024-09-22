Examining the Relationship Between Immigration Status and Employment Outcome of Recent Graduates using a Chi-Squared Analysis
=============================================================================================================================

Overview
--------

This project investigates the potential impact of immigration status on the employment outcomes of recent graduates. Using a Chi-Squared analysis, we aim to identify if there's a significant association between the immigration status (Permanent Residency or Work Permit) and employment status (Employed or Not Employed) of individuals. The analysis is based on survey responses from international graduates, leveraging statistical methods to assess the relationship between these categorical variables.

Introduction
------------

A Chi-Squared test is a statistical tool used to examine if there is a significant association between two categorical variables. It compares the observed frequencies of categories with expected frequencies if there were no association between the variables. This project applies the Chi-Squared test to investigate the relationship between immigration status and employment outcomes among recent graduates.

Getting Started
---------------

Follow these steps to set up and run the project on your local machine.

### Prerequisites

Make sure you have the following installed:

-   Python 3.x
-   Node.js and npm
-   Vite (for frontend development)

### Installing Dependencies

Backend (Python and Node.js)
----------------------------

1.  Install the necessary Python packages:

    `pip install pandas scipy`

2.  Install the Node.js packages for the backend:

    `npm install express multer cors`

Frontend (React.js with Vite)
-----------------------------

In the frontend folder:

`npm install`

### Running the Project

1\. Running the Backend
-----------------------

The backend handles file uploads and triggers the Python script to analyze the data.

1.  Navigate to the backend directory:
   
    `cd backend
    node index.js`

2\. Running the Frontend
------------------------

The frontend is a Vite-based React application.

1.  Navigate to the frontend directory:

    `cd frontend
    npm run dev`

The app will be running at <http://localhost:3000>.

3\. Uploading a CSV File
------------------------

Once the application is running:

1.  Open the app in your browser (<http://localhost:3000>).
2.  Select a CSV file (formatted like the sample data).
3.  Click "Upload and Analyze" to view the results.

Application Overview
--------------------

### Key Components

-   **Frontend (React with Vite)**: Provides a simple interface for uploading CSV files and viewing the results.
-   **Backend (Express.js)**: Handles file uploads and triggers the Python script.
-   **Python (Statistical Analysis)**: Performs the Chi-Squared test, T-test, Correlation, ANOVA, and Logistic Regression on the dataset.

### Sample Output

When a CSV file is uploaded, the web app will analyze the data and provide results like:

![Results](backend/image.png)

Data
----

The analysis uses the `immigration_response.csv` file, which contains survey responses from 500 international graduates. This dataset includes information on each graduate's immigration and employment status. For the purpose of this analysis, a subset of 75 responses was used.

Results
-------

The analysis concludes that there is evidence of a significant association between immigration status and employment status based on the 75 surveyed responses. This suggests that immigration status may play a role in the employment outcomes of recent graduates.

Conclusion
----------

The Chi-Squared analysis provides valuable insights into the relationship between immigration status and employment outcomes among recent graduates. By identifying a significant association, this research underscores the importance of considering immigration status in discussions about employment prospects for international graduates.

For detailed analysis and code, please refer to the attached `chi_squared_test.py` file and the `immigration_response.csv` dataset.

Future Improvements
-------------------

1.  **Additional Statistical Tests**: Incorporate more advanced analyses like regression models, clustering, or advanced machine learning models.
2.  **Data Visualization**: Add graphs and charts to visualize the data and results.
3.  **Extended File Support**: Allow support for other data formats (e.g., Excel, JSON).
4.  **Enhanced Frontend**: Improve the frontend design for better user experience and functionality.

Acknowledgments
---------------

This project was inspired by the need to analyze how immigration status influences the employment outcomes of recent graduates. This was my work during a Data Science Intern position as part of the MUCEP program at Memorial University of Newfoundland.

Authors
-------

  **Devender Singh (idevender)** 
