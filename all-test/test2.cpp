#include <iostream>
#include <string>
#include <regex>
using namespace std;

int main() {
    std::string txt = "maximum(protected_div(multiply(maximum(protected_div('CPU_CONFIGURATION', 'ACTUALAVAILABLETIME'), subtract('SLACKTIME', 'CPU_CONFIGURATION')), minimum(add('CPU_CONFIGURATION', 'COMMUNICATIONTIME'), maximum('WEIGHT_TASK_CATEGORY', 'MEMORY_CONFIGURATION'))), add(multiply(subtract('ACTUALAVAILABLETIME', 'SLACKTIME'), protected_div('MINEXECUTETIME', 'CURRENTLYCPU_INSTANCE')), add(add('CURRENTLYCPU_INSTANCE', 'WEIGHT_TASK_CATEGORY'), protected_div('PRICE_CONFIGURATION', 'STATICPOWER_CONFIGURATION')))), add(protected_div(add(subtract('NUMBERTASKINCLOUD', 'ACTUALAVAILABLETIME'), subtract('CURRENTLYMEMORY_INSTANCE', 'ACTUALAVAILABLETIME')), multiply(multiply('PRICE_CONFIGURATION', 'MEMORY_CONFIGURATION'), multiply('MINEXECUTETIME', 'CPU_CONFIGURATION'))), multiply(maximum(minimum('NUMBERTASKINCLOUD', 'SLACKTIME'), multiply('SLACKTIME', 'PRICE_CONFIGURATION')), maximum(maximum('WEIGHT_TASK_CATEGORY', 'WEIGHT_TASK_CATEGORY'), maximum('PRICE_CONFIGURATION', 'CPU_CONFIGURATION')))))";
    std::string to_search = "'CPU_CONFIGURATION'";
    std::string replace_with = "189.32";    

    string text = txt;
    string::size_type pos=0;
    string::size_type a=to_search.size();
    string::size_type b=replace_with.size();
    while((pos=text.find(to_search,pos))!=string::npos)
    {
        text.replace(pos,a,replace_with);
        pos+=b;
    }  
    std::cout << text << std::endl; 
    return 0;
}