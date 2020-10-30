import os,platform as p
system = p.system()
path = os.path.abspath('.')
if (system == 'Darwin'):
    print('--------Download Mac install file--------')
    os.system("svn checkout https://github.com/derrick921213/fake-python/trunk/setdone/mac")
    print('In mac folder use ./Mac-setup')
    print('--------Download fisished--------')
    os.system("cd mac;./Mac-setup;cd mac-main;./Mac-main --install;mv Mac-main ~/Documents/pycontroler")
elif (system == 'Linux'):
    print('--------Download Linux install file--------')
    os.system("svn checkout https://github.com/derrick921213/fake-python/trunk/setdone/linux")
    print('In linux folder use ./Linux-setup')
    print('--------Download fisished--------')
else:
    print('This app only support Mac and Linux')