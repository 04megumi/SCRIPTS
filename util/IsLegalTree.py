#######################
# author: SeraphimWei
#######################

# 描述：
#     该函数用于验证给定路径下的文件(.yml)内容是否符合合法的树形结构格式。
#     树形结构格式指的是每一层的目录或文件按照层级缩进的方式排列，且每个目录或文件名称必须符合一定规则。
#     该函数将根据文件的内容检查是否符合这种树形结构的规则，并返回是否为合法树的布尔值。
#     用yaml格式保存的树结构通常使用缩进来表示目录结构。
#
# 接口：IsLegalTree(path)
#     该接口用于验证路径下的文件内容是否为合法树结构。
#
# 参数：
#     path (str): 需要检查的文件路径。该路径应指向一个包含树形结构描述的yaml文件。
#                 文件内容应该符合预定义的树形结构规范（例如每行表示目录或文件，使用缩进表示层级关系）。
#
# 返回值：
#     bool: 如果文件内容符合树形结构规范，返回 True；否则返回 False。
#
# 异常：
#     - 如果给定的路径无效或文件不可访问，函数将抛出 `FileNotFoundError` 异常。
#     - 如果文件内容无法解析为合法树结构，函数将返回 False。
#
# 示例：
#     IsLegalTree("project_structure.yml")
#     # 假设 "project_structure.yml" 文件内容如下：
#     # SCRIPTS:
#     #   util:
#     #     - test.py
#     #     - IsLegalTree.py
#     #     - tests: null
#     #   dic:
#     #     - test.py
#     #     - tests: null
#     #   README.md: null
#     #   dev.md: null
#     # 返回值：True
##
# TODO:
#     - 测试   
#######################

import yaml
import os

def IsLegalTree(path: str) -> bool:
    """
    检查给定路径下的 YAML 文件内容是否符合合法的树形结构格式。
    
    :param path: 需要检查的文件路径，文件内容应该是符合树形结构描述规范的 YAML 文件。
    :return: 如果文件内容符合合法的树形结构，返回 True；否则返回 False。

    :raises FileNotFoundError: 如果文件路径无效或文件不可访问时抛出异常。
    :raises ValueError: 如果 YAML 文件的内容不符合树形结构规则时抛出异常。
    """
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return False

    try:
        with open(path, 'r') as file:
            # 打开并读取 YAML 文件
            content = yaml.safe_load(file)

            # print(content)

    except FileNotFoundError:
        print(f"File not Found: {path}")
        return False
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return False


