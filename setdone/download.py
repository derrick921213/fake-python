import os,platform as p
system = p.system()
if (system == 'Darwin'):
    print('--------Download Mac install file--------')
    os.system("svn checkout https://github.com/derrick921213/fake-python/trunk/setdone/Mac-setup")
    print('--------Download fisished--------')
elif (system == 'Linux'):
    print('--------Download Linux install file--------')
    os.system("svn checkout https://github.com/derrick921213/fake-python/trunk/setdone/Linux-setup")
    print('--------Download fisished--------')
else:
    print('This app only support Mac and Linux')