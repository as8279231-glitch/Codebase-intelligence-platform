import Navbar from "../components/Navbar";
import AnalyzeCard from "../components/AnalyzeCard";

function Home() {
  return (
    <div className="min-h-screen bg-gray-100">

      <Navbar />

      <div className="max-w-6xl mx-auto py-10 px-6">

        <AnalyzeCard />

      </div>

    </div>
  );
}

export default Home;