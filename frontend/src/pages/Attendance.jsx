import { useState } from "react";
import axios from "axios";

const API = "http://127.0.0.1:8000";

function Attendance() {
  const [form, setForm] = useState({
    employee_id: "",
    date: "",
    status: "Present",
  });

  const [records, setRecords] = useState([]);
  const [summary, setSummary] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [filterDate, setFilterDate] = useState("");

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");

    try {
      await axios.post(`${API}/attendance`, form);
      alert("Attendance marked successfully");
    } catch (err) {
      setError(err.response?.data?.detail || "Error marking attendance");
    }

    setLoading(false);
  };

  const fetchAttendance = async () => {
    try {
      let url = `${API}/attendance/${form.employee_id}`;

      if (filterDate) {
        url += `?date=${filterDate}`;
      }

      const res = await axios.get(url);
      setRecords(res.data);
    } catch {
      setError("Failed to fetch attendance");
    }
  };

  const fetchSummary = async () => {
    try {
      const res = await axios.get(
        `${API}/attendance/summary/${form.employee_id}`
      );
      setSummary(res.data);
    } catch {
      setError("Failed to fetch summary");
    }
  };

  return (
    <div>
      <h2>Mark Attendance</h2>

      <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
        <input
          name="employee_id"
          placeholder="Employee ID"
          value={form.employee_id}
          onChange={handleChange}
          required
        />

        <input
          type="date"
          name="date"
          value={form.date}
          onChange={handleChange}
          required
        />

        <select
          name="status"
          value={form.status}
          onChange={handleChange}
        >
          <option value="Present">Present</option>
          <option value="Absent">Absent</option>
        </select>

        <button type="submit" disabled={loading}>
          {loading ? "Saving..." : "Mark Attendance"}
        </button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <hr />

      <h3>Filter Attendance</h3>

      <input
        type="date"
        value={filterDate}
        onChange={(e) => setFilterDate(e.target.value)}
      />

      <button onClick={fetchAttendance}>Load Records</button>

      {records.length === 0 ? (
        <p>No attendance records found.</p>
      ) : (
        <table border="1" cellPadding="8">
          <thead>
            <tr>
              <th>Date</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {records.map((rec) => (
              <tr key={rec.id}>
                <td>{new Date(rec.date).toLocaleDateString()}</td>
                <td>{rec.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      <hr />

      <h3>Attendance Summary</h3>

      <button onClick={fetchSummary}>Load Summary</button>

      {summary && (
        <div style={{ marginTop: "10px" }}>
          <p><strong>Total Present Days:</strong> {summary.total_present_days}</p>
          <p><strong>Total Absent Days:</strong> {summary.total_absent_days}</p>
          <p><strong>Total Records:</strong> {summary.total_records}</p>
        </div>
      )}
    </div>
  );
}

export default Attendance;