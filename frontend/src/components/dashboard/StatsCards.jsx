function StatCard({ title, value, color }) {
  return (
    <div className="bg-white rounded-2xl shadow-md p-6">
      <h3 className="text-gray-500 text-sm">{title}</h3>

      <h1 className={`text-4xl font-bold mt-3 ${color}`}>
        {value}
      </h1>
    </div>
  );
}

export default function StatsCards({ metrics }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">

      <StatCard
        title="Python Files"
        value={metrics.total_python_files}
        color="text-blue-600"
      />

      <StatCard
        title="Functions"
        value={metrics.total_functions}
        color="text-green-600"
      />

      <StatCard
        title="Classes"
        value={metrics.total_classes}
        color="text-purple-600"
      />

      <StatCard
        title="Lines of Code"
        value={metrics.loc}
        color="text-orange-600"
      />

    </div>
  );
}