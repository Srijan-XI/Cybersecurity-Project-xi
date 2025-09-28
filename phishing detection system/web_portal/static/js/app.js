// JavaScript Logic Section
// Global variables for UI elements
const urlInput = document.getElementById('urlInput');
const checkButton = document.getElementById('checkButton');
const statusArea = document.getElementById('statusArea');

// Function to create and display a dynamic result box
function displayResult(isSafe, url, probability = null) {
    const statusClass = isSafe ? 'result-safe' : 'result-suspicious';
    const statusText = isSafe ? 'Safe' : 'Suspicious';
    const icon = isSafe
        ? '<svg class="w-8 h-8 mr-3 text-green-700" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>'
        : '<svg class="w-8 h-8 mr-3 text-red-700" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>';

    const message = isSafe
        ? `The URL appears to be **safe** based on analysis. ${probability ? `Confidence: ${probability}%` : ''}`
        : `!! DANGER !! The URL is classified as **Suspicious/Phishing Risk**. Do NOT click. ${probability ? `Confidence: ${probability}%` : ''}`;

    statusArea.innerHTML = `
        <div class="w-full p-4 rounded-xl flex flex-col md:flex-row items-center transition-all duration-300 ${statusClass}">
            <div class="flex items-center mb-3 md:mb-0">
                ${icon}
                <span class="text-xl font-extrabold">${statusText}</span>
            </div>
            <div class="md:ml-4 text-sm font-medium text-center md:text-left">
                <p class="font-bold">${url}</p>
                <p>${message.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')}</p>
            </div>
        </div>
    `;
}

// Function to show a simple loading spinner
function showLoading() {
    checkButton.disabled = true;
    checkButton.classList.add('opacity-50', 'cursor-not-allowed');
    checkButton.textContent = 'Analyzing...';
    statusArea.innerHTML = `
        <div class="flex flex-col items-center justify-center p-4">
            <svg class="animate-spin h-8 w-8 text-blue-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            <p class="mt-2 text-gray-500 font-medium">Running advanced security checks...</p>
        </div>
    `;
}

// Function to reset the button state
function hideLoading() {
    checkButton.disabled = false;
    checkButton.classList.remove('opacity-50', 'cursor-not-allowed');
    checkButton.textContent = 'Analyze URL';
}

/**
 * Core simulation logic for phishing detection.
 * @param {string} url The URL to check.
 * @returns {boolean} true if safe, false if suspicious.
 */
function checkPhishingSimulation(url) {
    const lowerUrl = url.toLowerCase();
    let suspiciousScore = 0;

    // 1. Check for common deceptive keywords
    const deceptiveKeywords = ['login', 'signin', 'verify', 'account', 'security', 'update', 'password', 'webscr', 'confirm'];
    if (deceptiveKeywords.some(keyword => lowerUrl.includes(keyword))) {
        suspiciousScore += 2;
    }

    // 2. Check for URL length (very long URLs are often used to hide the true destination)
    if (url.length > 80) {
        suspiciousScore += 1;
    }

    // 3. Check for the '@' symbol (used for embedding credentials/fake domain in the URL)
    if (lowerUrl.includes('@')) {
        suspiciousScore += 3;
    }

    // 4. Check for multiple subdomains or excessive hyphens (e.g., microsoft.com-login-verify.site)
    const dotCount = (url.match(/\./g) || []).length;
    const hyphenCount = (url.match(/-/g) || []).length;
    if (dotCount > 3 || hyphenCount > 4) {
        suspiciousScore += 2;
    }

    // 5. Check for IP addresses instead of domain names
    const ipRegex = /\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/;
    if (ipRegex.test(url)) {
        suspiciousScore += 3;
    }

    // Simple threshold: If the score is 3 or more, it's suspicious.
    return suspiciousScore < 3;
}

// Main event handler for form submission
document.getElementById('urlForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const url = urlInput.value.trim();

    if (!url) {
        // Display error message in the UI
        statusArea.innerHTML = `
            <div class="w-full p-4 rounded-xl bg-red-100 border border-red-300 text-red-700">
                <p class="font-bold">Input Error</p>
                <p class="text-sm">Please enter a valid URL to check.</p>
            </div>
        `;
        return;
    }

    // Clear previous results and show loading
    statusArea.innerHTML = '';
    showLoading();

    try {
        // First try to connect to the ML API
        const response = await fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url })
        });
        
        if (response.ok) {
            const data = await response.json();
            const result = data.result.toLowerCase();
            const probability = (data.probability * 100).toFixed(1);
            const isSafe = result !== 'phishing';
            
            displayResult(isSafe, url, probability);
        } else {
            throw new Error('API response not ok');
        }

    } catch (error) {
        console.log("ML API not available, falling back to simulation logic");
        
        // Simulate network delay for analysis (2 seconds)
        await new Promise(resolve => setTimeout(resolve, 2000));

        const isSafe = checkPhishingSimulation(url);
        displayResult(isSafe, url);

    } finally {
        hideLoading();
    }
});
