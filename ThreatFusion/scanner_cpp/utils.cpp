#include "scanner.hpp"
#include <iostream>
#include <fstream>
#include <filesystem>
#include <regex>
#include "json.hpp"


namespace fs = std::filesystem;
using json = nlohmann::json;

Scanner::Scanner(const std::string& dir, const std::string& log)
    : targetDir(dir), logFile(log) {}

void Scanner::loadSignatures(const std::string& filepath) {
    std::ifstream file(filepath);
    if (!file) {
        std::cerr << "[-] Unable to open signature file." << std::endl;
        return;
    }

    json j;
    file >> j;
    for (const auto& sig : j["signatures"]) {
        signatures[sig["pattern"]] = sig["description"];
    }
    std::cout << "[*] Loaded " << signatures.size() << " signatures." << std::endl;
}

void Scanner::scanDirectory() {
    std::ofstream log(logFile);
    for (const auto& entry : fs::recursive_directory_iterator(targetDir)) {
        if (entry.is_regular_file()) {
            scanFile(entry.path().string());
        }
    }
}

void Scanner::scanFile(const std::string& filepath) {
    std::ifstream file(filepath, std::ios::binary);
    if (!file) return;

    std::ostringstream buffer;
    buffer << file.rdbuf();
    std::string content = buffer.str();

    for (const auto& [pattern, description] : signatures) {
        std::regex hex_pattern(pattern);
        if (std::regex_search(content, hex_pattern)) {
            std::ofstream log(logFile, std::ios::app);
            log << "[!] Threat Detected in: " << filepath << " — " << description << "\n";
            std::cout << "[!] " << filepath << " -> " << description << std::endl;
        }
    }
}
