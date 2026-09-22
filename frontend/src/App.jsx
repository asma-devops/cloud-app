import { useEffect, useState } from "react";

function App() {
  const [backend, setBackend] = useState(null);
  const [database, setDatabase] = useState(null);

  useEffect(() => {
    fetch("/api/health")
      .then((response) => response.json())
      .then((data) => setBackend(data));
    fetch("/api/db-health")
      .then((response) => response.json())
      .then((data) => setDatabase(data));
  }, []);

  return (
    <div>
      <h1>Cloud App Dashboard</h1>

      <h2>Backend</h2>

      {backend ? (
        <div>
          <p>Status: {backend.status}</p>
          <p>App: {backend.app}</p>
          <p>Environment: {backend.environment}</p>
        </div>
      ) : (
        <p>Loading...</p>
      )}
       <h2>Database</h2>

       {database ? (
          <p>Status: {database.database}</p>
        ) : (
          <p>Loading...</p>
)}
    </div>
  );
}

export default App;  
