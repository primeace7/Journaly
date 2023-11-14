import React, { useState } from 'react';
import axios from 'axios';
import './Insight.css'; // Make sure to create InsightPage.css file

export default function InsightPage() {
  const [generatedInsight, setGeneratedInsight] = useState('');

  const generateInsight = () => {
    // POST request to generate insight
    axios.post('http://52.3.241.176:5000/api/v1/insight')
      .then((response) => {
        // Handle the insight response as needed
        setGeneratedInsight(response.data.insight);
      })
      .catch((error) => {
        console.error('Error generating insight:', error);
      });
  };

  return (
    <div className="insight-page">
      <h1>Insight Page</h1>
      <button onClick={generateInsight}>Generate Insight</button>
      {generatedInsight && (
        <div className="insight-result">
          <h2>Generated Insight:</h2>
          <p>{generatedInsight}</p>
        </div>
      )}
    </div>
  );
}
