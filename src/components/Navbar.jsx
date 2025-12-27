import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="bg-white dark:bg-gray-800  shadow-md  p-4 md:hidden">
      <div className="container mx-auto flex justify-between items-center">
        <Link
          href="/dashboard"
          className="text-2xl font-bold text-blue-600 dark:text-blue-400"
        >
          Drought App
        </Link>
        <div className="space-x-4">
          <Link href="/dashboard/alerts" className="hover:text-blue-600">
            Alerts
          </Link>
          <Link href="/dashboard/map" className="hover:text-blue-600">
            Map
          </Link>
          <Link href="/dashboard/charts" className="hover:text-blue-600">
            Charts
          </Link>
          <Link href="/dashboard/settings" className="hover:text-blue-600">
            Settings
          </Link>
        </div>
      </div>
    </nav>
  );
}
