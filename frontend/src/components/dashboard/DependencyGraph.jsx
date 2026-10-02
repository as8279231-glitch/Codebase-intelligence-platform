function DependencyGraph({ image }) {
  return (
    <div className="bg-white rounded-xl shadow-md p-6">
      <h2 className="text-lg font-semibold mb-4">
        Dependency Graph
      </h2>

      <img
        src={image}
        alt="Dependency Graph"
        className="rounded-lg border"
      />
    </div>
  );
}

export default DependencyGraph;