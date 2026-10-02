import { useState } from "react";

import Navbar from "../components/Navbar";
import AnalyzeCard from "../components/AnalyzeCard";

import RepositoryScoreCard from "../components/dashboard/RepositoryScoreCard";
import StatsCards from "../components/dashboard/StatsCards";
import HealthCard from "../components/dashboard/HealthCard";
import RepositoryTree from "../components/dashboard/RepositoryTree";
import RecommendationsCard from "../components/dashboard/RecommendationsCard";
import InsightsCard from "../components/dashboard/InsightsCard";
import DependencyGraph from "../components/dashboard/DependencyGraph";

function Home() {
  const [analysis, setAnalysis] = useState(null);

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />

      <div className="max-w-6xl mx-auto py-10 px-6">

        <AnalyzeCard onAnalyze={setAnalysis} />

        {!analysis && (
          <div className="mt-10 bg-white rounded-xl shadow-md p-8 text-center text-gray-500">
            Analyze a repository to view the dashboard.
          </div>
        )}

        {analysis && (
          <>
            <div className="mt-8">
              <RepositoryScoreCard
                score={analysis.repository_score}
              />
            </div>

            <div className="mt-8">
              <StatsCards
                metrics={{
                  total_python_files:
                    analysis.summary.total_python_files,

                  total_functions:
                    analysis.summary.total_functions,

                  total_classes:
                    analysis.summary.total_classes,

                  loc:
                    analysis.metrics.total_lines_of_code,
                }}
              />
            </div>

            <div className="mt-8">
              <HealthCard
                health={analysis.health}
              />
            </div>

            <div className="mt-8">
              <RepositoryTree
                tree={analysis.repository_tree.tree}
              />
            </div>

            <div className="mt-8">
              <RecommendationsCard
                recommendations={analysis.recommendations}
              />
            </div>

            <div className="mt-8">
              <InsightsCard
                insights={analysis.insights}
              />
            </div>

            <div className="mt-8">
              <DependencyGraph
                image={`http://127.0.0.1:8000/${analysis.dependency_graph_image.image.replace(/\\/g, "/")}`}
              />
            </div>
          </>
        )}

      </div>
    </div>
  );
}

export default Home;