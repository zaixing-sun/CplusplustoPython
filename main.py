import ctypes
import os
import numpy as np

# Load the shared library
if os.name == 'nt':
    lib = ctypes.CDLL('./math_expression.dll')
else:
    lib = ctypes.CDLL('./libmath_expression.so')

# Define the argument and return types of the C++ function
lib.evaluate_expression.argtypes = [
    ctypes.c_char_p,         # Expression as a string
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'),  # Values as a double array
    ctypes.POINTER(ctypes.c_char_p),  # Keys as a string array
    ctypes.c_int             # Length of the arrays
]
lib.evaluate_expression.restype = ctypes.c_double

# Define the expression and variables
expression = b"maximum(protected_div(multiply(maximum(protected_div('CPU_CONFIGURATION', 'ACTUALAVAILABLETIME'), subtract('SLACKTIME', 'CPU_CONFIGURATION')), minimum(add('CPU_CONFIGURATION', 'COMMUNICATIONTIME'), maximum('WEIGHT_TASK_CATEGORY', 'MEMORY_CONFIGURATION'))), add(multiply(subtract('ACTUALAVAILABLETIME', 'SLACKTIME'), protected_div('MINEXECUTETIME', 'CURRENTLYCPU_INSTANCE')), add(add('CURRENTLYCPU_INSTANCE', 'WEIGHT_TASK_CATEGORY'), protected_div('PRICE_CONFIGURATION', 'STATICPOWER_CONFIGURATION')))), add(protected_div(add(subtract('NUMBERTASKINCLOUD', 'ACTUALAVAILABLETIME'), subtract('CURRENTLYMEMORY_INSTANCE', 'ACTUALAVAILABLETIME')), multiply(multiply('PRICE_CONFIGURATION', 'MEMORY_CONFIGURATION'), multiply('MINEXECUTETIME', 'CPU_CONFIGURATION'))), multiply(maximum(minimum('NUMBERTASKINCLOUD', 'SLACKTIME'), multiply('SLACKTIME', 'PRICE_CONFIGURATION')), maximum(maximum('WEIGHT_TASK_CATEGORY', 'WEIGHT_TASK_CATEGORY'), maximum('PRICE_CONFIGURATION', 'CPU_CONFIGURATION')))))"
variables = {
    "CPU_CONFIGURATION": 2.0,
    "ACTUALAVAILABLETIME": 3.0,
    "SLACKTIME": 1.0,
    "COMMUNICATIONTIME": 4.0,
    "WEIGHT_TASK_CATEGORY": 5.0,
    "MEMORY_CONFIGURATION": 6.0,
    "MINEXECUTETIME": 7.0,
    "CURRENTLYCPU_INSTANCE": 8.0,
    "PRICE_CONFIGURATION": 9.0,
    "STATICPOWER_CONFIGURATION": 10.0,
    "NUMBERTASKINCLOUD": 11.0,
    "CURRENTLYMEMORY_INSTANCE": 12.0
}

# Prepare the keys and values for passing to the C++ function
keys = (ctypes.c_char_p * len(variables))()
values = np.zeros(len(variables), dtype=np.float64)
for i, (key, value) in enumerate(variables.items()):
    keys[i] = key.encode('utf-8')
    values[i] = value

# Call the C++ function
result = lib.evaluate_expression(expression, values, keys, len(variables))
print(f"Result: {result}")
