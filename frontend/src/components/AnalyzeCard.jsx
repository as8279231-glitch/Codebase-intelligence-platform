import { useState } from "react";
import api from "../services/api";

function AnalyzeCard({ onAnalyze }) {
  const [path, setPath] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleAnalyze() {
    if (!path.trim()) {
      alert("Please enter a repository path.");
      return;
    }

    setLoading(true);

    try {
      const response = await api.post("/repository/analyze", {
        repository_path: path,
      });

      onAnalyze(response.data);
    } catch (error) {
      console.error(error);
      alert("Repository analysis failed.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="bg-white rounded-xl shadow-lg p-8">
      <h2 className="text-2xl font-bold mb-2">
        Repository Analyzer
      </h2>

      <p className="text-gray-500 mb-6">
        Enter the local repository path to generate a complete analysis.
      </p>

      <input
        type="text"
        value={path}
        onChange={(e) => setPath(e.target.value)}
        placeholder="C:\Users\YourName\Repository"
        className="w-full border rounded-lg p-3 mb-5"
      />

      <button
        onClick={handleAnalyze}
        disabled={loading}
        className="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 disabled:bg-gray-400 transition"
      >
        {loading ? "Analyzing..." : "Analyze Repository"}
      </button>
    </div>
  );
}

export default AnalyzeCard;