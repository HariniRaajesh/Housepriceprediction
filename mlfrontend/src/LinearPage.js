import React, { useState } from "react";
import axios from "axios";


function LinearPage() {
  const [metrics, setMetrics] = useState(null);
  const [file, setFile] = useState(null);

  const uploadAndFetch = async () => {
    const formData = new FormData();
    formData.append("file", file);
    const res = await axios.post("http://localhost:8000/api/linear/", formData);
    setMetrics(res.data);
  };

  return (
    <div>
      <h1>Linear Regression Results</h1>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={uploadAndFetch}>Upload & Predict</button>

      {metrics && (
        <div>
          <p>MAE: {metrics.mae.toFixed(2)}</p>
          <p>R² Score: {metrics.r2.toFixed(2)}</p>
          <p>Accuracy: {metrics.accuracy.toFixed(2)}%</p>
          <img src={`http://localhost:8000${metrics.plot_url}`} alt="Plot" />
        </div>
      )}
    </div>
  );
}

export default LinearPage;
