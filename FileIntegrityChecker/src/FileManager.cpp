#include "FileManager.h"
#include <fstream>
#include <sstream>
#include <iostream>
#include <stdexcept>

FileManager::FileManager(const std::string& dbPath) : dbFilePath(dbPath) {}

void FileManager::loadDatabase() {
    fileHashMap.clear();
    std::ifstream dbFile(dbFilePath);
    if (!dbFile) {
        // Database file doesn't exist yet; no action required.
        std::cout << "Database file not found. Starting with empty database." << std::endl;
        return;
    }

    std::string line;
    while (std::getline(dbFile, line)) {
        // Skip empty lines
        if (line.empty()) continue;
        
        size_t delimPos = line.find('|');
        if (delimPos == std::string::npos) {
            std::cerr << "Warning: Malformed database entry: " << line << std::endl;
            continue;
        }

        std::string filepath = line.substr(0, delimPos);
        std::string hash = line.substr(delimPos + 1);
        
        // Basic validation
        if (filepath.empty() || hash.empty()) {
            std::cerr << "Warning: Empty filepath or hash in entry: " << line << std::endl;
            continue;
        }

        fileHashMap[filepath] = hash;
    }
    dbFile.close();
}

void FileManager::saveDatabase() {
    std::ofstream dbFile(dbFilePath, std::ios::trunc);
    if (!dbFile) {
        throw std::runtime_error("Cannot open database file for writing.");
    }

    for (const auto& entry : fileHashMap) {
        dbFile << entry.first << "|" << entry.second << "\n";
    }
    dbFile.close();
}

void FileManager::addOrUpdateEntry(const std::string& filepath, const std::string& hash) {
    fileHashMap[filepath] = hash;
}

std::string FileManager::getHash(const std::string& filepath) {
    if (fileHashMap.find(filepath) != fileHashMap.end()) {
        return fileHashMap[filepath];
    }
    return "";
}

bool FileManager::containsFile(const std::string& filepath) {
    return fileHashMap.find(filepath) != fileHashMap.end();
}
