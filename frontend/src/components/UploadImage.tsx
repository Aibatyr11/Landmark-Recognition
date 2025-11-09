import React, { useState } from "react";
import axios from "axios";
import "./UploadImage.css";

const API_URL = "http://127.0.0.1:8000/predict";

const UploadImage: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<string>("");
  const [result, setResult] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selected = e.target.files?.[0];
    if (selected) {
      setFile(selected);
      setPreview(URL.createObjectURL(selected));
      setResult("");
    }
  };

  const handleUpload = async () => {
    if (!file) return;
    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(API_URL, formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      const { landmark_name, landmark_id } = response.data;
      setResult(`${landmark_name} `);
    } catch (error) {
      console.error("Ошибка при отправке:", error);
      setResult("❌ Ошибка при распознавании");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="upload-card">
      <label className="file-input">
        <input type="file" accept="image/*" onChange={handleFileChange} />
        {!file && <span>📸 Нажми, чтобы выбрать фото</span>}
      </label>

      {preview && (
        <div className="image-preview">
          <img src={preview} alt="preview" />
        </div>
      )}

      <button
        className={`upload-button ${loading ? "loading" : ""}`}
        onClick={handleUpload}
        disabled={!file || loading}
      >
        {loading ? "🔄 Распознаю..." : "✨ Распознать"}
      </button>

      {result && <p className="result-text">{result}</p>}
    </div>
  );
};

export default UploadImage;
