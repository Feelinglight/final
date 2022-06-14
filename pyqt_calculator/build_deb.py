import re
import subprocess
import pathlib
import shutil
import os

from pyqt_dark_calculator import app_info


DEB_BUILD_FOLDER = pathlib.Path('./deb_build')
DEB_SOURCES_FOLDER = DEB_BUILD_FOLDER/pathlib.Path("sources")

DEB_PACKET_NAME = f'{app_info.SHORT_NAME.replace("_", "-")}_{app_info.VERSION}'


# Из этих папок берутся только .py файлы
source_folders = ['./pyqt_dark_calculator', './pyqt_dark_calculator/tests']

# Эти папки/файлы полностью копируются
files = [
    # Папки
    './pyqt_dark_calculator/ico',
    './pyqt_dark_calculator/style',
    #Отдельные файлы
]


def exec_shell(cmd):
    print(f'shell: {cmd}')
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    return output.decode().strip().replace('\r', '')


def make_tarball():

    tarball_filename = DEB_BUILD_FOLDER/f'{DEB_PACKET_NAME}.orig.tar.gz'

    if os.path.exists(DEB_SOURCES_FOLDER):
        shutil.rmtree(DEB_SOURCES_FOLDER)

    if os.path.exists(tarball_filename):
        os.remove(tarball_filename)

    for folder_str in source_folders:
        current_folder = DEB_SOURCES_FOLDER/folder_str
        os.makedirs(current_folder)

        folder = os.fsencode(folder_str)
        for file in os.listdir(folder):
            filename = os.fsdecode(file)
            if filename.endswith('.py'):
                shutil.copyfile(os.path.join(folder_str, filename), os.path.join(current_folder, filename))

    for path in files:
        os.makedirs(DEB_SOURCES_FOLDER/os.path.dirname(path), exist_ok=True)
        if os.path.isdir(path):
            shutil.copytree(path, DEB_SOURCES_FOLDER/path)
        else:
            shutil.copyfile(path, DEB_SOURCES_FOLDER/path)

    print('Make tarball...')
    exec_shell(f'tar -zcf {os.path.basename(tarball_filename)} -C {DEB_SOURCES_FOLDER} .')

    if os.path.exists(DEB_SOURCES_FOLDER):
        shutil.rmtree(DEB_SOURCES_FOLDER)


def rm_pycache():
    for folder_str in source_folders:
        pycache_folder = f"{folder_str}/__pycache__"
        if os.path.exists(pycache_folder):
            shutil.rmtree(pycache_folder)


if __name__ == "__main__":
    make_tarball()
    rm_pycache()

    os.chdir("pyqt_dark_calculator")
    exec_shell("dpkg-buildpackage -us -uc")
