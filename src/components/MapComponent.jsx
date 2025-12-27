"use client";

import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

// Fix leaflet icons
const DefaultIcon = L.icon({
  iconUrl: "/leaflet/marker-icon.png",
  shadowUrl: "/leaflet/marker-shadow.png",
});

L.Marker.prototype.options.icon = DefaultIcon;

export default function MapComponent() {
  return (
    <MapContainer
      center={[6.7749, 43.4194]}
      zoom={5}
      style={{ height: "500px", width: "100%" }}
      scrollWheelZoom={true}
      className="h-96 rounded-lg shadow-md"
      worldCopyJump={false}
      maxBoundsViscosity={1.0}
      maxBounds={[
        [-90, -180],
        [90, 180],
      ]}
    >
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />

      <Marker position={[6.7749, 43.4194]}>
        <Popup>Drought Risk: High</Popup>
      </Marker>
    </MapContainer>
  );
}
