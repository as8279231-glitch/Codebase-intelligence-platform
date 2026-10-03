function RepositoryTree({ tree }) {
  if (!tree) return null;

  const lines = tree.split("\n");

  return (
    <div className="bg-white rounded-2xl shadow-lg overflow-hidden hover:shadow-2xl transition duration-300">

      <div className="bg-gradient-to-r from-slate-800 via-slate-900 to-black px-6 py-5">
        <h2 className="text-2xl font-bold text-white flex items-center gap-3">
          📁 Repository Structure
        </h2>

        <p className="text-gray-300 mt-1">
          Project file hierarchy
        </p>
      </div>

      <div className="bg-[#1e1e1e] text-gray-100 font-mono text-sm p-6 overflow-x-auto">

        {lines.map((line, index) => (
          <div
            key={index}
            className="py-1 hover:bg-gray-800 rounded px-2 transition"
          >
            {line}
          </div>
        ))}

      </div>

    </div>
  );
}

export default RepositoryTree;