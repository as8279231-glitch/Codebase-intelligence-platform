import Navbar from "../components/Navbar";
import AnalyzeCard from "../components/AnalyzeCard";

import RepositoryScoreCard from "../components/dashboard/RepositoryScoreCard";
import StatsCards from "../components/dashboard/StatsCards";
import HealthCard from "../components/dashboard/HealthCard";
import RepositoryTree from "../components/dashboard/RepositoryTree";
import RecommendationsCard from "../components/dashboard/RecommendationsCard";
import InsightsCard from "../components/dashboard/InsightsCard";
import DependencyGraph from "../components/dashboard/DependencyGraph";

const demoData = {
  repository_score: {
    score: 90,
    rating: "Excellent",
  },

  health: {
    score: 100,
    grade: "A+",
  },

  summary: {
    total_python_files: 2,
    total_functions: 1,
    total_classes: 0,
  },

  metrics: {
    loc: 5,
  },

  repository_tree: {
    tree: `Test_repo
├── main.py
├── README.md
├── requirements.txt
└── utils.py`,
  },

  recommendations: [
    "No security issues detected.",
    "Complexity is healthy.",
    "Repository is production ready.",
    "No dead code detected.",
  ],

  insights: {
    executive_summary:
      "Repository health is excellent. The project follows a clean architecture with minimal complexity.",

    strengths: [
      "Low cyclomatic complexity",
      "Excellent maintainability",
      "No detected vulnerabilities",
    ],

    risks: [],
  },

  dependency_graph_image: {
    image: "https://placehold.co/900x450?text=Dependency+Graph",
  },
};

function Home() {
  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />

      <div className="max-w-6xl mx-auto py-10 px-6">

        <AnalyzeCard />

        <div className="mt-8">
          <RepositoryScoreCard score={demoData.repository_score} />
        </div>

        <div className="mt-8">
          <StatsCards
            metrics={{
              total_python_files: demoData.summary.total_python_files,
              total_functions: demoData.summary.total_functions,
              total_classes: demoData.summary.total_classes,
              loc: demoData.metrics.loc,
            }}
          />
        </div>

        <div className="mt-8">
          <HealthCard health={demoData.health} />
        </div>

        <div className="mt-8">
          <RepositoryTree tree={demoData.repository_tree.tree} />
        </div>

        <div className="mt-8">
          <RecommendationsCard
            recommendations={demoData.recommendations}
          />
        </div>

        <div className="mt-8">
          <InsightsCard
            insights={demoData.insights}
          />
        </div>

        <div className="mt-8">
          <DependencyGraph
            image={demoData.dependency_graph_image.image}
          />
        </div>

      </div>
    </div>
  );
}

export default Home;