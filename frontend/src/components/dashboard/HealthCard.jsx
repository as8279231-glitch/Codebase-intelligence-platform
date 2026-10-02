function HealthCard({ health }) {
  return (
    <div className="bg-white rounded-xl shadow-md p-6">
      <h2 className="text-lg font-semibold mb-4">
        Repository Health
      </h2>

      <div className="flex items-center justify-center">
        <div className="w-40 h-40 rounded-full border-8 border-green-500 flex flex-col items-center justify-center">
          <span className="text-4xl font-bold">
            {health.score}
          </span>

          <span className="text-gray-500">
            /100
          </span>
        </div>
      </div>

      <p className="text-center mt-5 text-green-600 font-semibold">
        Grade: {health.grade}
      </p>
    </div>
  );
}

export default HealthCard;