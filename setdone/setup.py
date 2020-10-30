import os,platform as p
system = p.system()
if (system == 'Darwin'):
    print('--------Download Mac install file--------')
    os.system("mkdir dist;cd dist;svn checkout https://github.com/derrick921213/fake-python/trunk/done/mac-main;cd mac-main;svn checkout https://github.com/derrick921213/fake-python/trunk/commands")
    print('--------Download fisished--------')
elif (system == 'Linux'):
    print('--------Download Linux install file--------')
    os.system("mkdir dist;cd dist;svn checkout https://github.com/derrick921213/fake-python/trunk/done/linux-main;svn checkout https://github.com/derrick921213/fake-python/trunk/commands")
    print('--------Download fisished--------')
else:
    print('This app only support Mac and Linux')        

