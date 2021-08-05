import  unittest
from common import HTMLTestRunner_cn
casePath='D:\BLSJ_AUTO\\case' # 用例路径
rule='test*.py'

discover =unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)
reportPath='D:\\BLSJ_AUTO\\report\\'+'result.html'
fp=open(reportPath,'wb')


# discover =unittest.defaultTestLoader.discover()




runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                       title='报告的名称',
                                       description='描述你的报告干什么用的',
                                          retry=1)

runner.run(discover)

fp.close()
