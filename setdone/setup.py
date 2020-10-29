import os,platform as p
system = p.system()
if (system == 'Darwin'):
    print('MacOS')
elif (system == 'Linux'):
    print('Linux')
else:
    print('This app only support Mac and Linux')        

#print('--------Download install file--------')
#os.system("svn checkout https://github.com/derrick921213/fake-python/trunk/dist;cd dist;svn checkout https://github.com/derrick921213/fake-python/trunk/commands")
#print('--------Download fisished--------')