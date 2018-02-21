"""
Does the following:

1. Inits git if used
2. Deletes dockerfiles if not going to be used
3. Deletes config utils if not needed
"""
from __future__ import print_function
import os
import shutil
from subprocess import Popen

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filename):
    """
    generic remove file from project dir
    """
    fullpath = os.path.join(PROJECT_DIRECTORY, filename)
    if os.path.exists(fullpath):
        os.remove(fullpath)


def init_git():
    """
    Initialises git on the new project folder
    """
    GIT_COMMANDS = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-a", "-m", "Initial Commit."]
    ]

    for command in GIT_COMMANDS:
        git = Popen(command, cwd=PROJECT_DIRECTORY)
        git.wait()


def remove_docker_files():
    """
    Removes files needed for docker if it isn't going to be used
    """
    for filename in ["Dockerfile"]:
        path = os.path.join(
            PROJECT_DIRECTORY, filename
        )
        if os.path.exists:
            os.remove(path)


def remove_viper_files():
    """
    Removes files needed for viper config utils
    """
    path = os.path.join(
        PROJECT_DIRECTORY, "config"
    )

    if os.path.exists(path):
        shutil.rmtree(path)


def remove_logrus_files():
    """
    Removes files needed for viper config utils
    """
    path = os.path.join(
        PROJECT_DIRECTORY, "log"
    )

    if os.path.exists(path):
        shutil.rmtree(path)

# remove service specific files if we're writing a library
if '{{ cookiecutter.project_type }}'.lower() == 'library':
    remove_viper_files()
    remove_logrus_files()
    remove_docker_files()
    remove_file('main.go')
    remove_file('version.go')

# 1. Remove Dockerfiles if docker is not going to be used
if '{{ cookiecutter.use_docker }}'.lower() != 'y':
    remove_docker_files()

# 2. Remove viper config if not selected
if '{{ cookiecutter.use_viper_config }}'.lower() != 'y':
    remove_viper_files()

# 3. Remove logrus utils if not selected
if '{{ cookiecutter.use_logrus_logging }}'.lower() != 'y':
    remove_logrus_files()

# 4. Remove unused ci choice
if '{{ cookiecutter.use_ci}}'.lower() == 'travis':
    remove_file("circle.yml")
elif '{{ cookiecutter.use_ci}}'.lower() == 'circle':
    remove_file(".travis.yml")
else:
    remove_file(".travis.yml")
    remove_file("circle.yml")

# 5. Initialize Git (should be run after all file have been modified or deleted)
if '{{ cookiecutter.use_git }}'.lower() == 'y':
    init_git()
else:
    remove_file(".gitignore")

# Remove unused vendor related tools
if '{{ cookiecutter.vendor_tool }}'.lower() == 'glide':
    remove_file('Gopkg.toml')
elif '{{ cookiecutter.vendor_tool }}'.lower() == 'dep':
    remove_file('glide.yaml')
else:
    remove_file('Gopkg.toml')
    remove_file('glide.yaml')

