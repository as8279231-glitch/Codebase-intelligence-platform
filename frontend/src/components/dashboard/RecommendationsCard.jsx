function RecommendationsCard({ recommendations }) {
  return (
    <div className="bg-white rounded-xl shadow-md p-6">
      <h2 className="text-lg font-semibold mb-4">
        Recommendations
      </h2>

      <ul className="space-y-3">
        {recommendations.map((item, index) => (
          <li
            key={index}
            className="bg-green-50 p-3 rounded-lg"
          >
            ✅ {item}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default RecommendationsCard;