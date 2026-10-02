function InsightsCard({ insights }) {
  return (
    <div className="bg-white rounded-xl shadow-md p-6">
      <h2 className="text-lg font-semibold mb-4">
        AI Repository Insights
      </h2>

      <p className="mb-5">
        {insights.executive_summary}
      </p>

      <h3 className="font-semibold mb-2">
        Strengths
      </h3>

      <ul className="list-disc ml-6 mb-5">
        {insights.strengths.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>

      <h3 className="font-semibold mb-2">
        Risks
      </h3>

      <ul className="list-disc ml-6">
        {insights.risks.length === 0
          ? <li>No risks detected.</li>
          : insights.risks.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
      </ul>
    </div>
  );
}

export default InsightsCard;