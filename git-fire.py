import subprocess
import os
from datetime import date


current_branch = (
    subprocess.run("git symbolic-ref HEAD", capture_output=True)
    .stdout.decode("utf-8")
    .replace("\n", "")
    .replace("\r", "")
)
repo_base = (
    subprocess.run("git rev-parse --show-toplevel", capture_output=True)
    .stdout.decode("utf-8")
    .replace("\n", "")
    .replace("\r", "")
)
user_email = (
    subprocess.run("git config user.email", capture_output=True)
    .stdout.decode("utf-8")
    .replace("\n", "")
    .replace("\r", "")
)
current_epoch = date.today()
new_branch = str(f"FIRE_({current_branch})_({user_email})_({current_epoch})")

# push committed local changes
os.system("git push -a")

initial_branch = current_branch

# checks out fire branch
os.system(f"git switch -c {new_branch}")

# navigates to base folder of repo
if repo_base != os.getcwd():
    os.chdir(repo_base)
    print(f"Navigated to {os.getcwd()}")

# adds all changes to staging area
os.system("git add -A")
message = str(f"Fire! Branch {current_branch}")

os.system(f'git commit -m "{message}"')

os.system(f"git push -u origin {new_branch}")
print("Push successful! Now git out!")
