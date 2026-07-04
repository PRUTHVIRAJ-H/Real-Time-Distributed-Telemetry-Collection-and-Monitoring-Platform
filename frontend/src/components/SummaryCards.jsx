function SummaryCards({
  nodes = []
}) {
  const online =
    nodes.filter(
      n => n.status === "ONLINE"
    ).length;

  const packets =
    nodes.reduce(
      (a, n) => a + n.packets_received,
      0
    );

  const avg =
    nodes.length === 0
      ? 0
      : (
          nodes.reduce(
            (a, n) =>
              a + n.current_value,
            0
          ) / nodes.length
        ).toFixed(1);

  return (
    <div className="cards">
      <div className="card">
        <h3>Online Nodes</h3>
        <h1>{online}</h1>
      </div>

      <div className="card">
        <h3>Total Nodes</h3>
        <h1>{nodes.length}</h1>
      </div>

      <div className="card">
        <h3>Packets</h3>
        <h1>{packets}</h1>
      </div>

      <div className="card">
        <h3>Average Value</h3>
        <h1>{avg}</h1>
      </div>
    </div>
  );
}

export default SummaryCards;