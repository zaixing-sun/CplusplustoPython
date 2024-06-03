#include <iostream>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>
#include <unordered_map>

using namespace std;

// Utility function to safely divide two values
double protected_div(double a, double b) {
    return b == 0.0 ? 1.0 : a / b;
}

// Function to perform the operations
double performOperation(const string &op, double a, double b) {
    if (op == "add") return a + b;
    if (op == "subtract") return a - b;
    if (op == "multiply") return a * b;
    if (op == "protected_div") return protected_div(a, b);
    if (op == "maximum") return max(a, b);
    if (op == "minimum") return min(a, b);
    return 0.0;
}

// Function to parse and evaluate the expression recursively
double evaluateExpression(const string &expr, const map<string, double> &variables, unordered_map<string, double> &cache) {
    if (cache.find(expr) != cache.end()) {
        return cache[expr];
    }

    // Remove leading and trailing whitespaces
    string trimmedExpr = expr;
    trimmedExpr.erase(0, trimmedExpr.find_first_not_of(' '));
    trimmedExpr.erase(trimmedExpr.find_last_not_of(' ') + 1);

    // Find the first open parenthesis
    size_t openPos = trimmedExpr.find('(');
    if (openPos == string::npos) {
        // If there's no open parenthesis, it's either a variable or a number
        if (variables.find(trimmedExpr) != variables.end()) {
            return variables.at(trimmedExpr);
        } else {
            return stod(trimmedExpr);
        }
    }

    // Find the corresponding close parenthesis
    size_t closePos = trimmedExpr.find_last_of(')');
    string op = trimmedExpr.substr(0, openPos);
    string innerExpr = trimmedExpr.substr(openPos + 1, closePos - openPos - 1);

    // Split the inner expression into two arguments
    int depth = 0;
    size_t splitPos = 0;
    for (size_t i = 0; i < innerExpr.length(); ++i) {
        if (innerExpr[i] == '(') depth++;
        if (innerExpr[i] == ')') depth--;
        if (innerExpr[i] == ',' && depth == 0) {
            splitPos = i;
            break;
        }
    }

    string arg1 = innerExpr.substr(0, splitPos);
    string arg2 = innerExpr.substr(splitPos + 1);

    double val1 = evaluateExpression(arg1, variables, cache);
    double val2 = evaluateExpression(arg2, variables, cache);

    double result = performOperation(op, val1, val2);
    cache[expr] = result;
    return result;
}

// Function to preprocess the expression
string preprocessExpression(const string &expr) {
    string preprocessed = expr;
    replace(preprocessed.begin(), preprocessed.end(), '\'', ' ');
    return preprocessed;
}

