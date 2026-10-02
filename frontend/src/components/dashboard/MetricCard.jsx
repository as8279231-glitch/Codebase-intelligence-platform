function MetricCard({ title, value, icon, color }) {
  return (
    <div
      className={`rounded-2xl shadow-lg p-6 text-white ${color}
      hover:scale-105 transition duration-300`}
    >
      <div className="flex justify-between items-center">

        <div>
          <p className="text-sm opacity-80">
            {title}
          </p>

          <h2 className="text-3xl font-bold mt-2">
            {value}
          </h2>
        </div>

        <div className="text-5xl">
          {icon}
        </div>

      </div>
    </div>
  );
}

export default MetricCard;