# Telemetry Dashboard

This frontend is a React + Vite dashboard for the FleetManager telemetry platform.
It listens for live UDP telemetry updates from the Python backend and renders real-time node metrics, a device inventory, and historical charts.

## Setup

```bash
cd telemetry-dashboard
npm install
cp .env.example .env
npm run dev
```

## Environment variables

The dashboard reads the backend host from environment variables:

- `VITE_API_BASE` — REST API base URL
- `VITE_WS_BASE` — Socket.IO host URL

Example:

```env
VITE_API_BASE=http://localhost:5000
VITE_WS_BASE=http://localhost:5000
```

## Notes

- Backend API routes:
  - `GET /api/clients`
  - `DELETE /api/clients/:id`
  - `GET /api/history/:id?offset=0`
- Live telemetry is delivered using Socket.IO on the same backend host.
- If the backend is hosted on a different machine, update `.env` or `.env.local` before starting.