int main() {
    // Define the variables and their values
    map<string, double> variables = {
        {"CPU_CONFIGURATION", 1.0},
        {"ACTUALAVAILABLETIME", 2.0},
        {"SLACKTIME", 3.0},
        {"COMMUNICATIONTIME", 4.0},
        {"WEIGHT_TASK_CATEGORY", 5.0},
        {"MEMORY_CONFIGURATION", 6.0},
        {"MINEXECUTETIME", 7.0},
        {"CURRENTLYCPU_INSTANCE", 8.0},
        {"PRICE_CONFIGURATION", 9.0},
        {"STATICPOWER_CONFIGURATION", 10.0},
        {"NUMBERTASKINCLOUD", 11.0},
        {"CURRENTLYMEMORY_INSTANCE", 12.0},
        {"COMMUNICATIONCOST", 13.0}
    };

    // Define the expression
    // string expr = "minimum(subtract(3.0, 1.0), 9.0)";
    // string expr = "maximum(multiply('PRICE_CONFIGURATION', 'MEMORY_CONFIGURATION'), 7.0)))";
    string expr = "maximum(protected_div(multiply(maximum(protected_div('CPU_CONFIGURATION', 'ACTUALAVAILABLETIME'), subtract('SLACKTIME', 'CPU_CONFIGURATION')), minimum(add('CPU_CONFIGURATION', 'COMMUNICATIONTIME'), maximum('WEIGHT_TASK_CATEGORY', 'MEMORY_CONFIGURATION'))), add(multiply(subtract('ACTUALAVAILABLETIME', 'SLACKTIME'), protected_div('MINEXECUTETIME', 'CURRENTLYCPU_INSTANCE')), add(add('CURRENTLYCPU_INSTANCE', 'WEIGHT_TASK_CATEGORY'), protected_div('PRICE_CONFIGURATION', 'STATICPOWER_CONFIGURATION')))), add(protected_div(add(subtract('NUMBERTASKINCLOUD', 'ACTUALAVAILABLETIME'), 10.0), multiply(multiply('PRICE_CONFIGURATION', 'MEMORY_CONFIGURATION'), 7.0)), multiply(maximum(minimum('NUMBERTASKINCLOUD', 'SLACKTIME'), 27.0), maximum(5.0, 9.0))))";
    // string expr = "add(minimum(protected_div(multiply(add(maximum(minimum('CPU_CONFIGURATION', 'CPU_CONFIGURATION'), multiply('PRICE_CONFIGURATION', 'ACTUALAVAILABLETIME')), maximum(add('NUMBERTASKINCLOUD', 'SLACKTIME'), maximum('CPU_CONFIGURATION', 'NUMBERTASKINCLOUD'))), add(protected_div('STATICPOWER_CONFIGURATION', 'CURRENTLYMEMORY_INSTANCE'), multiply('MINEXECUTETIME', 'PRICE_CONFIGURATION'))), multiply(subtract(multiply('COMMUNICATIONCOST', 'WEIGHT_TASK_CATEGORY'), protected_div('WEIGHT_TASK_CATEGORY', 'NUMBERTASKINCLOUD')), minimum(protected_div('NUMBERTASKINCLOUD', 'CPU_CONFIGURATION'), maximum('SLACKTIME', 'WEIGHT_TASK_CATEGORY')))), maximum(add(subtract(maximum('WEIGHT_TASK_CATEGORY', 'MEMORY_CONFIGURATION'), multiply('WEIGHT_TASK_CATEGORY', 'CURRENTLYCPU_INSTANCE')), minimum(add('MINEXECUTETIME', 'NUMBERTASKINCLOUD'), add('NUMBERTASKINCLOUD', 'NUMBERTASKINCLOUD'))), protected_div(subtract(maximum('MINEXECUTETIME', 'MEMORY_CONFIGURATION'), protected_div('MINEXECUTETIME', 'ACTUALAVAILABLETIME')), multiply(protected_div('PRICE_CONFIGURATION', 'COMMUNICATIONCOST'), add('MINEXECUTETIME', 'PRICE_CONFIGURATION'))))), multiply(subtract(multiply(maximum(minimum('NUMBERTASKINCLOUD', 'CURRENTLYMEMORY_INSTANCE'), subtract('PRICE_CONFIGURATION', 'COMMUNICATIONTIME')), maximum(add('NUMBERTASKINCLOUD', 'SLACKTIME'), protected_div('COMMUNICATIONCOST', 'MEMORY_CONFIGURATION'))), multiply(add(add('CURRENTLYCPU_INSTANCE', 'CURRENTLYMEMORY_INSTANCE'), maximum('CURRENTLYMEMORY_INSTANCE', 'COMMUNICATIONTIME')), protected_div(minimum('NUMBERTASKINCLOUD', 'WEIGHT_TASK_CATEGORY'), add('CURRENTLYMEMORY_INSTANCE', 'PRICE_CONFIGURATION')))), minimum(add(add(protected_div('CURRENTLYCPU_INSTANCE', 'CURRENTLYMEMORY_INSTANCE'), multiply('ACTUALAVAILABLETIME', 'NUMBERTASKINCLOUD')), subtract(subtract('COMMUNICATIONTIME', 'CURRENTLYMEMORY_INSTANCE'), minimum('CURRENTLYMEMORY_INSTANCE', 'ACTUALAVAILABLETIME'))), protected_div(add(protected_div('PRICE_CONFIGURATION', 'COMMUNICATIONCOST'), maximum('SLACKTIME', 'NUMBERTASKINCLOUD')), minimum(minimum('ACTUALAVAILABLETIME', 'PRICE_CONFIGURATION'), minimum('COMMUNICATIONTIME', 'CURRENTLYCPU_INSTANCE'))))))";
    // Preprocess the expression
    string preprocessedExpr = preprocessExpression(expr);

    // Cache for intermediate results
    unordered_map<string, double> cache;

    // Evaluate the expression
    double result = evaluateExpression(preprocessedExpr, variables, cache);

    // Output the result
    cout << "Result: " << result << endl;

    return 0;
}
