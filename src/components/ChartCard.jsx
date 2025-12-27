"use client";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  LineElement,
  PointElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Bar, Line } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  LineElement,
  PointElement,
  Title,
  Tooltip,
  Legend
);

export default function ChartCard({ title, type, data }) {
  const ChartComponent = type === "bar" ? Bar : Line;
  return (
    <div className="p-6 bg-white dark:bg-gray-800 rounded-lg shadow-md">
      <h3 className="text-xl font-bold mb-4">{title}</h3>
      <ChartComponent
        data={data}
        options={{ responsive: true, scales: { y: { beginAtZero: true } } }}
      />
    </div>
  );
}
