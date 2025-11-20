import React from "react";
import "./Navbar.css";

interface NavbarProps {
  currentPage: string;
  setPage: (page: string) => void;
  isLoggedIn: boolean;
}

const Navbar: React.FC<NavbarProps> = ({ currentPage, setPage, isLoggedIn }) => {
  return (
    <nav className="navbar">
      <h2>🏰 Landmark AI</h2>
      <div className="nav-buttons">
        <button
          onClick={() => setPage("recognition")}
          className={currentPage === "recognition" ? "active" : ""}
        >
          Распознавание
        </button>

        {!isLoggedIn && (
          <>
            <button
              onClick={() => setPage("login")}
              className={currentPage === "login" ? "active" : ""}
            >
              Вход
            </button>
            <button
              onClick={() => setPage("register")}
              className={currentPage === "register" ? "active" : ""}
            >
              Регистрация
            </button>
          </>
        )}

        {isLoggedIn && (
          <button
            onClick={() => setPage("profile")}
            className={currentPage === "profile" ? "active" : ""}
          >
            Профиль
          </button>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
