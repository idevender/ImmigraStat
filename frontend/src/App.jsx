// src/App.jsx
import React, { useState } from 'react';


function App() {
  const [file, setFile] = useState(null);
  const [results, setResults] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!file) {
      alert('Please select a file first!');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    fetch('http://localhost:5001/upload', {
      method: 'POST',
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        setResults(data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  return (
    <div className="container">
      <div className="box">
        <h1>Chi-Squared Test</h1>
        <form onSubmit={handleSubmit}>
          <input type="file" accept=".csv" onChange={handleFileChange} />
          <br />
          <button type="submit">Upload and Analyze</button>
        </form>
        {results && (
          <div className="results">
            <h2>Results:</h2>
            <ul>
              <li>Number of observations: {results.number_of_observations}</li>
              <li>Proportion with PR: {results.pr_proportion.toFixed(2)}</li>
              <li>
                Proportion with Work Permit: {results.wp_proportion.toFixed(2)}
              </li>
              <li>
                Proportion Employed: {results.employed_proportion.toFixed(2)}
              </li>
              <li>
                Chi-Squared Statistic:{' '}
                {results.chi_squared_statistic.toFixed(4)}
              </li>
              <li>p-value: {results.chi_squared_p_value}</li>
              <li>
                Significant Association:{' '}
                {results.significant_association ? 'Yes' : 'No'}
              </li>
              <li>Message: {results.chi_squared_message}</li>
            </ul>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
