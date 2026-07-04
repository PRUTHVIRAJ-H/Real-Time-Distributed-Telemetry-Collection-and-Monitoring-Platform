import { useEffect, useState } from "react";
import api from "../api/telemetryApi";

export default function useTelemetry() {
  const [nodes, setNodes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let intervalId;

    const fetchNodes = async () => {
      try {
        const response = await api.get("/nodes");
        setNodes(response.data);
        setError(null);
      } catch (err) {
        console.error("Failed to fetch telemetry:", err);
        setError("Unable to connect to backend.");
      } finally {
        setLoading(false);
      }
    };

    // Initial fetch
    fetchNodes();

    // Poll every second
    intervalId = setInterval(fetchNodes, 1000);

    return () => clearInterval(intervalId);
  }, []);

  return {
    nodes,
    loading,
    error,
  };
}