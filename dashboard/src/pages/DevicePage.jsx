import { useParams } from "react-router-dom";

function DevicePage() {
  const { id } = useParams();

  return (
    <div className="container">
      <h1>{id}</h1>
      <p>Telemetry charts coming next.</p>
    </div>
  );
}

export default DevicePage;