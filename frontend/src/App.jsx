import { useEffect, useState } from "react";
import { checkBackendHealth } from "./services/api";

function App() {
    const [status, setStatus] = useState("Checking backend...");

    useEffect(() => {
        checkBackendHealth()
            .then((data) => {
                setStatus(`${data.service}: ${data.status}`);
            })
            .catch(() => {
                setStatus("Backend unavailable");
            });
    }, []);

    return (
        <main>
            <h1>WriteLens</h1>
            <p>{status}</p>
        </main>
    );
}

export default App;