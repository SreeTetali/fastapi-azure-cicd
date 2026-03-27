// In development, this points to your local FastAPI server.
// In production, we will change this to your Azure App Service URL.
const API_URL = "http://127.0.0.1:8000/api/visitors/";

async function fetchVisitors() {
    try {
        const response = await fetch(API_URL);
        const visitors = await response.json();
        
        const listDiv = document.getElementById('visitor-list');
        listDiv.innerHTML = ''; // Clear loading text

        if (visitors.length === 0) {
            listDiv.innerHTML = '<p>No data in the Tier 3 Database yet.</p>';
            return;
        }

        visitors.forEach(visitor => {
            const div = document.createElement('div');
            div.className = 'visitor-card';
            div.innerHTML = `<strong>${visitor.name}</strong>: ${visitor.message}`;
            listDiv.appendChild(div);
        });
    } catch (error) {
        document.getElementById('visitor-list').innerHTML = `<p style="color: red;">Error connecting to Tier 2 API: ${error.message}</p>`;
    }
}

// Run when the page loads
fetchVisitors();