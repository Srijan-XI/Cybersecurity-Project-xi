#include "FileHasher.h"
#include <openssl/sha.h>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <vector>

std::string FileHasher::calculateSHA256(const std::string& filepath) {
    std::ifstream file(filepath, std::ios::binary);
    if (!file) {
        throw std::runtime_error("Cannot open file: " + filepath);
    }

    SHA256_CTX sha256;
    SHA256_Init(&sha256);

    const size_t buffer_size = 32768;
    std::vector<char> buffer(buffer_size);

    while (file.good()) {
        file.read(buffer.data(), buffer_size);
        SHA256_Update(&sha256, buffer.data(), file.gcount());
    }

    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_Final(hash, &sha256);

    std::stringstream ss;
    for (int i = 0; i < SHA256_DIGEST_LENGTH; ++i) {
        ss << std::hex << std::setw(2) << std::setfill('0') << (int)hash[i];
    }

    return ss.str();
}
