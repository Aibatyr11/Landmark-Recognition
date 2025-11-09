import React from "react";
import UploadImage from "./components/UploadImage";
import "./App.css";
function App() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-blue-50 via-white to-blue-100 dark:from-gray-900 dark:via-gray-950 dark:to-gray-900 transition-colors duration-500">
      <h1 className="text-4xl font-bold text-gray-800 dark:text-gray-100 mb-10 tracking-tight flex items-center gap-3">
        <span className="text-5xl">🏰</span> Landmark Recognition
      </h1>
      <UploadImage />
     
    </div>
  );
}

export default App;
