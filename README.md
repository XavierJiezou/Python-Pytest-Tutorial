# Python-Pytest-Tutorial

## Introduction

Pytest 是一个非常成熟 Python 单元测试框架。比 unitest 灵活，且简单上手。

什么是单元测试？针对软件的最小单位（函数或方法）进行正确性的检测测试。

Pytest 市场占比较高于 unittest。

单元测试框架主要做什么？

1. 测试发现：从多个文件里面去找我们的测试用例
2. 测试执行：按照一定的顺序和规则去执行，并生成结果
3. 测试判断：通过断言判断预期结果和实际结果的差异
4. 测试报告：统计测试进度、耗时和通过率等，并生成测试报告

pytest 还可以和 selenium, requests, appium 结合实现web自动化, 接口自动化, 和app自动化。

pytest 还可以实现测试用例的跳过和失败用例的重试。

pytest可以和allure生成美观的测试报告。

pytest 还可以和jenkins持续集成。

## 插件

- pytest-html：生成html格式的自动化测试报告
- pytest-xdist：测试用例的分布式执行，多CPU，多进程
- pytest-ordering：改变测试用例的执行顺序
- pytest-rerunfailures：用例失败后重跑
- allure-pytest：生成美观的测试报告

## 约束

1. py文件名必须以test_开发或_test结尾
2. 测试类必须以Test开头，并且不能有init方法
3. 测试方法必须test开头

## 运行

1. 主函数模式
   - 运行所有：pytest.main()
   - 指定模块：pytest.main(['-vs', 'test_xxx.py'])
   - 指定目录：pytest.main(['-vs', './xxx/'])
   - 指定nodeid：目录+模块+分隔符（::）+类名+分隔符（::）+方法名
2. 命令行模式
3. 读取pytest.ini配置文件来运行【推荐】
   - 一般放在项目根目录
   - 编码必须是ANSI
   - 作用：改变pytest默认行为
   - 运行规则：主函数或命令行都会自动读取该配置文件

参数详解：

- -s：输出调试信息，包括print()函数的打印信息
- -v：显示更详细的信息
- -vs：-s 和 -v 参数的结合
- -n：支持多线程或者分布式运行测试用例（要安装pytest-xdist）
- --reruns <nums>：重新执行失败的用例
- -x：只要有一个错，就停止
- --maxfail=2：只要有2个错就停止
- -k：字符匹配，只执行函数名或类名匹配的用例

## 执行顺序

unittest：ascll 码的大小来执行
pytest：从上到下
