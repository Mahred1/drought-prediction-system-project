"use client";
import { useEffect, useState } from "react";
import ChartCard from "../../../components/ChartCard";
import LoadingSpinner from "../../../components/LoadingSpinner";

export default function Charts() {
  const [chartData, setChartData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/api/charts")
      .then((res) => res.json())
      .then((data) => {
        setChartData(data);
        setLoading(false);
      });
  }, []);

  if (loading) return <LoadingSpinner />;

  return (
    <div className="p-8 h-screen">
      <h1 className="text-4xl font-bold mb-6">Drought Charts</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {chartData.map((chart, i) => (
          <ChartCard
            key={i}
            title={chart.title}
            type={chart.type}
            data={chart.data}
          />
        ))}
      </div>
    </div>
  );
}
