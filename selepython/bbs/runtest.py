'''
    加载测试用例并执行测试用例
'''

import unittest
import HTMLTestRunner as hr

# 加载用例
# TestLoader
loader = unittest.TestLoader()
# discover()方法
suite = loader.discover(start_dir="./test_case", pattern="test*.py")
# print(suite)

# 执行用例
# TestRunner unittest自带
# HTMLTestRunner 扩展，可以生成一个HTML报告
# 需要将HTMLTestRunner.py放入到C:\Python36\Lib中
# 生成HTMLTestRunner
#   1.需要一个打开的文件对象
#   2.报告的标题
#   3.报告的描述（详细信息）
report = open("./report/20200630_report.html", "wb")
html_test_runner = hr.HTMLTestRunner(report, title="bbs测试报告", description="第一轮测试用例执行结果")
# 执行用例
html_test_runner.run(suite)

report.close()