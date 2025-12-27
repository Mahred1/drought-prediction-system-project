import Link from "next/link";

export default function Sidebar() {
  return (
    <aside className="w-64 bg-gray-100 dark:bg-gray-800 p-6 hidden md:block">
      <h2 className="text-2xl font-bold mb-6">Menu</h2>
      <ul className="space-y-4">
        <li>
          <Link href="/dashboard" className="hover:text-blue-600">
            Dashboard
          </Link>
        </li>
        <li>
          <Link href="/dashboard/alerts" className="hover:text-blue-600">
            Alerts
          </Link>
        </li>
        <li>
          <Link href="/dashboard/map" className="hover:text-blue-600">
            Map
          </Link>
        </li>
        <li>
          <Link href="/dashboard/charts" className="hover:text-blue-600">
            Charts
          </Link>
        </li>
        <li>
          <Link href="/dashboard/settings" className="hover:text-blue-600">
            Settings
          </Link>
        </li>
      </ul>
    </aside>
  );
}
