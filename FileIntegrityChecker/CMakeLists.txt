cmake_minimum_required(VERSION 3.16)
project(FileIntegrityChecker)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find OpenSSL
find_package(OpenSSL REQUIRED)

# Include directories
include_directories(include)

# Create executable
add_executable(FileIntegrityChecker
    src/main.cpp
    src/FileHasher.cpp
    src/FileManager.cpp
    src/IntegrityChecker.cpp
)

# Link OpenSSL libraries
target_link_libraries(FileIntegrityChecker OpenSSL::SSL OpenSSL::Crypto)

# Ensure data directory exists
file(MAKE_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/data)