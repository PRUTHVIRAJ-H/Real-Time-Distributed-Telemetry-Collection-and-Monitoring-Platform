import useTelemetry from "../hooks/useTelemetry";
import SummaryCards from "../components/SummaryCards";
import FleetInsights from "../components/FleetInsights";
import DeviceTable from "../components/DeviceTable";

function DashboardPage() {
  const {
    nodes,
    loading,
    error
  } = useTelemetry();

  console.log(nodes)

  if (loading) {
    return <h1>Loading...</h1>;
  }

  if (error) {
    return <h1>{error}</h1>;
  }

  return (
    <div className="container">
      <h1>🚀 FleetPulse Dashboard</h1>

      <SummaryCards nodes={nodes} />

      <FleetInsights nodes={nodes} />

      <DeviceTable nodes={nodes} />
    </div>
  );
}

export default DashboardPage;