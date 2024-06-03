/*
 函数说明：对字符串中所有指定的子串进行替换
 参数：
string resource_str            //源字符串
string sub_str                //被替换子串
string new_str                //替换子串
返回值: string
 */

#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

std::string subreplace(std::string resource_str, std::string sub_str, std::string new_str)
{
    std::string dst_str = resource_str;
    std::string::size_type pos = 0;
    while((pos = dst_str.find(sub_str)) != std::string::npos)   //替换所有指定子串
    {
        dst_str.replace(pos, sub_str.length(), new_str);
    }
    return dst_str;
}

string fnd = "dataset";
string rep = "labels";
string buf = "d:/data/dataset/ii.jpg";
/// @brief 
string buff = buf.replace(buf.find(fnd), fnd.length(), rep);