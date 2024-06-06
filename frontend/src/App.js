import React, { useState, useEffect } from 'react';

function App() {
    const [races, setRaces] = useState([]);

    useEffect(() => {
        fetch('/races')
            .then(response => response.json())
            .then(data => setRaces(data));
    }, []);

    return (
        <div>
            <h1>Horse Betting</h1>
            <ul>
                {races.map(race => (
                    <li key={race.id}>{race.race_name}</li>
                ))}
            </ul>
        </div>
    );
}

export default App;
