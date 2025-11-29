package internal

import (
	"encoding/json"
	"net/http"
)

type PredictionRequest struct {
	URL string `json:"url"`
}

type PredictionResponse struct {
	URL        string `json:"url"`
	IsPhishing bool   `json:"is_phishing"`
	Confidence float64 `json:"confidence"`
}

// HandlePrediction handles the phishing prediction request
func HandlePrediction(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Method Not Allowed", http.StatusMethodNotAllowed)
		return
	}

	var req PredictionRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}

	// Simulate ML service interaction (Replace with real call)
	response := PredictionResponse{
		URL:        req.URL,
		IsPhishing: true,         // Placeholder
		Confidence: 0.92,         // Placeholder
	}

	// Optionally send notifications
	go SendNotification(req.URL, response.IsPhishing)

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)
}
