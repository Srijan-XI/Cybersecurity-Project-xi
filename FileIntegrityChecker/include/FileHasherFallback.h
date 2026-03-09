#ifndef FILE_HASHER_FALLBACK_H
#define FILE_HASHER_FALLBACK_H

#include <string>

class FileHasherFallback {
public:
    // Simple hash function for testing (not cryptographically secure)
    static std::string calculateSimpleHash(const std::string& filepath);
    
    // CRC32 hash function (better than simple hash, still not cryptographically secure)
    static std::string calculateCRC32(const std::string& filepath);
};

#endif // FILE_HASHER_FALLBACK_H