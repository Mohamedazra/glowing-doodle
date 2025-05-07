import os; token=input("GitHub Token: ").strip(); repo=input("Repo URL (e.g. https://github.com/user/repo.git): ").strip(); msg=input("Commit msg: "); os.system(f'git init && git add . && git commit -m "{msg}" && git branch -M main && git remote remove origin && git remote add origin https://{token}@{repo[8:]} && git push -u origin main')

0
