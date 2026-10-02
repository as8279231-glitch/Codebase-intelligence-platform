export default function RepositoryScoreCard({ score }) {
  const value = score?.score ?? 0;
  const rating = score?.rating ?? "Unknown";

  return (
    <div className="bg-white rounded-2xl shadow-md p-6">
      <h2 className="text-lg font-semibold text-gray-700">
        Repository Score
      </h2>

      <div className="mt-6 flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-5xl font-bold text-blue-600">
            {value}
          </h1>

          <p className="text-gray-500 mt-2">
            /100
          </p>

          <span className="inline-block mt-4 px-4 py-1 rounded-full bg-green-100 text-green-700 font-medium">
            {rating}
          </span>
        </div>
      </div>
    </div>
  );
}