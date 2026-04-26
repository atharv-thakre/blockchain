import os

commit_message = "New audit block added"

os.system("git add .")
os.system(f'git commit -m "{commit_message}"')
os.system("git push origin main")