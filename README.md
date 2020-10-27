# *_Use the python to control server_*  
## Requirement
- Cmder
- python3
- pipenv
- pyinstaller

## Install
* For linux and mac, run <a href="./install.sh">**install.sh**</a> to install this program.
* For windows, in cmder type ``` sh install.sh ``` then it can install.  

## Uninstall
* Just remove this program folder

## Compile yourself
1. Step one  
    1. Make sure the <a href="https://medium.com/tsungs-blog/python-%E8%AE%93pipenv-%E5%B9%AB%E4%BD%A0%E5%81%9A%E5%A5%97%E4%BB%B6%E7%AE%A1%E7%90%86-bb284e865dc1">**pipenv**</a> was installed on your system.
2. Step two  
    1. Download the cmder, then install.
    2. Open cmder, then change this program directory.  
    3. Then copy this command ``` pipenv --python 3.8 install ``` on terminal.
    4. If the process finished successfully, then you type ``` pipenv shell ```, after type ``` pyinstaller -F -n control_server main.py ```
    5. you should learn **How to use <a href="https://www.coderbridge.com/@WeiHaoEric/0b2ced0696cc4c38a62d7b26fa7bbea0">pyinstaller</a>**
3. ### *_Congratulations!!!_*
    


