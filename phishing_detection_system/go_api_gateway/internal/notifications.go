package internal

import (
	"log"
)

// SendNotification simulates sending a notification to admins or users
func SendNotification(url string, phishing bool) {
	if phishing {
		log.Printf("[ALERT] Phishing URL Detected: %s", url)
		// Extend: Send to Telegram, Email, Slack, etc.
	} else {
		log.Printf("[INFO] Safe URL Submitted: %s", url)
	}
}
