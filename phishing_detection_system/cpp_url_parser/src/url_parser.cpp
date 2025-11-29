#include "url_parser.h"
#include <regex>
#include <iostream>

URLParser::URLParser(const std::string& url) {
    parseURL(url);
}

void URLParser::parseURL(const std::string& url) {
    // Simple regex for URL parsing: scheme://host/path?query
    std::regex url_regex(R"((https?)://([^/\r\n]+)([^?\r\n]*)(\??[^#\r\n]*)?)",
                         std::regex::icase);
    std::smatch match;
    if (std::regex_match(url, match, url_regex)) {
        scheme_ = match[1];
        host_ = match[2];
        path_ = match[3];
        query_ = match[4];
    } else {
        // Handle invalid URL format (fallback)
        scheme_ = "";
        host_ = "";
        path_ = "";
        query_ = "";
    }
}

std::string URLParser::getScheme() const { return scheme_; }
std::string URLParser::getHost() const { return host_; }
std::string URLParser::getPath() const { return path_; }
std::string URLParser::getQuery() const { return query_; }

bool URLParser::isSuspicious() const {
    // Example heuristic: suspicious if host contains IP instead of domain or has '@'
    if (host_.find('@') != std::string::npos) return true;
    
    std::regex ip_regex(R"((\d{1,3}\.){3}\d{1,3})");
    if (std::regex_search(host_, ip_regex)) return true;

    // Check for unusual characters in path or query
    if (path_.find("..") != std::string::npos) return true;

    return false;
}
