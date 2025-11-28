
import MapComponent from "../../../components/MapComponent";

export default function MapPage() {
  return (
    <div className="p-8 h-screen w-full">
      <h1 className="text-4xl font-bold mb-6">Interactive Drought Map</h1>
      <MapComponent />
    </div>
  );
}
