//g++ -o libpycallC_replace.so -shared -fPIC pycallC_replace.cpp
#include <iostream>
#include <string>
#include <regex>
#include <chrono>
using namespace std;

class TestLib
{
    public:
        string replace_szx(string text, string to_search, string replace_with);
};
string TestLib::replace_szx(string text, string to_search, string replace_with) {

	auto beforeTime2 = std::chrono::steady_clock::now();
	
	for (int i = 0; i < 1000000; ++i)
	{
        string txt = text;
        string::size_type pos=0;
        string::size_type a=to_search.size();
        string::size_type b=replace_with.size();
        while((pos=txt.find(to_search,pos))!=string::npos)
        {
            txt.replace(pos,a,replace_with);
            pos+=b;
        }
		if (i==999999)
		{
			text=txt;
		}	        
	}

	auto afterTime2 = std::chrono::steady_clock::now();

	std::cout << "总耗时:" << std::endl;
    
	double duration_second2 = std::chrono::duration<double>(afterTime2 - beforeTime2).count();
	std::cout << duration_second2 << "秒" << std::endl;

    std::cout << text << std::endl;    
    return text;
}

extern "C" {
    TestLib obj;
    char* replace_string(char* text, char* to_search, char* replace_with) {
        char *text_C = text;
        char *to_search_C = to_search;
        char *replace_with_C = replace_with;
        string text_S = text_C;
        string to_search_S = to_search_C;
        string replace_with_S = replace_with_C;
        string result = obj.replace_szx(text_S,to_search_S,replace_with_S);
        return strdup(result.c_str());
        // return obj.replace_szx(text_S,to_search_S,replace_with_S);
    }
}

