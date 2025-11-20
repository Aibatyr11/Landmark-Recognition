import { useState } from "react";
import UploadImage from "./components/UploadImage";
import Login from "./components/Login";
import Register from "./components/Register";
import Profile from "./components/Profile";
import Navbar from "./components/Navbar";
import "./App.css";

function App() {
  const [page, setPage] = useState("recognition");
  const [isLoggedIn, setIsLoggedIn] = useState(!!localStorage.getItem("access_token"));

  return (
    <div className="min-h-screen flex flex-col items-center justify-start py-10 bg-gradient-to-br from-blue-50 via-white to-blue-100 dark:from-gray-900 dark:via-gray-950 dark:to-gray-900 transition-colors duration-500">
      <Navbar currentPage={page} setPage={setPage} isLoggedIn={isLoggedIn} />

      {page === "recognition" && <UploadImage />}
      {page === "login" && <Login setPage={setPage} setIsLoggedIn={setIsLoggedIn} />}
      {page === "register" && <Register setPage={setPage} setIsLoggedIn={setIsLoggedIn} />}
      {page === "profile" && <Profile setPage={setPage} setIsLoggedIn={setIsLoggedIn} />}
    </div>
  );
}

export default App;
