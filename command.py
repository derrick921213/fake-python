import paramiko
host = '192.168.210.130'
user = 'derrick'
pw = '0170'
'''def connect():
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.load_system_host_keys()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(host,22,user,pw)
        std_in,std_out,std_err = ssh_client.exec_command('cd test/;ls',get_pty=True) 
        #std_in.write('PWD'+'\n') #执行输入命令，输入sudo命令的密码，会自动执行
        for line in std_out:
            print(line.strip('\n'))
        #print(''.join(std_out.readlines()))    
        ssh_client.close()
    except Exception as e:
        print (e)'''
try:
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(host,22,user,pw)
    std_in,std_out,std_err = ssh_client.exec_command('cd test/;ls',get_pty=True) 
    #std_in.write('PWD'+'\n') #执行输入命令，输入sudo命令的密码，会自动执行
    #for line in std_out:
        #print(line.strip('\n'))
    print(''.join(std_out.readlines()))    
    ssh_client.close()
except Exception as e:
    print (e)