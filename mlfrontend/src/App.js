import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route, useNavigate } from "react-router-dom";
import LinearPage from "./LinearPage";
import XGBoostPage from "./XGBoostPage";

function Home() {
  const navigate = useNavigate();
  const [selectedModel, setSelectedModel] = useState("");

  const handleSelect = (e) => {
    const model = e.target.value;
    setSelectedModel(model);
    if (model === "linear") navigate("/linear");
    if (model === "xgboost") navigate("/xgboost");
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>ML Model Visualizer</h1>
      <label>Select Model: </label>
      <select value={selectedModel} onChange={handleSelect}>
        <option value="">-- Choose Model --</option>
        <option value="linear">Linear Regression</option>
        <option value="xgboost">XGBoost</option>
      </select>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/linear" element={<LinearPage />} />
        <Route path="/xgboost" element={<XGBoostPage />} />
      </Routes>
    </Router>
  );
}

export default App;
