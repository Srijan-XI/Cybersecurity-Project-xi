#ifndef URL_PARSER_H
#define URL_PARSER_H

#include <string>
#include <tuple>

class URLParser {
public:
    explicit URLParser(const std::string& url);
    
    std::string getScheme() const;
    std::string getHost() const;
    std::string getPath() const;
    std::string getQuery() const;
    
    // Basic heuristic: Detect suspicious characters or patterns
    bool isSuspicious() const;

private:
    std::string scheme_;
    std::string host_;
    std::string path_;
    std::string query_;
    
    void parseURL(const std::string& url);
};

#endif // URL_PARSER_H
