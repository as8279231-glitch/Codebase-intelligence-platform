function RepositoryTree({ tree }) {
  return (
    <div className="bg-white rounded-xl shadow-md p-6">
      <h2 className="text-lg font-semibold mb-4">
        Repository Structure
      </h2>

      <pre className="bg-gray-900 text-green-400 rounded-lg p-4 overflow-auto text-sm">
        {tree}
      </pre>
    </div>
  );
}

export default RepositoryTree;