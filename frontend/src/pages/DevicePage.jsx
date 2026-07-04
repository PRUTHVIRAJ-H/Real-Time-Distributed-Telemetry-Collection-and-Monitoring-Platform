import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import api from "../api/telemetryApi";
import TelemetryChart from "../components/TelemetryChart";

function DevicePage() {
  const { id } = useParams();

  const [device, setDevice] =
    useState(null);

  const [history, setHistory] =
    useState([]);

  useEffect(() => {
    api
      .get(`/nodes/${id}`)
      .then(res => setDevice(res.data));

    api
      .get(`/history/${id}`)
      .then(res => setHistory(res.data));
  }, [id]);

  if (!device)
    return <h1>Loading...</h1>;

  return (
    <div className="container">
      <h1>{device.device_id}</h1>

      <p>IP: {device.ip}</p>

      <p>Status: {device.status}</p>

      <p>
        Packets:
        {device.packets_received}
      </p>

      <p>
        Packet Loss:
        {device.packet_loss}
      </p>

      <TelemetryChart
        history={history}
      />
    </div>
  );
}

export default DevicePage;