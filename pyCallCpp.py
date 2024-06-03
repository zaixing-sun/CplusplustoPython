#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import importlib,sys
importlib.reload(sys)
# reload(sys)
# sys.setdefaultencoding('utf-8')
import ctypes

so = ctypes.cdll.LoadLibrary
# # g++ -o libpycallclass.so -shared -fPIC pycallclass.cpp
# lib = so("./libpycallclass.so")
# print(lib.foo(2, 4))

# # g++ -o libpycallC_replace.so -shared -fPIC pycallC_replace.cpp

text = b"maximum(protected_div(multiply(maximum(protected_div('CPU_CONFIGURATION', 'ACTUALAVAILABLETIME'), subtract('SLACKTIME', 'CPU_CONFIGURATION')), minimum(add('CPU_CONFIGURATION', 'COMMUNICATIONTIME'), maximum('WEIGHT_TASK_CATEGORY', 'MEMORY_CONFIGURATION'))), add(multiply(subtract('ACTUALAVAILABLETIME', 'SLACKTIME'), protected_div('MINEXECUTETIME', 'CURRENTLYCPU_INSTANCE')), add(add('CURRENTLYCPU_INSTANCE', 'WEIGHT_TASK_CATEGORY'), protected_div('PRICE_CONFIGURATION', 'STATICPOWER_CONFIGURATION')))), add(protected_div(add(subtract('NUMBERTASKINCLOUD', 'ACTUALAVAILABLETIME'), subtract('CURRENTLYMEMORY_INSTANCE', 'ACTUALAVAILABLETIME')), multiply(multiply('PRICE_CONFIGURATION', 'MEMORY_CONFIGURATION'), multiply('MINEXECUTETIME', 'CPU_CONFIGURATION'))), multiply(maximum(minimum('NUMBERTASKINCLOUD', 'SLACKTIME'), multiply('SLACKTIME', 'PRICE_CONFIGURATION')), maximum(maximum('WEIGHT_TASK_CATEGORY', 'WEIGHT_TASK_CATEGORY'), maximum('PRICE_CONFIGURATION', 'CPU_CONFIGURATION')))))"
to_search = b"'CPU_CONFIGURATION'"
replace_with = b"189.32"

lib = so("./libpycallC_replace.so")

lib.replace_string.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
lib.replace_string.restype = ctypes.c_char_p

print(lib.replace_string(text,to_search,replace_with))

# print(lib.replace_string(ctypes.c_char_p(text),ctypes.c_char_p(to_search),ctypes.c_char_p(replace_with)))