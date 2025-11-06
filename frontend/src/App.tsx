import UploadImage from "./components/UploadImage";

function App() {
  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center justify-center">
      <h1 className="text-3xl font-bold mb-4">🏰 Landmark Recognition</h1>
      <UploadImage />
    </div>
  );
}

export default App;
