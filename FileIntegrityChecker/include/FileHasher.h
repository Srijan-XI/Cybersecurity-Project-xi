#ifndef FILE_HASHER_H
#define FILE_HASHER_H

#include <string>

class FileHasher {
public:
    // Calculate SHA-256 hash of the given file
    static std::string calculateSHA256(const std::string& filepath);
};

#endif // FILE_HASHER_H
