function StatsCards({ metrics }) {
  if (!metrics) return null;

  const cards = [
    {
      title: "Python Files",
      value: metrics.total_python_files,
      icon: "📄",
      color: "from-blue-500 to-cyan-500",
    },
    {
      title: "Functions",
      value: metrics.total_functions,
      icon: "⚙️",
      color: "from-purple-500 to-pink-500",
    },
    {
      title: "Classes",
      value: metrics.total_classes,
      icon: "🏛️",
      color: "from-green-500 to-emerald-500",
    },
    {
      title: "Lines of Code",
      value: metrics.loc,
      icon: "📏",
      color: "from-orange-500 to-red-500",
    },
  ];

  return (
    <div>

      <h2 className="text-2xl font-bold mb-6">
        Repository Statistics
      </h2>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">

        {cards.map((card) => (
          <div
            key={card.title}
            className="
              bg-white
              rounded-2xl
              shadow-lg
              hover:shadow-2xl
              hover:-translate-y-2
              transition
              duration-300
              overflow-hidden
            "
          >

            <div
              className={`h-2 bg-gradient-to-r ${card.color}`}
            />

            <div className="p-6">

              <div className="text-5xl mb-5">
                {card.icon}
              </div>

              <h3 className="text-gray-500 font-medium">
                {card.title}
              </h3>

              <h1 className="text-5xl font-extrabold mt-3 text-gray-800">
                {card.value}
              </h1>

            </div>

          </div>
        ))}

      </div>

    </div>
  );
}

export default StatsCards;