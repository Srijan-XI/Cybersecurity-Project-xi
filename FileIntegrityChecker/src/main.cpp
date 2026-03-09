#include <iostream>
#include <string>
#include "FileHasher.h"
#include "FileManager.h"
#include "IntegrityChecker.h"

void printUsage() {
    std::cout << "🛡️  File Integrity Checker\n"
              << "==============================\n"
              << "Usage:\n"
              << "  add <filepath>    : Add file hash to database\n"
              << "  check <filepath>  : Check file integrity against stored hash\n"
              << "  update <filepath> : Update stored hash for an existing file\n"
              << "  help              : Show this help message\n\n"
              << "Examples:\n"
              << "  FileIntegrityChecker add \"C:\\important\\file.txt\"\n"
              << "  FileIntegrityChecker check \"C:\\important\\file.txt\"\n"
              << "  FileIntegrityChecker update \"C:\\important\\file.txt\"\n";
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
                std::cout << "File already exists in database. Use 'update' to change the hash.\n";
                return 1;
            } else {
                fileManager.addOrUpdateEntry(filepath, hash);
                fileManager.saveDatabase();
                std::cout << "File added successfully with hash: " << hash << std::endl;
            }
        } catch (const std::exception& e) {
            std::cerr << "Error adding file: " << e.what() << std::endl;
            return 1;
        }
    }
    else if (command == "check" && argc == 3) {
        std::string filepath = argv[2];
        bool isIntact = checker.checkIntegrity(filepath);
        if (isIntact) {
            std::cout << "✓ Integrity verified: No changes detected.\n";
            return 0;
        } else {
            std::cout << "✗ Integrity violation detected!\n";
            return 1;
        }
    }
    else if (command == "update" && argc == 3) {
        std::string filepath = argv[2];
        try {
            if (!fileManager.containsFile(filepath)) {
                std::cout << "File not found in database. Use 'add' to add new files.\n";
                return 1;
            }
            std::string hash = FileHasher::calculateSHA256(filepath);
            fileManager.addOrUpdateEntry(filepath, hash);
            fileManager.saveDatabase();
            std::cout << "File hash updated successfully to: " << hash << std::endl;
        } catch (const std::exception& e) {
            std::cerr << "Error updating file: " << e.what() << std::endl;
            return 1;
        }
    }
    else if (command == "help") {
        printUsage();
        return 0;
    }
    else {
        std::cerr << "Error: Invalid command or incorrect number of arguments.\n\n";
        printUsage();
        return 1;
    }

    return 0;
}
