"use client";
import { useEffect, useState } from "react";
import AlertCard from "../../../components/AlertCard";
import LoadingSpinner from "../../../components/LoadingSpinner";

export default function Alerts() {
  const [alerts, setAlerts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/api/alerts")
      .then((res) => res.json())
      .then((data) => {
        setAlerts(data);
        setLoading(false);
      });
  }, []);

  if (loading) return <LoadingSpinner />;

  return (
    <div className="p-8 h-screen">
      <h1 className="text-4xl font-bold mb-6">Early Warning Alerts</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {alerts.map((alert, i) => (
          <AlertCard key={i} {...alert} />
        ))}
      </div>
    </div>
  );
}
