export default function AlertCard({ title, description, severity }) {
  const color = severity === "high" ? "bg-red-500" : "bg-yellow-500";
  return (
    <div
      className={`p-6 rounded-lg shadow-md text-white ${color} hover:scale-105 transition-transform`}
    >
      <h3 className="text-xl font-bold mb-2">{title}</h3>
      <p>{description}</p>
    </div>
  );
}
