import { useEffect, useState } from "react";
import api from "../api/telemetryApi";

function InventoryPage() {
  const [devices, setDevices] = useState([]);

  useEffect(() => {
    api
      .get("/inventory")
      .then(res => setDevices(res.data));
  }, []);

  return (
    <div className="container">
      <h1>Inventory</h1>

      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>IP</th>
            <th>First Seen</th>
            <th>Last Seen</th>
          </tr>
        </thead>

        <tbody>
          {devices.map(d => (
            <tr key={d.device_id}>
              <td>{d.device_id}</td>
              <td>{d.ip}</td>
              <td>{d.first_seen}</td>
              <td>{d.last_seen}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default InventoryPage;