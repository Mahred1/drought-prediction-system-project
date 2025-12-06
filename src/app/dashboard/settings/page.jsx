"use client";
import { useState } from "react";

export default function Settings() {
  const [theme, setTheme] = useState("light");

  const toggleTheme = () => {
    const newTheme = theme === "light" ? "dark" : "light";
    setTheme(newTheme);
    document.documentElement.classList.toggle("dark", newTheme === "dark");
  };

  return (
    <div className="p-8 h-screen">
      <h1 className="text-4xl font-bold mb-6">Settings</h1>
      <div className="space-y-4">
        <button
          onClick={toggleTheme}
          className="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-all"
        >
          Toggle to {theme === "light" ? "Dark" : "Light"} Mode
        </button>
        {/* Add more settings like profile edit */}
      </div>
    </div>
  );
}
