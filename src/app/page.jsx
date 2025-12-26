import Link from "next/link";
import Image from "next/image";

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-r from-blue-500 to-indigo-600 text-white">
      <header className="w-full py-6 text-center">
        <Image
          src="/logo.png"
          alt="Logo"
          width={200}
          height={200}
          className="mx-auto mb-4 rounded-4xl"
        />
        <h1 className="text-5xl font-extrabold mb-2 animate-fade-in">
          Drought Prediction
        </h1>
        <p className="text-xl mb-8">
          Stay ahead of droughts with real-time monitoring and predictions.
        </p>
      </header>
      <main className="flex flex-col items-center space-y-6">
        <Link
          href="/login"
          className="bg-white text-blue-600 px-8 py-4 rounded-full font-bold hover:bg-gray-100 transition-all shadow-lg"
        >
          Login
        </Link>
        <Link
          href="/register"
          className="bg-transparent border-2 border-white text-white px-8 py-4 rounded-full font-bold hover:bg-white hover:text-blue-600 transition-all"
        >
          Register
        </Link>
      </main>
      <footer className="mt-auto py-6 text-sm">
        &copy; 2025 Drought Prediction App
      </footer>
    </div>
  );
}
