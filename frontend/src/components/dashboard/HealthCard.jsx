function HealthCard({ health }) {
  if (!health) return null;

  const percentage = health.score;

  return (
    <div className="bg-white rounded-2xl shadow-lg overflow-hidden hover:shadow-2xl transition duration-300">

      <div className="bg-gradient-to-r from-green-500 via-emerald-500 to-teal-500 px-6 py-5">
        <h2 className="text-2xl font-bold text-white flex items-center gap-3">
          🩺 Repository Health
        </h2>

        <p className="text-green-100 mt-1">
          Overall maintainability and code health
        </p>
      </div>

      <div className="p-8 text-center">

        <div
          className="
            w-40
            h-40
            mx-auto
            rounded-full
            border-[12px]
            border-green-500
            flex
            flex-col
            items-center
            justify-center
            shadow-md
          "
        >

          <h1 className="text-5xl font-extrabold text-green-600">
            {percentage}
          </h1>

          <p className="text-gray-500 font-medium">
            /100
          </p>

        </div>

        <div className="mt-8">

          <span className="inline-block bg-green-100 text-green-700 px-6 py-2 rounded-full font-bold text-lg">
            Grade {health.grade}
          </span>

        </div>

        <div className="mt-8">

          <div className="flex justify-between text-sm mb-2">
            <span>Health Score</span>
            <span>{percentage}%</span>
          </div>

          <div className="w-full bg-gray-200 rounded-full h-4 overflow-hidden">

            <div
              className="bg-gradient-to-r from-green-500 via-emerald-500 to-teal-500 h-4 rounded-full transition-all duration-1000"
              style={{
                width: `${percentage}%`,
              }}
            />

          </div>

        </div>

        <p className="mt-6 text-gray-500">
          Higher scores indicate better maintainability,
          lower technical debt, and cleaner architecture.
        </p>

      </div>

    </div>
  );
}

export default HealthCard;