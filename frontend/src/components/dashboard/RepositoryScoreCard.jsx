function RepositoryScoreCard({ score }) {
  if (!score) return null;

  const percentage = score.score;

  return (
    <div className="bg-white rounded-2xl shadow-lg overflow-hidden hover:shadow-2xl transition duration-300">

      <div className="bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-500 px-6 py-5">
        <h2 className="text-2xl font-bold text-white flex items-center gap-3">
          🏆 Repository Score
        </h2>

        <p className="text-indigo-100 mt-1">
          Overall quality assessment of the repository
        </p>
      </div>

      <div className="p-8">

        <div className="text-center">

          <h1 className="text-7xl font-extrabold text-indigo-700">
            {percentage}
          </h1>

          <p className="text-xl text-gray-500 mb-6">
            /100
          </p>

          <span className="inline-block bg-green-100 text-green-700 font-semibold px-5 py-2 rounded-full">
            {score.rating}
          </span>

        </div>

        <div className="mt-8">

          <div className="flex justify-between mb-2 text-sm font-medium">
            <span>Repository Quality</span>
            <span>{percentage}%</span>
          </div>

          <div className="w-full h-5 bg-gray-200 rounded-full overflow-hidden">

            <div
              className="h-5 rounded-full bg-gradient-to-r from-indigo-600 via-purple-500 to-pink-500 transition-all duration-1000"
              style={{
                width: `${percentage}%`,
              }}
            />

          </div>

        </div>

      </div>

    </div>
  );
}

export default RepositoryScoreCard;