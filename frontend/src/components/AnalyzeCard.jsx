import { useState } from "react";
import api from "../services/api";


function AnalyzeCard() {
  const [path, setPath] = useState("");

 async function handleAnalyze() {

    try {

        const response = await api.post(
            "/repository/analyze",
            {
                repository_path: path
            }
        );

        console.log(response.data);

    } catch (error) {

        console.error(error);

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
        placeholder="C:\Users\YourName\Desktop\Repository"
        value={path}
        onChange={(e) => setPath(e.target.value)}
        className="w-full border rounded-lg p-3 mb-5"
      />

      <button
        onClick={handleAnalyze}
        className="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition"
      >
        Analyze Repository
      </button>

    </div>
  );
}

export default AnalyzeCard;