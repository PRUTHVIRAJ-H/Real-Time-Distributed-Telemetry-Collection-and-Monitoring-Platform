import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer
} from "recharts";

function TelemetryChart({
  history
}) {
  const data =
    history.map(
      (v, i) => ({
        x: i,
        y: v
      })
    );

  return (
    <ResponsiveContainer
      width="100%"
      height={300}
    >
      <LineChart data={data}>
        <CartesianGrid />
        <XAxis dataKey="x" />
        <YAxis />
        <Tooltip />
        <Line
          dataKey="y"
          type="monotone"
        />
      </LineChart>
    </ResponsiveContainer>
  );
}

export default TelemetryChart;