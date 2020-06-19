#!/user/bin/python
#!-*- coding:utf-8 -*-
import pytest
<<<<<<< HEAD
import random
=======
from time import sleep
>>>>>>> origin/master
def add(a,b):
    return a+b
def zhang(a,b):
    return a-b
def lu(a,b):
    return a*b
def sheng(a,b):
    return a/b
class Testcase(object):
    @pytest.mark.run_these_please
    def test_one(self):
        print("\n正在执行-----test_one")
        assert add(1,2) == 3    #add 是上面函数的名称
    @pytest.mark.run_these_please
    def test_two(self):
        print("正在执行-----test_two")
        assert zhang(1,2) == -1
        assert zhang(3,2) == 1    #哈哈
    def test_three(self):
        print("正在执行-----test_three")
        sleep(1.0)
        assert lu(1,2) == 2
    def test_thour(self):
        print("正在执行-----test_thour")
        assert sheng(6,2) == 3
<<<<<<< HEAD
# if __name__ == "__main__":
#     pytest.main(["-s","test_xuexi.py"])
=======
if __name__ == "__main__":
    pytest.main(["-s",'-v',"test_xuexi.py"])#运行文件
    # pytest.main(['--collect-only'])    #  已运行的全部用例情况
    # pytest.main(['-k','one or two','--collect-only','test_xuexi.py'])  #希望要运行用例的情况
    # pytest.main(['-k', 'one or two','test_xuexi.py']) #指定运行用例
    # pytest.main(['-v', '-k','one or two', '--collect-only'])  #详细的要运行用例的情况
    # pytest.main(['-v','-m','run_these_please',"test_xuexi.py"])  #打标记，只执行带有标记的用例配合pytest.main.mark.标记名使用
                                                                   #也可以使用多个标记名如：-m "标记名1 and 标记名2"
                                                                   #或-m "标记名1 and not 标记名2" 过滤掉标记名2的用例
                                                                   #使用-m "标记名1 or 标记名2"选中所有的用例运行
    # pytest.main(['-x','test_xuexi.py'])    #遇到失败的测试用例，当前停止
    # pytest.main(['--tb=no','test_xuexi.py'])   #信息回溯
    # pytest.main(['--maxfail=1','test_xuexi.py'])   # 遇到失败的测试用例，全局停止，后面的数字代表可以遇到几个失败的测试用例
    # pytest.main(['--maxfail=2', '--tb=no','test_xuexi.py'])  #错误堆栈回溯
    # pytest.main(['-l', 'test_xuexi.py'])    #失败后，输出函数局部变量和全局变量的值
    # pytest.main(['--tb=no', 'test_xuexi.py']) #信息回溯，输出详细的失败原因，三个参数：short、line、no
    # pytest.main(['--tb=line', 'test_xuexi.py'])  # 告诉错误位置，可以发现他们失败的共性
    # pytest.main(['--tb=short', 'test_xuexi.py'])    #比前两种更详细，还有三种模式可选：1、--tb=long:信息最详细
    # pytest.main(['--tb=long', 'test_xuexi.py'])            #2、--tb=auto  默认值，多个用例失败，仅打印最后一个和第一个
    # pytest.main(['--tb=auto', 'test_xuexi.py'])            #3、--tb=native只输出python标准库的回溯信息
    # pytest.main(['--tb=nativa', 'test_xuexi.py'])
    # pytest.main(['--durations=0', 'test_xuexi.py'])  #显示测试用例的call、setup、teardown的耗时
    
>>>>>>> origin/master


# import requests
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
# r = requests.get("https://wwww.baidu.com",headers=headers)
# r.content.decode('utf-8')    #指定解码格式为utf - 8
# print(r.content.decode("utf-8"))
# try:
#     pass
# except:
#     pass
# else:    #try和except都没有才执行else语句
#     pass
# finally:
<<<<<<< HEAD
#     print(1)
=======
#     print(1)  #无论上面结果如何都执行  finally语句


import pytest
>>>>>>> origin/master
