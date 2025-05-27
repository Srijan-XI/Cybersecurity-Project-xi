#include "FileManager.h"
#include <fstream>
#include <sstream>
#include <iostream>

FileManager::FileManager(const std::string& dbPath) : dbFilePath(dbPath) {}

void FileManager::loadDatabase() {
    fileHashMap.clear();
    std::ifstream dbFile(dbFilePath);
    if (!dbFile) {
        // Database file doesn't exist yet; no action required.
        return;
    }

    std::string line;
    while (std::getline(dbFile, line)) {
        std::istringstream iss(line);
        std::string filepath, hash;
        size_t delimPos = line.find('|');
        if (delimPos == std::string::npos) continue;

        filepath = line.substr(0, delimPos);
        hash = line.substr(delimPos + 1);

        fileHashMap[filepath] = hash;
    }
    dbFile.close();
}

void FileManager::saveDatabase() {
    std::ofstream dbFile(dbFilePath, std::ios::trunc);
    if (!dbFile) {
        throw std::runtime_error("Cannot open database file for writing.");
    }

    for (const auto& [filepath, hash] : fileHashMap) {
        dbFile << filepath << "|" << hash << "\n";
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
