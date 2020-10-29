import os
print('--------Download install file--------')
os.system("svn checkout https://github.com/derrick921213/fake-python/trunk/dist;cd dist;svn checkout https://github.com/derrick921213/fake-python/trunk/commands")
print('--------Download fisished--------')