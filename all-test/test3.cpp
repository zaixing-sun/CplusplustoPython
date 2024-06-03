#include <iostream>
#include <string>
#include <chrono>
#include <regex>

using namespace std;



int main()
{
    std::string txt = "maximum(protected_div(multiply(maximum(protected_div('CPU_CONFIGURATION', 'ACTUALAVAILABLETIME'), subtract('SLACKTIME', 'CPU_CONFIGURATION')), minimum(add('CPU_CONFIGURATION', 'COMMUNICATIONTIME'), maximum('WEIGHT_TASK_CATEGORY', 'MEMORY_CONFIGURATION'))), add(multiply(subtract('ACTUALAVAILABLETIME', 'SLACKTIME'), protected_div('MINEXECUTETIME', 'CURRENTLYCPU_INSTANCE')), add(add('CURRENTLYCPU_INSTANCE', 'WEIGHT_TASK_CATEGORY'), protected_div('PRICE_CONFIGURATION', 'STATICPOWER_CONFIGURATION')))), add(protected_div(add(subtract('NUMBERTASKINCLOUD', 'ACTUALAVAILABLETIME'), subtract('CURRENTLYMEMORY_INSTANCE', 'ACTUALAVAILABLETIME')), multiply(multiply('PRICE_CONFIGURATION', 'MEMORY_CONFIGURATION'), multiply('MINEXECUTETIME', 'CPU_CONFIGURATION'))), multiply(maximum(minimum('NUMBERTASKINCLOUD', 'SLACKTIME'), multiply('SLACKTIME', 'PRICE_CONFIGURATION')), maximum(maximum('WEIGHT_TASK_CATEGORY', 'WEIGHT_TASK_CATEGORY'), maximum('PRICE_CONFIGURATION', 'CPU_CONFIGURATION')))))";
    std::string to_search = "'CPU_CONFIGURATION'";
    std::string replace_with = "189.32";


    // // 使用正则表达式进行替换
	// auto beforeTime1 = std::chrono::steady_clock::now();
	
	// for (int i = 0; i < 100000; ++i)
	// {
    //     string text = txt;
    //     std::regex expr(to_search);
    //     std::string text_with_regex = std::regex_replace(text, expr, replace_with);
	// }

	// auto afterTime1 = std::chrono::steady_clock::now();

	// std::cout << "总耗时:" << std::endl;
    
	// double duration_second1 = std::chrono::duration<double>(afterTime1 - beforeTime1).count();
	// std::cout << duration_second1 << "秒" << std::endl;

    // 使用 replace 进行替换
	auto beforeTime2 = std::chrono::steady_clock::now();
	
	for (int i = 0; i < 1000000; ++i)
	{
        string text = txt;
        string::size_type pos=0;
        string::size_type a=to_search.size();
        string::size_type b=replace_with.size();
        while((pos=text.find(to_search,pos))!=string::npos)
        {
            text.replace(pos,a,replace_with);
            pos+=b;
        }

        // // std::cout << text << std::endl; // 输出：我喜欢橘子和香蕉。        
	}

	auto afterTime2 = std::chrono::steady_clock::now();

	std::cout << "总耗时:" << std::endl;
    
	double duration_second2 = std::chrono::duration<double>(afterTime2 - beforeTime2).count();
	std::cout << duration_second2 << "秒" << std::endl;

    // 使用 erase 进行替换
	auto beforeTime3 = std::chrono::steady_clock::now();
	
	for (int i = 0; i < 1000000; ++i)
	{
        string text = txt;
        string::size_type pos=0;
        string::size_type a=to_search.size();
        string::size_type b=replace_with.size();
        while((pos=text.find(to_search,pos))!=string::npos)
        {
            // text.replace(pos,a,replace_with);
            // pos+=b;
            text.erase(pos,a);
            text.insert(pos,replace_with);
            pos+=b;

        }

        // // std::cout << text << std::endl; // 输出：我喜欢橘子和香蕉。        
	}

	auto afterTime3 = std::chrono::steady_clock::now();

	std::cout << "总耗时:" << std::endl;
    
	double duration_second3 = std::chrono::duration<double>(afterTime3 - beforeTime3).count();
	std::cout << duration_second3 << "秒" << std::endl;


        // 总耗时:
        // 461.226秒
        // 总耗时:
        // 1.4145秒
        // 总耗时:
        // 1.55591秒    

}


