function DependencyGraph({ image }) {
  if (!image) return null;

  return (
    <div className="bg-white rounded-2xl shadow-xl p-8">

      <div className="flex justify-between items-center mb-6">

        <h2 className="text-3xl font-bold">
          Dependency Graph
        </h2>

        <span className="text-sm text-gray-500">
          Repository Visualization
        </span>

      </div>

      <div className="bg-gray-100 rounded-2xl border-2 border-gray-200 p-6">

        <a
          href={image}
          target="_blank"
          rel="noopener noreferrer"
        >
          <img
            src={image}
            alt="Dependency Graph"
            className="
              w-full
              rounded-xl
              object-contain
              cursor-zoom-in
              hover:scale-[1.01]
              transition-all
              duration-300
            "
          />
        </a>

      </div>

      <p className="mt-5 text-center text-gray-500 text-sm">
        Click the graph to open the full-size image.
      </p>

    </div>
  );
}

export default DependencyGraph;