#include <iostream>
#include <print>
using namespace std;

/// @brief 主函数: 程序入口
/// @param argc 命令行参数个数
/// @param argv 命令行参数数组
/// @return 返回值: 错误码
int main(int argc, char** argv) {
    // 打印命令行参数
    for (int i = 0; i < argc; i++) {
        println("argv[{}]: {}", i, argv[i]);
    }

    // 打印 hello world
    println("Hello, World!");
}
