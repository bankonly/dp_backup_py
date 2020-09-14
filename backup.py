import os
import platform
import datetime
from dotenv import load_dotenv
from pexpect import popen_spawn
import pytz

# LOAD .ENV
load_dotenv(dotenv_path="./.env")

# Store key
PROD_SERVER_PASSWORD = os.getenv("PROD_SERVER_PASSWORD")
PROD_SERVER_IP = os.getenv("PROD_SERVER_IP")
PROD_SERVER_USER = os.getenv("PROD_SERVER_USER")
SAVE_PATH = os.getenv("SAVE_PATH")

# target download folder name
target_folder_download = datetime.datetime.utcnow()
target_folder_download = target_folder_download.replace(tzinfo=pytz.utc)
target_folder_download = target_folder_download.strftime('%Y-%m-%d-%H')

# default command
command = "sshpass -p '{password}' scp -r root@{server_ip}:/root/DB/{path} {save_path}".format(
    server_ip=PROD_SERVER_IP, path=target_folder_download, password=PROD_SERVER_PASSWORD, save_path=SAVE_PATH)

# Detect OS
detect_os = platform.system()

# if detect_os is Windows then do this command
if detect_os == "Windows":
    command = "scp -r root@{server_ip}:/root/DB/{path} {save_path}".format(
        server_ip=PROD_SERVER_IP, path=target_folder_download, save_path=SAVE_PATH)
    runner = popen_spawn.PopenSpawn(cmd=command)
    runner.sendline(PROD_SERVER_PASSWORD)
else:
    # run Mac, Linux command without password
    os.system(command)

# Complete Backup Message
print("COMPLETE BACKUP")
