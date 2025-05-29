document.getElementById('urlForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const url = document.getElementById('urlInput').value;
    const resultDiv = document.getElementById('result');
    resultDiv.textContent = 'Scanning...';

    try {
        const response = await fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url })
        });
        const data = await response.json();
        if (response.ok) {
            resultDiv.textContent = `Result: ${data.result.toUpperCase()}, Probability: ${(data.probability * 100).toFixed(2)}%`;
        } else {
            resultDiv.textContent = `Error: ${data.error}`;
        }
    } catch (err) {
        resultDiv.textContent = `Error: Could not reach server.`;
    }
});
