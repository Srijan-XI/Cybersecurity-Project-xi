#ifndef FILE_MANAGER_H
#define FILE_MANAGER_H

#include <string>
#include <unordered_map>

class FileManager {
private:
    std::string dbFilePath;
    std::unordered_map<std::string, std::string> fileHashMap;

public:
    FileManager(const std::string& dbPath);

    void loadDatabase();
    void saveDatabase();

    void addOrUpdateEntry(const std::string& filepath, const std::string& hash);
    std::string getHash(const std::string& filepath);
    bool containsFile(const std::string& filepath);
};

#endif // FILE_MANAGER_H
