#include <iostream>
#include <string>
#include "FileHasher.h"
#include "FileManager.h"
#include "IntegrityChecker.h"

void printUsage() {
    std::cout << "File Integrity Checker\n"
              << "Usage:\n"
              << "  add <filepath>    : Add file hash to database\n"
              << "  check <filepath>  : Check file integrity\n"
              << "  update <filepath> : Update stored hash for a file\n"
              << "  help              : Show this help message\n";
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printUsage();
        return 1;
    }

    std::string command = argv[1];
    std::string dbPath = "data/integrity_db.txt";

    FileManager fileManager(dbPath);
    fileManager.loadDatabase();

    IntegrityChecker checker(fileManager);

    if (command == "add" && argc == 3) {
        std::string filepath = argv[2];
        try {
            std::string hash = FileHasher::calculateSHA256(filepath);
            if (fileManager.containsFile(filepath)) {
                std::cout << "File already exists in database. Use update to change the hash.\n";
            } else {
                fileManager.addOrUpdateEntry(filepath, hash);
                fileManager.saveDatabase();
                std::cout << "File added with hash: " << hash << std::endl;
            }
        } catch (const std::exception& e) {
            std::cerr << "Error: " << e.what() << std::endl;
        }
    }
    else if (command == "check" && argc == 3) {
        std::string filepath = argv[2];
        bool isIntact = checker.checkIntegrity(filepath);
        if (isIntact) {
            std::cout << "Integrity verified: No changes detected.\n";
        } else {
            std::cout << "Integrity violation detected!\n";
        }
    }
    else if (command == "update" && argc == 3) {
        std::string filepath = argv[2];
        try {
            std::string hash = FileHasher::calculateSHA256(filepath);
            fileManager.addOrUpdateEntry(filepath, hash);
            fileManager.saveDatabase();
            std::cout << "File hash updated to: " << hash << std::endl;
        } catch (const std::exception& e) {
            std::cerr << "Error: " << e.what() << std::endl;
        }
    }
    else {
        printUsage();
    }

    return 0;
}
