function RecommendationsCard({ recommendations }) {
  if (!recommendations) return null;

  return (
    <div className="bg-white rounded-2xl shadow-lg overflow-hidden hover:shadow-2xl transition duration-300">

      <div className="bg-gradient-to-r from-emerald-600 to-green-500 px-6 py-5">
        <h2 className="text-2xl font-bold text-white">
          💡 Recommendations
        </h2>

        <p className="text-green-100 mt-1">
          Suggestions to improve repository quality
        </p>
      </div>

      <div className="p-8">

        <div className="space-y-4">

          {recommendations.map((item, index) => (
            <div
              key={index}
              className="bg-green-50 border-l-4 border-green-500 rounded-lg p-5 hover:translate-x-1 transition"
            >
              {item}
            </div>
          ))}

        </div>

      </div>

    </div>
  );
}

export default RecommendationsCard;