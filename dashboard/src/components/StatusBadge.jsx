function StatusBadge({ status }) {
  return (
    <span
      className={
        status === "ONLINE"
          ? "online"
          : "offline"
      }
    >
      {status}
    </span>
  );
}

export default StatusBadge;