#!/bin/bash

# 使用說明
# 1. 將此腳本複製到靶機上。
# 2. 開啟終端機。
# 3. 導航至腳本所在的目錄。
# 4. 給腳本執行權限: chmod +x setup_vulnerabilities.sh
# 5. 執行腳本: ./setup_vulnerabilities.sh

# 靶機管理設定
echo ""
echo "靶機管理設定"
useradd -m boxadmin
usermod -aG sudo boxadmin
echo "boxadmin:boxadmin" | chpasswd
if ! service --status-all | grep -Fq 'ssh'; then
  apt-get update && apt-get install -y ssh
fi
service ssh start

# 外部滲透設定
echo ""
echo "外部滲透設定"
useradd -m allen
echo "allen:password" | chpasswd
echo "user's flag" > /home/allen/user.txt
chown allen:allen /home/allen/user.txt

# 內部提權設定
echo ""
echo "內部提權設定"
echo "root's flag" > /root/root.txt
if ! dpkg -l | grep -Fq 'sudo'; then
  apt-get update && apt-get install -y sudo
fi
echo "ALL ALL=(ALL) NOPASSWD: /bin/cp" >> /etc/sudoers

# 完成設定
echo ""
echo "完成設定"
echo "靶機已成功設定，請小心使用。"
