#include <pybind11/pybind11.h>
#include <iostream>
#include <string>
#include <regex>
using namespace std;

namespace py = pybind11;

string replace_szx(string text, string to_search, string replace_with) {

	for (int i = 0; i < 1000000; ++i)
	{
        string text1 = text;
        string::size_type pos=0;
        string::size_type a=to_search.size();
        string::size_type b=replace_with.size();
        while((pos=text1.find(to_search,pos))!=string::npos)
        {
            // text.replace(pos,a,replace_with);
            // pos+=b;
            text1.erase(pos,a);
            text1.insert(pos,replace_with);
            pos+=b;

        }
		if (i==999999)
		{
			text=text1;
		}	
        // // std::cout << text << std::endl; // 输出：我喜欢橘子和香蕉。        
	}	
    // string::size_type pos=0;
    // string::size_type a=to_search.size();
    // string::size_type b=replace_with.size();
    // while((pos=text.find(to_search,pos))!=string::npos)
    // {
    //     text.replace(pos,a,replace_with);
    //     pos+=b;
    // }      
    return text;
}


PYBIND11_MODULE(example, m) {
	m.doc() = "pybind11 example plugin"; // optional module docstring

	m.def("replace_szx", &replace_szx, "A function that adds two numbers",
      py::arg("text"), py::arg("to_search"), py::arg("replace_with"));
}