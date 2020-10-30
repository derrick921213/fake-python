#########################################
#建立日期:2020/8/12                     
#作者:Derrick                              
#Github:https://github.com/derrick921213
#########################################


#!/bin/bash
#-----------------設定變數------------------#
env=~/Documents #設定安裝目錄
folder=pycontroler #設定安裝資料夾名稱
download=~/Downloads
system=`uname`
#-----------------設定結束------------------#

echo "#-----------------辨識系統------------------#"
if [ ${system} = "Darwin" ]
    then
        echo "MacOS"
    elif [ ${system} = "Linux" ] 
        then
            echo "Linux"
    else
        echo "Windows"
fi
echo "#-----------------辨識結束------------------#"

echo "#-----------------開始安裝------------------#"
cd ${env}
exites=`test -d ${folder} && echo "exist" || echo "Not exist"`
if [[ ${exites} = "Not exist" ]]
    then
        mkdir ${folder}
    else
        echo "${folder} exist!!"
fi
cd ${download}
svn checkout https://github.com/derrick921213/fake-python/trunk/install-done            
mv install-done ${env}/${folder}
mv ${env}/${folder}/install-done ..
ls
echo "#-----------------安裝結束------------------#"
#cd ${env}
#mkdir pycontroler
#test=`ls ${env}`
#for loop in ${test}; 
#do
#    echo $loop
#done