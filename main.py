import ctypes
import os
import numpy as np

# Load the shared library
if os.name == 'nt':
    expression_evaluator  = ctypes.CDLL('./expression_evaluator.dll')
else:
    expression_evaluator  = ctypes.CDLL('./expression_evaluator.so')

# 设置函数参数和返回类型
expression_evaluator.evaluate_expression_from_python.argtypes = [
    ctypes.c_char_p,
    ctypes.POINTER(ctypes.c_char_p),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int
]
expression_evaluator.evaluate_expression_from_python.restype = ctypes.c_double

# 定义表达式和变量
# expr = b"minimum(subtract(3.0, 1.0), 9.0)"
# expr = b"maximum(multiply('PRICE_CONFIGURATION', 'MEMORY_CONFIGURATION'), 7.0)))";
# expr = b"maximum(protected_div(multiply(maximum(protected_div('CPU_CONFIGURATION', 'ACTUALAVAILABLETIME'), subtract('SLACKTIME', 'CPU_CONFIGURATION')), minimum(add('CPU_CONFIGURATION', 'COMMUNICATIONTIME'), maximum('WEIGHT_TASK_CATEGORY', 'MEMORY_CONFIGURATION'))), add(multiply(subtract('ACTUALAVAILABLETIME', 'SLACKTIME'), protected_div('MINEXECUTETIME', 'CURRENTLYCPU_INSTANCE')), add(add('CURRENTLYCPU_INSTANCE', 'WEIGHT_TASK_CATEGORY'), protected_div('PRICE_CONFIGURATION', 'STATICPOWER_CONFIGURATION')))), add(protected_div(add(subtract('NUMBERTASKINCLOUD', 'ACTUALAVAILABLETIME'), 10.0), multiply(multiply('PRICE_CONFIGURATION', 'MEMORY_CONFIGURATION'), 7.0)), multiply(maximum(minimum('NUMBERTASKINCLOUD', 'SLACKTIME'), 27.0), maximum(5.0, 9.0))))"; 

expr = b"add(minimum(protected_div(multiply(add(maximum(minimum('CPU_CONFIGURATION', 'CPU_CONFIGURATION'), multiply('PRICE_CONFIGURATION', 'ACTUALAVAILABLETIME')), maximum(add('NUMBERTASKINCLOUD', 'SLACKTIME'), maximum('CPU_CONFIGURATION', 'NUMBERTASKINCLOUD'))), add(protected_div('STATICPOWER_CONFIGURATION', 'CURRENTLYMEMORY_INSTANCE'), multiply('MINEXECUTETIME', 'PRICE_CONFIGURATION'))), multiply(subtract(multiply('COMMUNICATIONCOST', 'WEIGHT_TASK_CATEGORY'), protected_div('WEIGHT_TASK_CATEGORY', 'NUMBERTASKINCLOUD')), minimum(protected_div('NUMBERTASKINCLOUD', 'CPU_CONFIGURATION'), maximum('SLACKTIME', 'WEIGHT_TASK_CATEGORY')))), maximum(add(subtract(maximum('WEIGHT_TASK_CATEGORY', 'MEMORY_CONFIGURATION'), multiply('WEIGHT_TASK_CATEGORY', 'CURRENTLYCPU_INSTANCE')), minimum(add('MINEXECUTETIME', 'NUMBERTASKINCLOUD'), add('NUMBERTASKINCLOUD', 'NUMBERTASKINCLOUD'))), protected_div(subtract(maximum('MINEXECUTETIME', 'MEMORY_CONFIGURATION'), protected_div('MINEXECUTETIME', 'ACTUALAVAILABLETIME')), multiply(protected_div('PRICE_CONFIGURATION', 'COMMUNICATIONCOST'), add('MINEXECUTETIME', 'PRICE_CONFIGURATION'))))), multiply(subtract(multiply(maximum(minimum('NUMBERTASKINCLOUD', 'CURRENTLYMEMORY_INSTANCE'), subtract('PRICE_CONFIGURATION', 'COMMUNICATIONTIME')), maximum(add('NUMBERTASKINCLOUD', 'SLACKTIME'), protected_div('COMMUNICATIONCOST', 'MEMORY_CONFIGURATION'))), multiply(add(add('CURRENTLYCPU_INSTANCE', 'CURRENTLYMEMORY_INSTANCE'), maximum('CURRENTLYMEMORY_INSTANCE', 'COMMUNICATIONTIME')), protected_div(minimum('NUMBERTASKINCLOUD', 'WEIGHT_TASK_CATEGORY'), add('CURRENTLYMEMORY_INSTANCE', 'PRICE_CONFIGURATION')))), minimum(add(add(protected_div('CURRENTLYCPU_INSTANCE', 'CURRENTLYMEMORY_INSTANCE'), multiply('ACTUALAVAILABLETIME', 'NUMBERTASKINCLOUD')), subtract(subtract('COMMUNICATIONTIME', 'CURRENTLYMEMORY_INSTANCE'), minimum('CURRENTLYMEMORY_INSTANCE', 'ACTUALAVAILABLETIME'))), protected_div(add(protected_div('PRICE_CONFIGURATION', 'COMMUNICATIONCOST'), maximum('SLACKTIME', 'NUMBERTASKINCLOUD')), minimum(minimum('ACTUALAVAILABLETIME', 'PRICE_CONFIGURATION'), minimum('COMMUNICATIONTIME', 'CURRENTLYCPU_INSTANCE'))))))" 



var_names = [b"CPU_CONFIGURATION", b"ACTUALAVAILABLETIME", b"SLACKTIME", b"COMMUNICATIONTIME",
             b"WEIGHT_TASK_CATEGORY", b"MEMORY_CONFIGURATION", b"MINEXECUTETIME",
             b"CURRENTLYCPU_INSTANCE", b"PRICE_CONFIGURATION", b"STATICPOWER_CONFIGURATION",
             b"NUMBERTASKINCLOUD", b"CURRENTLYMEMORY_INSTANCE",b"COMMUNICATIONCOST"]
var_values = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0]

# 转换为 ctypes 数组
var_names_ctypes = (ctypes.c_char_p * len(var_names))(*var_names)
var_values_ctypes = (ctypes.c_double * len(var_values))(*var_values)

# 调用 C++ 函数
result = expression_evaluator.evaluate_expression_from_python(expr, var_names_ctypes, var_values_ctypes, len(var_names))
print(f"Result: {result}")