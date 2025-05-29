library(ggplot2)
library(readr)
library(dplyr)

# Load phishing detection statistics CSV
data <- read_csv("../data/phishing_stats.csv")

# Example data structure: Date, Phishing_Count, Legitimate_Count

# Plot phishing vs legitimate URLs over time
ggplot(data, aes(x = as.Date(Date))) +
  geom_line(aes(y = Phishing_Count, color = "Phishing")) +
  geom_line(aes(y = Legitimate_Count, color = "Legitimate")) +
  labs(title = "Phishing Detection Trends Over Time",
       x = "Date", y = "Count", color = "Category") +
  theme_minimal()

# Save plot to PNG
ggsave("../output/phishing_trends.png")
