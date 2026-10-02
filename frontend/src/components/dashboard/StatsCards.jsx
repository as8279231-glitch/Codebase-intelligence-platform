import MetricCard from "./MetricCard";

import {
  FaPython,
  FaCode,
  FaCube,
  FaFileCode,
} from "react-icons/fa";

function StatsCards({ metrics }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">

      <MetricCard
        title="Python Files"
        value={metrics.total_python_files}
        icon={<FaPython />}
        color="bg-blue-600"
      />

      <MetricCard
        title="Functions"
        value={metrics.total_functions}
        icon={<FaCode />}
        color="bg-green-600"
      />

      <MetricCard
        title="Classes"
        value={metrics.total_classes}
        icon={<FaCube />}
        color="bg-purple-600"
      />

      <MetricCard
        title="Lines of Code"
        value={metrics.loc}
        icon={<FaFileCode />}
        color="bg-orange-500"
      />

    </div>
  );
}

export default StatsCards;