#include <iostream>
#include <cstring>
#include <map>
#include <stdexcept>
#include <sstream>
#include <string>

extern "C" {

// Define mathematical functions
double maximum(double a, double b) {
    return (a > b) ? a : b;
}

double minimum(double a, double b) {
    return (a < b) ? a : b;
}

double protected_div(double a, double b) {
    if (b == 0) {
        return 1;
    }
    return a / b;
}

double evaluate(const std::string& expression, const std::map<std::string, double>& variables);

double parse_and_evaluate(std::istringstream& iss, const std::map<std::string, double>& variables) {
    std::string token;
    iss >> token;

    if (token == "maximum") {
        double a = parse_and_evaluate(iss, variables);
        double b = parse_and_evaluate(iss, variables);
        return maximum(a, b);
    } else if (token == "minimum") {
        double a = parse_and_evaluate(iss, variables);
        double b = parse_and_evaluate(iss, variables);
        return minimum(a, b);
    } else if (token == "protected_div") {
        double a = parse_and_evaluate(iss, variables);
        double b = parse_and_evaluate(iss, variables);
        return protected_div(a, b);
    } else if (token == "add") {
        double a = parse_and_evaluate(iss, variables);
        double b = parse_and_evaluate(iss, variables);
        return a + b;
    } else if (token == "subtract") {
        double a = parse_and_evaluate(iss, variables);
        double b = parse_and_evaluate(iss, variables);
        return a - b;
    } else if (token == "multiply") {
        double a = parse_and_evaluate(iss, variables);
        double b = parse_and_evaluate(iss, variables);
        return a * b;
    } else {
        // Token is a variable
        if (variables.find(token) != variables.end()) {
            return variables.at(token);
        } else {
            throw std::runtime_error("Unknown variable: " + token);
        }
    }
}

double evaluate(const std::string& expression, const std::map<std::string, double>& variables) {
    std::istringstream iss(expression);
    return parse_and_evaluate(iss, variables);
}

// Expose the evaluate function to be callable from Python
double evaluate_expression(const char* expression, const double* values, const char** keys, int length) {
    std::map<std::string, double> variables;
    for (int i = 0; i < length; ++i) {
        variables[keys[i]] = values[i];
    }
    return evaluate(expression, variables);
}

}
