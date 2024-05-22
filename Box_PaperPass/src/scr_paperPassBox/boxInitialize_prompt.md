Request Prompt to ChatGPT
========
> ...

# 運用構想：
  I want to set a simple vulnerable ubuntu box for cyber security class.

# 擬請AI提供項目
  please provide a bash script that can set the vulnerabilities in a given Ubuntu.

## 提供操作說明：
  - how to run this bash script step by step.
  - box admin can management this box via ssh

## 設定基本功能：
  - add a new user "boxadmin" .   And add boxowner to root group.
  - change admin's password to plaintext "boxadmin". Ex. echo "boxadmin:boxadmin" | chpasswd.
  - check whether ssh service exists. if ssh not exist, install it.
    
## 設定外部滲透弱點：
  - add a new user, allen, who is a regular user.
  - change allen's password to plaintext "password". Ex. echo "allen:password" | chpasswd
  - In allen's home directory create a new file, named user.txt. And add a string "user's flag" to the file.
  - set allen's password as plaintext "password" exactly, not use crypted string. 

## 設定內部擴散弱點：
  * In root's home directory create a new file, named root.txt. And add a string "root's flag" to the file.
  * check whether sudo function exists. if sudo not exist, install it.
  * authorize all users the privilege that can execute cp command with root privileged.

# 擬請AI作業流程

## When prepare the data:
- do the work step by step.make it easy to understand for students.
- provide clear explanation with traditional Chinese.
- give instructions about how to use this file in the beginning.

## When respond the data to me
- just show the action files only. If you need any thing for reminding, put it in the action file in comment style.
* segment  code exactly according what I mention in  [# 需求項目]
* echo empty line between segments.
* This script will be run in Ubuntu container by root, don't use sudo.
* This script will be run in Ubuntu container with only core functions, use core commands only.
* do the work step by step.make it easy to understand for students.
* use limited echo lines with traditional Chinese I show you in following reference.
  
# 提供AI參考格式
```sh
#!/bin/bash

# 使用說明  
# 1. Copy this script to...
# 2. Open terminal...
# 3. Navigate to ...
# 4. chmod +x ...
# 5. Run the command...

# 靶機管理設定
echo "" 
echo "靶機管理設定"
useradd -m...
usermod -aG ...
echo... | chpasswd
service ssh ...

# 外部滲透設定
echo ""
echo "外部滲透設定"
useradd ...
service ssh ...


# 內部提權設定
echo ""
echo "內部提權設定"
if ...sudo...  

# 完成設定
echo ""
echo "完成設定"
```