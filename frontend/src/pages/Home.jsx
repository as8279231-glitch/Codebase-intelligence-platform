import { useState } from "react";

import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import AnalyzeCard from "../components/AnalyzeCard";

import DashboardHeader from "../components/dashboard/DashboardHeader";
import RepositoryScoreCard from "../components/dashboard/RepositoryScoreCard";
import StatsCards from "../components/dashboard/StatsCards";
import HealthCard from "../components/dashboard/HealthCard";
import RepositoryTree from "../components/dashboard/RepositoryTree";
import RecommendationsCard from "../components/dashboard/RecommendationsCard";
import InsightsCard from "../components/dashboard/InsightsCard";
import DependencyGraph from "../components/dashboard/DependencyGraph";

import LanguageChart from "../components/charts/LanguageChart";
import IssueChart from "../components/charts/IssueChart";
import ComplexityChart from "../components/charts/ComplexityChart";
import HealthGauge from "../components/charts/HealthGauge";

function Home() {
  const [analysis, setAnalysis] = useState(null);

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />

      <div className="max-w-7xl mx-auto py-10 px-6">

        <DashboardHeader />

        <Hero />

        <AnalyzeCard onAnalyze={setAnalysis} />

        {!analysis && (
          <div className="mt-10 bg-white rounded-2xl shadow-lg p-10 text-center text-gray-500">
            Analyze a repository to view the dashboard.
          </div>
        )}

        {analysis && (
          <>

            {/* Repository Score + Health */}

            <div className="grid lg:grid-cols-2 gap-8 mt-8">
              <RepositoryScoreCard
                score={analysis.repository_score}
              />

              <HealthCard
                health={analysis.health}
              />
            </div>

            {/* Statistics */}

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

            {/* Charts */}

            <div className="grid lg:grid-cols-2 gap-8 mt-8">

              <LanguageChart
                chart={analysis.charts.language_distribution}
              />

              <IssueChart
                chart={analysis.charts.issue_breakdown}
              />

            </div>

            <div className="grid lg:grid-cols-2 gap-8 mt-8">

              <ComplexityChart
                chart={analysis.charts.complexity_distribution}
              />

              <HealthGauge
                chart={analysis.charts.health_score}
              />

            </div>

            {/* Repository Tree + AI Insights */}

            <div className="grid lg:grid-cols-2 gap-8 mt-8">

              <RepositoryTree
                tree={analysis.repository_tree.tree}
              />

              <InsightsCard
                insights={analysis.insights}
              />

            </div>

            {/* Dependency Graph */}

            <div className="mt-8">

              <DependencyGraph
                image={`http://127.0.0.1:8000/${analysis.dependency_graph_image.image.replace(/\\/g, "/")}`}
              />

            </div>

            {/* Recommendations */}

            <div className="mt-8">

              <RecommendationsCard
                recommendations={analysis.recommendations}
              />

            </div>

          </>
        )}

      </div>
    </div>
  );
}

export default Home;