function Hero() {
  return (
    <section className="bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-500 text-white rounded-3xl shadow-2xl px-10 py-16 mb-10">

      <p className="uppercase tracking-widest text-sm text-indigo-100 font-semibold">
        AI Powered Repository Analysis
      </p>

      <h1 className="text-5xl font-extrabold mt-3 leading-tight">
        Codebase Intelligence
        <br />
        Platform
      </h1>

      <p className="mt-6 text-lg text-indigo-100 max-w-3xl leading-8">
        Analyze software repositories, discover architecture,
        detect security issues, measure maintainability,
        visualize dependencies, and generate AI-powered
        engineering insights—all from one dashboard.
      </p>

      <div className="mt-10 flex flex-wrap gap-4">

        <div className="bg-white/20 backdrop-blur-md rounded-xl px-5 py-3">
          📊 Repository Analytics
        </div>

        <div className="bg-white/20 backdrop-blur-md rounded-xl px-5 py-3">
          🤖 AI Insights
        </div>

        <div className="bg-white/20 backdrop-blur-md rounded-xl px-5 py-3">
          🔒 Security Detection
        </div>

        <div className="bg-white/20 backdrop-blur-md rounded-xl px-5 py-3">
          🌳 Dependency Graph
        </div>

      </div>

    </section>
  );
}

export default Hero;