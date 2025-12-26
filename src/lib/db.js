// src/lib/db.js
import mongoose from "mongoose";

export const connectToDB = async () => {
  if (mongoose.connection.readyState === 1) {
    return; // already connected
  }

  const uri = process.env.MONGO_URI;

  if (!uri) {
    throw new Error("MONGO_URI is missing in .env file");
  }

  try {
    await mongoose.connect(uri, {
      dbName: "drought_prediction",
    });
    console.log("✔ Connected to MongoDB");
  } catch (error) {
    console.error("❌ MongoDB connection error:", error);
    throw error;
  }
};
