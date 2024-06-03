#include <iostream>
#include <map>
#include <stack>
#include <string>
#include <sstream>
#include <algorithm>

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
double evaluateExpression(const string &expr, const map<string, double> &variables) {
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

    double val1 = evaluateExpression(arg1, variables);
    double val2 = evaluateExpression(arg2, variables);

    return performOperation(op, val1, val2);
}

// Function to preprocess the expression
string preprocessExpression(const string &expr) {
    string preprocessed = expr;
    replace(preprocessed.begin(), preprocessed.end(), '\'', ' ');
    return preprocessed;
}

extern "C" double evaluate_expression_from_python(const char* expr, const char** var_names, const double* var_values, int var_count) {
    map<string, double> variables;
    for (int i = 0; i < var_count; ++i) {
        variables[var_names[i]] = var_values[i];
    }

    string expression = expr;
    string preprocessedExpr = preprocessExpression(expression);
    return evaluateExpression(preprocessedExpr, variables);
}
