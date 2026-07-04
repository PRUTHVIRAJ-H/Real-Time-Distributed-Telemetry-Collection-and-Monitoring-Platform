import { useState, useEffect } from "react";
import api from "../api/telemetryApi";

export default function useTelemetry() {
  const [nodes, setNodes] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchNodes = async () => {
      try {
        const res = await api.get("/nodes");
        setNodes(res.data);
      } catch (err) {
        console.log(err);
      }

      setLoading(false);
    };

    fetchNodes();

    const id = setInterval(
      fetchNodes,
      1000
    );

    return () => clearInterval(id);
  }, []);

  return {
    nodes,
    loading
  };
}