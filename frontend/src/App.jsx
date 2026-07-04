import { Routes, Route } from "react-router-dom";
import DashboardPage from "./pages/DashboardPage";
import DevicePage from "./pages/DevicePage";
import InventoryPage from "./pages/InventoryPage";

function App() {
  return (
    <Routes>
      <Route path="/" element={<DashboardPage />} />
      <Route path="/inventory" element={<InventoryPage />}/>
      <Route path="/device/:id" element={<DevicePage />}/>
    </Routes>
  );
}

export default App;