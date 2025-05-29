#include <iostream>
#include "scanner.hpp"

int main() {
    std::string target_dir = "../data/samples";
    std::string log_file = "../outputs/logs/scan.log";

    std::cout << "[*] Starting file scan in directory: " << target_dir << std::endl;

    Scanner scanner(target_dir, log_file);
    scanner.loadSignatures("../configs/rules.json");
    scanner.scanDirectory();

    std::cout << "[+] Scan completed. Results saved to: " << log_file << std::endl;
    return 0;
}
