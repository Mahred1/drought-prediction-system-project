"use client";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import Sidebar from "../../components/Sidebar";
import Navbar from "../../components/Navbar";
import AlertCard from "../../components/AlertCard";
import ChartCard from "../../components/ChartCard";
import LoadingSpinner from "../../components/LoadingSpinner";

export default function Dashboard() {
  const [user, setUser] = useState(null);
  const [alerts, setAlerts] = useState([]);
  const [loading, setLoading] = useState(true);
  const router = useRouter();

  useEffect(() => {
    // const token = localStorage.getItem("token");
    // if (!token) {
    //   router.push("/login");
    //   return;
    // }
    // Fetch user data (mock for now)
    setUser({ name: "User" });
    // Fetch alerts
    fetch("/api/alerts")
      .then((res) => res.json())
      .then((data) => setAlerts(data))
      .finally(() => setLoading(false));
  }, [router]);

  if (loading) return <LoadingSpinner />;

  return (
    <div className="flex flex-col md:flex-row min-h-screen">
      <Sidebar />
      <Navbar/>
      <main className="flex-grow p-8">
        <h1 className="text-4xl font-bold mb-6">Dashboard</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {alerts.map((alert, i) => (
            <AlertCard key={i} {...alert} />
          ))}
          <ChartCard title="Drought Risk" type="line" data={mockChartData} />
        </div>
      </main>
    </div>
  );
}

const mockChartData = {
  labels: ["Jan", "Feb", "Mar", "Apr", "May"],
  datasets: [
    { label: "Risk Level", data: [30, 45, 60, 50, 70], borderColor: "red" },
  ],
};
