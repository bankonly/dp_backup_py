import os
import platform
from datetime import datetime
from dotenv import load_dotenv
from pexpect import popen_spawn

# LOAD .ENV
load_dotenv(dotenv_path="./.env")

# target download folder name
target_folder_download = datetime.today().strftime('%Y-%m-%d-00-00')

# Store key
PROD_SERVER_PASSWORD = os.getenv("PROD_SERVER_PASSWORD")
PROD_SERVER_IP = os.getenv("PROD_SERVER_IP")
PROD_SERVER_USER = os.getenv("PROD_SERVER_USER")

command = "sshpass -p {password} scp -r root@{server_ip}:/root/DB/{path} /d/db_backup".format(
    server_ip=PROD_SERVER_IP, path=target_folder_download, password=PROD_SERVER_PASSWORD)

# Detect OS
detect_os = platform.system()

# if detect_os is Windows then do this command
if detect_os == "Windows":
    command = "scp -r root@{server_ip}:/root/DB/{path} /d/db_backup".format(
        server_ip=PROD_SERVER_IP, path=target_folder_download)
    runner = popen_spawn.PopenSpawn(cmd=command)
    runner.sendline(PROD_SERVER_PASSWORD)
else:
    # run Mac, Linux command without password
    os.system(command)

# Complete Backup Message
print("COMPLETE BACKUP")
