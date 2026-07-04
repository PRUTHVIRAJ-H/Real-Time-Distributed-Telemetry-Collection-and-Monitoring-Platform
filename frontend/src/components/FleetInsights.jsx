function FleetInsights({
  nodes = []
}) {
  if (nodes.length === 0)
    return null;

  const max = Math.max(
    ...nodes.map(
      n => n.current_value
    )
  );

  const min = Math.min(
    ...nodes.map(
      n => n.current_value
    )
  );

  return (
    <div className="card">
      <h2>Fleet Insights</h2>

      <p>Highest Reading: {max}</p>
      <p>Lowest Reading: {min}</p>
    </div>
  );
}

export default FleetInsights;