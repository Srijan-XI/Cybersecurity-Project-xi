package internal

import (
	"log"
	"net/http"
)

// InitRouter initializes the application router
func InitRouter() {
	http.HandleFunc("/api/predict", HandlePrediction)

	log.Println("✅ Server started on http://localhost:8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatalf("❌ Server failed to start: %v", err)
	}
}
