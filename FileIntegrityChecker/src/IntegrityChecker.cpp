#include "IntegrityChecker.h"
#include "FileHasher.h"
#include <iostream>

bool IntegrityChecker::checkIntegrity(const std::string& filepath) {
    if (!fileManager.containsFile(filepath)) {
        std::cerr << "File not found in database: " << filepath << std::endl;
        return false;
    }

    std::string storedHash = fileManager.getHash(filepath);
    std::string currentHash;
    try {
        currentHash = FileHasher::calculateSHA256(filepath);
    } catch (const std::exception& e) {
        std::cerr << "Error hashing file: " << e.what() << std::endl;
        return false;
    }

    return (storedHash == currentHash);
}
