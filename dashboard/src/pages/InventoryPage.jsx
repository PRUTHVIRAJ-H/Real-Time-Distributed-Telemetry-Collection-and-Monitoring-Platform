import useTelemetry from "../hooks/useTelemetry";
import DeviceTable from "../components/DeviceTable";

function InventoryPage() {
  const nodes = useTelemetry();

  return (
    <div className="container">
      <h1>Inventory</h1>
      <DeviceTable nodes={nodes} />
    </div>
  );
}

export default InventoryPage;