#########################
# INITIAL SCRIPT
#########################
# Author: SeraphimWei
#########################
# Target: 正确打印Test.yaml
#########################

from IsLegalTree import IsLegalTree
import os

test_path = os.path.dirname(os.path.abspath(__file__)) + "/Test1.yaml"
# print("测试文件所在目录是:", test_path)

print(IsLegalTree(test_path))