# modular packing 模块打包,一般是setup.py文件

# pip install setuptools
# pip install wheel
# 模块的定义与使用

import setuptools # 模块导入
import setuptools # 模块导入
setuptools.setup( # 定义打包配置
    name='yootk.common', # 打包文件名称
    version='0.0.1', # 模块版本编号
    author='李兴华', # 模块作者
    url='http://www.yootk.com', # 模块网站
    description='Get Yootk Information.' , # 短描述信息
    long_description='提供图书类以及消息处理函数',   # 长描述信息
    packages=setuptools.find_packages('src'),  # 源代码目录
    package_dir={'': 'src'},  # 打包目录
    package_data={ # 打包文件类型
        '': ['*.txt', '*.info', '*.properties'], # 配置模块包含文件后缀类型配置
        '': ['data/*.*'], # 包含data文件夹中的所有文件
    },
    exclude=['*.test', '*.test.*', 'test.*', 'test'], # 排除所有测试包
    classifiers=[ # 程序使用环境
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)


#终端运行 python setup.py bdist_wheel
# 打包完成后，开发者可以使用开发包并通过pip安装
# 安装包位置：E:\summer_study\python开发\programe\pythonProject\python环境管理\dist\yootk.common-0.0.1-py3-none-any.whl
# 安装开发包：pip install E:\summer_study\python开发\programe\pythonProject\python环境管理\dist\yootk.common-0.0.1-py3-none-any.whl
# 接着 python setup.py install



# PS E:\summer_study\python开发\programe\pythonProject> python setup.py bdist_wheel
# D:\python_install_file\python.exe: can't open file 'E:\\summer_study\\python开发\\programe\\pythonProject\\setup.py': [Errno 2] No such file or directory
# PS E:\summer_study\python开发\programe\pythonProject> 
# 原来我的setup.py在python环境管理/setup.py
# PS E:\summer_study\python开发\programe\pythonProject> cd .\python环境管理\      
# PS E:\summer_study\python开发\programe\pythonProject\python环境管理> python setup.py bdist_wheel

# PS E:\summer_study\python开发\programe\pythonProject> python setup.py bdist_wheel
# D:\python_install_file\python.exe: can't open file 'E:\\summer_study\\python开发\\programe\\pythonProject\\setup.py': [Errno 2] No such file or directory
# PS E:\summer_study\python开发\programe\pythonProject> cd .\python环境管理\      
# PS E:\summer_study\python开发\programe\pythonProject\python环境管理> python setup.py bdist_wheel
# running bdist_wheel
# error: error in 'egg_base' option: '模块的定义与使用' does not exist or is not a directory
# PS E:\summer_study\python开发\programe\pythonProject\python环境管理> python setup.py bdist_wheel
# running bdist_wheel
# running build
# running build_py
# creating build
# creating build\lib
# creating build\lib\com
# copying src\com\__init__.py -> build\lib\com
# creating build\lib\com\yootk
# copying src\com\yootk\data.py -> build\lib\com\yootk
# copying src\com\yootk\message.py -> build\lib\com\yootk
# copying src\com\yootk\__init__.py -> build\lib\com\yootk
# D:\python_install_file\Lib\site-packages\setuptools\command\install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
#   warnings.warn(
# installing to build\bdist.win-amd64\wheel
# running install
# running install_lib
# creating build\bdist.win-amd64
# creating build\bdist.win-amd64\wheel
# creating build\bdist.win-amd64\wheel\com
# creating build\bdist.win-amd64\wheel\com\yootk
# copying build\lib\com\yootk\data.py -> build\bdist.win-amd64\wheel\.\com\yootk
# copying build\lib\com\yootk\message.py -> build\bdist.win-amd64\wheel\.\com\yootk
# copying build\lib\com\yootk\__init__.py -> build\bdist.win-amd64\wheel\.\com\yootk
# copying build\lib\com\__init__.py -> build\bdist.win-amd64\wheel\.\com
# running install_egg_info
# running egg_info
# creating src\yootk.common.egg-info
# writing src\yootk.common.egg-info\PKG-INFO
# writing dependency_links to src\yootk.common.egg-info\dependency_links.txt
# writing top-level names to src\yootk.common.egg-info\top_level.txt
# writing manifest file 'src\yootk.common.egg-info\SOURCES.txt'
# reading manifest file 'src\yootk.common.egg-info\SOURCES.txt'
# writing manifest file 'src\yootk.common.egg-info\SOURCES.txt'
# Copying src\yootk.common.egg-info to build\bdist.win-amd64\wheel\.\yootk.common-0.0.1-py3.11.egg-info        
# running install_scripts
# creating build\bdist.win-amd64\wheel\yootk.common-0.0.1.dist-info\WHEEL
# creating 'dist\yootk.common-0.0.1-py3-none-any.whl' and adding 'build\bdist.win-amd64\wheel' to it
# adding 'com/__init__.py'
# adding 'com/yootk/__init__.py'
# adding 'com/yootk/data.py'
# adding 'com/yootk/message.py'
# adding 'yootk.common-0.0.1.dist-info/METADATA'
# adding 'yootk.common-0.0.1.dist-info/WHEEL'
# adding 'yootk.common-0.0.1.dist-info/top_level.txt'
# adding 'yootk.common-0.0.1.dist-info/RECORD'
# removing build\bdist.win-amd64\wheel
# PS E:\summer_study\python开发\programe\pythonProject\python环境管理> 

