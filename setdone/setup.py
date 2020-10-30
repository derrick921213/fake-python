import os,platform as p
system = p.system()
path = os.path.abspath('.')
if (system == 'Darwin'):
    print('--------Download Mac install file--------')
    os.system("svn checkout https://github.com/derrick921213/fake-python/trunk/done/mac-main;cd mac-main;svn checkout https://github.com/derrick921213/fake-python/trunk/commands")
    print('--------Download fisished--------')
elif (system == 'Linux'):
    print('--------Download Linux install file--------')
    os.system("svn checkout https://github.com/derrick921213/fake-python/trunk/done/linux-main;cd linux-main;svn checkout https://github.com/derrick921213/fake-python/trunk/commands;mv commands linux-main")
    print('--------Download fisished--------')
else:
    print('This app only support Mac and Linux')        

