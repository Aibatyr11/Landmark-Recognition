import React, { useState } from "react";
import axios from "axios";

const API_URL = "http://127.0.0.1:8000/predict";

const UploadImage: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState<string>("");
  const [preview, setPreview] = useState<string>("");

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selected = e.target.files?.[0];
    if (selected) {
      setFile(selected);
      setPreview(URL.createObjectURL(selected));
    }
  };

  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(API_URL, formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      const { landmark_name, landmark_id } = response.data;
      setResult(`🏷 ${landmark_name} (ID: ${landmark_id})`);
    } catch (error) {
      console.error("Ошибка при отправке:", error);
      setResult("❌ Ошибка при распознавании");
    }
  };

  return (
    <div className="p-6 bg-white rounded-xl shadow-lg w-[400px] flex flex-col items-center">
      <input type="file" accept="image/*" onChange={handleFileChange} />
      {preview && (
        <img
          src={preview}
          alt="preview"
          className="mt-4 w-64 h-64 object-cover rounded-lg shadow"
        />
      )}
      <button
        onClick={handleUpload}
        className="mt-4 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
      >
        Распознать
      </button>
      {result && <p className="mt-4 text-lg font-medium text-center">{result}</p>}
    </div>
  );
};

export default UploadImage;
