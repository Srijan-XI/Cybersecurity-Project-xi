# Makefile for File Integrity Checker

# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -I include
LDFLAGS = -lssl -lcrypto

# Directories
SRCDIR = src
INCDIR = include
OBJDIR = obj
DATADIR = data

# Source files
SOURCES = $(wildcard $(SRCDIR)/*.cpp)
OBJECTS = $(SOURCES:$(SRCDIR)/%.cpp=$(OBJDIR)/%.o)

# Target executable
TARGET = FileIntegrityChecker

# Default target
all: $(TARGET)

# Create target executable
$(TARGET): $(OBJECTS) | $(DATADIR)
	$(CXX) $(OBJECTS) -o $@ $(LDFLAGS)

# Compile source files to object files
$(OBJDIR)/%.o: $(SRCDIR)/%.cpp | $(OBJDIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Create directories if they don't exist
$(OBJDIR):
	mkdir -p $(OBJDIR)

$(DATADIR):
	mkdir -p $(DATADIR)

# Clean build files
clean:
	rm -rf $(OBJDIR) $(TARGET)

# Clean everything including data
clean-all: clean
	rm -rf $(DATADIR)

# Install dependencies (Ubuntu/Debian)
install-deps:
	sudo apt-get update
	sudo apt-get install libssl-dev

# Install dependencies (CentOS/RHEL)
install-deps-centos:
	sudo yum install openssl-devel

# Install dependencies (macOS)
install-deps-mac:
	brew install openssl

.PHONY: all clean clean-all install-deps install-deps-centos install-deps-mac