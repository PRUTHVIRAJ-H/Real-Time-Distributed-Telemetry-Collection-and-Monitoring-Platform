import { useNavigate } from "react-router-dom";

function DeviceTable({
  nodes = []
}) {
  const navigate = useNavigate();

  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>IP</th>
          <th>Value</th>
          <th>Status</th>
          <th>Packets</th>
          <th>Loss</th>
        </tr>
      </thead>

      <tbody>
        {nodes.map(node => (
          <tr
            key={node.device_id}
            onClick={() =>
              navigate(
                `/device/${node.device_id}`
              )
            }
          >
            <td>{node.device_id}</td>
            <td>{node.ip}</td>
            <td>{node.current_value}</td>
            <td>{node.status}</td>
            <td>{node.packets_received}</td>
            <td>{node.packet_loss}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default DeviceTable;