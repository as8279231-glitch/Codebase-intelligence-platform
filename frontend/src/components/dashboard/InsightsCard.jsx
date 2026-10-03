function InsightsCard({ insights }) {
  if (!insights) return null;

  return (
    <div className="bg-white rounded-2xl shadow-lg overflow-hidden hover:shadow-2xl transition duration-300">

      <div className="bg-gradient-to-r from-violet-600 via-purple-600 to-indigo-700 px-6 py-5">
        <h2 className="text-2xl font-bold text-white flex items-center gap-3">
          🤖 AI Repository Insights
        </h2>

        <p className="text-purple-100 mt-1">
          AI-generated summary of your repository
        </p>
      </div>

      <div className="p-8 space-y-8">

        {/* Executive Summary */}

        <div>

          <h3 className="text-xl font-bold mb-3 text-gray-800">
            Executive Summary
          </h3>

          <div className="bg-indigo-50 border-l-4 border-indigo-600 rounded-lg p-5 text-gray-700 leading-7">
            {insights.executive_summary}
          </div>

        </div>

        {/* Strengths */}

        <div>

          <h3 className="text-xl font-bold text-green-700 mb-4">
            ✅ Strengths
          </h3>

          <div className="space-y-3">

            {insights.strengths.length > 0 ? (
              insights.strengths.map((item, index) => (
                <div
                  key={index}
                  className="bg-green-50 border border-green-200 rounded-lg px-5 py-4"
                >
                  {item}
                </div>
              ))
            ) : (
              <div className="text-gray-500">
                No strengths detected.
              </div>
            )}

          </div>

        </div>

        {/* Risks */}

        <div>

          <h3 className="text-xl font-bold text-red-700 mb-4">
            ⚠ Risks
          </h3>

          <div className="space-y-3">

            {insights.risks.length > 0 ? (
              insights.risks.map((item, index) => (
                <div
                  key={index}
                  className="bg-red-50 border border-red-200 rounded-lg px-5 py-4"
                >
                  {item}
                </div>
              ))
            ) : (
              <div className="bg-green-50 border border-green-200 rounded-lg px-5 py-4 text-green-700 font-medium">
                🎉 No risks detected.
              </div>
            )}

          </div>

        </div>

      </div>

    </div>
  );
}

export default InsightsCard;