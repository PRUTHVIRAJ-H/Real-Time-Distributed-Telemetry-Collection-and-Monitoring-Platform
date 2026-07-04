import { useNavigate } from "react-router-dom";
import StatusBadge from "./StatusBadge";

function DeviceTable({ nodes }) {
  const navigate = useNavigate();

  return (
    <table>
      <thead>
        <tr>
          <th>Device</th>
          <th>Status</th>
          <th>Value</th>
          <th>Packet Loss</th>
          <th>Packets</th>
        </tr>
      </thead>

      <tbody>
        {nodes.map((node) => (
          <tr
            key={node.device_id}
            onClick={() =>
              navigate(
                `/devices/${node.device_id}`
              )
            }
          >
            <td>{node.device_id}</td>
            <td>
              <StatusBadge
                status={node.status}
              />
            </td>
            <td>{node.current_value}</td>
            <td>{node.packet_loss}</td>
            <td>{node.packets_received}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default DeviceTable;