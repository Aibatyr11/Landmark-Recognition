
import { useState, useEffect } from "react";
interface ProfileProps {
  setPage: (page: string) => void;
  setIsLoggedIn: (value: boolean) => void;
}

interface UserData {
  id: string;
  username: string;
  email: string;
}

const Profile: React.FC<ProfileProps> = ({ setPage, setIsLoggedIn }) => {
  const [user, setUser] = useState<UserData | null>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    const token = localStorage.getItem("access_token");

    if (!token) {
      setPage("login");
      return;
    }

    const fetchUser = async () => {
      try {
        const res = await fetch("http://127.0.0.1:8000/auth/me", {
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        });

        if (res.status === 401) {
          localStorage.removeItem("access_token");
          setIsLoggedIn(false);
          setPage("login");
          return;
        }

        if (!res.ok) {
          const data = await res.json();
          throw new Error(data.detail || "Не удалось получить данные пользователя");
        }

        const data = await res.json();
        setUser(data);
      } catch (err: any) {
        setError(err.message);
      }
    };

    fetchUser();
  }, [setPage, setIsLoggedIn]);

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    setIsLoggedIn(false);
    setPage("login");
  };

  if (error) return <p className="error">{error}</p>;
  if (!user) return <p>Загрузка профиля...</p>;

  return (
    <div className="profile-page">
      <h2>Профиль пользователя</h2>
      <p>
        <strong>Имя:</strong> {user.username}
      </p>
      <p>
        <strong>Email:</strong> {user.email}
      </p>
      <button onClick={handleLogout}>Выйти</button>
    </div>
  );
};

export default Profile;
