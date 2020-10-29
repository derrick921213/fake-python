import os,platform as p
system = p.system()
if (system == 'Darwin'):
    print('--------Download Mac install file--------')
    os.system("svn checkout https://github.com/derrick921213/fake-python/trunk/setdone/mac")
    print('--------Download fisished--------')
elif (system == 'Linux'):
    print('--------Download Linux install file--------')
    os.system("svn checkout https://github.com/derrick921213/fake-python/trunk/setdone/linux")
    print('--------Download fisished--------')
else:
    print('This app only support Mac and Linux')