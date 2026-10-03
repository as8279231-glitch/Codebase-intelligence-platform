import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

function ComplexityChart({ chart }) {
  if (!chart) return null;

  const data = chart.labels.map((label, index) => ({
    name: label,
    value: chart.values[index],
  }));

  return (
    <div className="bg-white rounded-2xl shadow-lg p-6">
      <h2 className="text-2xl font-bold mb-6">
        Complexity Distribution
      </h2>

      {data.length === 0 ? (
        <div className="h-[250px] flex items-center justify-center text-gray-500">
          No complexity data available.
        </div>
      ) : (
        <div className="h-[320px]">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={data}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis allowDecimals={false} />
              <Tooltip />

              <Bar
                dataKey="value"
                fill="#6366F1"
                radius={[8, 8, 0, 0]}
              />
            </BarChart>
          </ResponsiveContainer>
        </div>
      )}
    </div>
  );
}

export default ComplexityChart;