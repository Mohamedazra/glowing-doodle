import os; import subprocess; def 
assistant(): print("Type 'help' to see 
commands."); token = input("Enter your 
GitHub token (or leave empty): ").strip(); 
repo = input("Enter your GitHub repo URL 
(e.g. 
https://github.com/username/repo.git): 
").strip(); while True: cmd = input(">> 
").strip(); print(); if cmd == "help": 
print("Commands: help, apps, cmd 
<command>, gitpush, quit"); elif cmd == 
"apps": os.system("ls ~"); elif 
cmd.startswith("cmd "): 
os.system(cmd[4:]); elif cmd == "gitpush": 
msg = input("Commit message: "); 
os.system(f"git add . && git commit -m 
\"{msg}\" && git branch -M main && git 
remote remove origin && git remote add 
origin https://{token}@{repo[8:]} && git 
push -u origin main"); elif cmd == "quit": 
break; else: print("Unknown command. Try 
'help'.");
if __name__ == "__main__": assistant()0
