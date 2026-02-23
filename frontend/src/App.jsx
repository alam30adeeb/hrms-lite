import { Routes, Route, Link } from "react-router-dom";
import Employees from "./pages/Employees.jsx";
import Attendance from "./pages/Attendance.jsx";

function App() {
  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>HRMS Lite</h1>

      <nav style={{ marginBottom: "20px" }}>
        <Link to="/" style={{ marginRight: "15px" }}>Employees</Link>
        <Link to="/attendance">Attendance</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Employees />} />
        <Route path="/attendance" element={<Attendance />} />
      </Routes>
    </div>
  );
}

export default App;