function HealthGauge({ chart }) {
  if (!chart) return null;

  const value = chart.value ?? 0;

  return (
    <div className="bg-white rounded-2xl shadow-lg p-6">
      <h2 className="text-2xl font-bold mb-6">
        Health Gauge
      </h2>

      <div className="flex justify-center">
        <div className="relative w-56 h-56">

          <div className="absolute inset-0 rounded-full border-[20px] border-gray-200" />

          <div
            className="absolute inset-0 rounded-full border-[20px] border-green-500"
            style={{
              clipPath: `inset(${100 - value}% 0 0 0)`,
            }}
          />

          <div className="absolute inset-0 flex flex-col items-center justify-center">
            <span className="text-5xl font-extrabold text-green-600">
              {value}
            </span>

            <span className="text-gray-500">
              /100
            </span>
          </div>

        </div>
      </div>
    </div>
  );
}

export default HealthGauge;