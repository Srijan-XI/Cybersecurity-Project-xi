#ifndef INTEGRITY_CHECKER_H
#define INTEGRITY_CHECKER_H

#include <string>
#include "FileManager.h"

class IntegrityChecker {
private:
    FileManager& fileManager;

public:
    IntegrityChecker(FileManager& fm) : fileManager(fm) {}

    bool checkIntegrity(const std::string& filepath);
};

#endif // INTEGRITY_CHECKER_H
