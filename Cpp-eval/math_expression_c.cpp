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

// Function to parse and evaluate the expression
double evaluateExpression(const string &expr, const map<string, double> &variables) {
    stack<double> values;
    stack<string> ops;
    istringstream iss(expr);
    string token;

    while (iss >> token) {
        if (variables.find(token) != variables.end()) {
            values.push(variables.at(token));
        } else if (token == "add" || token == "subtract" || token == "multiply" || token == "protected_div" || token == "maximum" || token == "minimum") {
            ops.push(token);
        } else if (token == ")") {
            while (!ops.empty() && ops.top() != "(") {
                string op = ops.top();
                ops.pop();
                double b = values.top();
                values.pop();
                double a = values.top();
                values.pop();
                values.push(performOperation(op, a, b));
            }
            if (!ops.empty() && ops.top() == "(") {
                ops.pop();
            }
        } else if (token == "(") {
            ops.push(token);
        } else {
            try {
                values.push(stod(token));
            } catch (invalid_argument &) {
                cerr << "Invalid token: " << token << endl;
                return 0.0;
            }
        }
    }

    while (!ops.empty()) {
        string op = ops.top();
        ops.pop();
        double b = values.top();
        values.pop();
        double a = values.top();
        values.pop();
        values.push(performOperation(op, a, b));
    }

    return values.top();
}

// Function to replace special characters with spaces
string preprocessExpression(const string &expr) {
    string preprocessed = expr;
    replace(preprocessed.begin(), preprocessed.end(), '(', ' ');
    replace(preprocessed.begin(), preprocessed.end(), ')', ' ');
    replace(preprocessed.begin(), preprocessed.end(), '\'', ' ');
    replace(preprocessed.begin(), preprocessed.end(), ',', ' ');
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
        {"CURRENTLYMEMORY_INSTANCE", 12.0}
    };

    // Define the expression
    // string expr = "maximum(protected_div(multiply(maximum(protected_div('CPU_CONFIGURATION', 'ACTUALAVAILABLETIME'), subtract('SLACKTIME', 'CPU_CONFIGURATION')), minimum(add('CPU_CONFIGURATION', 'COMMUNICATIONTIME'), maximum('WEIGHT_TASK_CATEGORY', 'MEMORY_CONFIGURATION'))), add(multiply(subtract('ACTUALAVAILABLETIME', 'SLACKTIME'), protected_div('MINEXECUTETIME', 'CURRENTLYCPU_INSTANCE')), add(add('CURRENTLYCPU_INSTANCE', 'WEIGHT_TASK_CATEGORY'), protected_div('PRICE_CONFIGURATION', 'STATICPOWER_CONFIGURATION')))), add(protected_div(add(subtract('NUMBERTASKINCLOUD', 'ACTUALAVAILABLETIME'), 10.0), multiply(multiply('PRICE_CONFIGURATION', 'MEMORY_CONFIGURATION'), 7.0)), multiply(maximum(minimum('NUMBERTASKINCLOUD', 'SLACKTIME'), 27.0), maximum(5.0, 9.0))))";
    string expr = "minimum(subtract('SLACKTIME', 'CPU_CONFIGURATION'), 'PRICE_CONFIGURATION')";
    // Preprocess the expression
    string preprocessedExpr = preprocessExpression(expr);

    // Evaluate the expression
    double result = evaluateExpression(preprocessedExpr, variables);

    // Output the result
    cout << "Result:= " << result << endl;

    return 0;
}
