function FleetInsights({ nodes }) {
  if (nodes.length === 0)
    return <div>No Devices</div>;

  const values = nodes.map(
    (n) => n.current_value
  );

  return (
    <div className="insights">
      <h2>Fleet Insights</h2>

      <p>Highest: {Math.max(...values)}</p>
      <p>Lowest: {Math.min(...values)}</p>
    </div>
  );
}

export default FleetInsights;