import os import subprocess import 
requests
# إعداد GitHub
GITHUB_USERNAME = "Mohamedazra" 
GITHUB_REPO = "glowing-doodle" 
GITHUB_TOKEN = "ghp_XXXXXXXXXXXXXX" # 
بدلو بالتوكن 
ديالك def run_command(cmd):
    try: result = 
        subprocess.check_output(cmd, 
        shell=True, 
        stderr=subprocess.STDOUT, 
        text=True) return result.strip()
    except subprocess.CalledProcessError 
    as e:
        return f"[خطأ] 
        {e.output.strip()}"
def list_installed_apps(): return 
    run_command("pm list packages")
def github_push(commit_msg="تحديث 
تلقائي"):
    run_command("git add .") 
    run_command(f"git commit -m 
    \"{commit_msg}\"") push_cmd = f"git 
    push 
    https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{GITHUB_REPO}.git" 
    return run_command(push_cmd)
def show_help(): return """ أوامر 
متاحة: - apps : عرض 
التطبيقات المثبتة - 
gitpush نص : إرسال إلى 
GitHub مع رسالة - cmd أمر : 
تنفيذ أمر في 
النظام - help : عرض 
المساعدة - exit : الخروج 
""" def assistant():
    print("مساعدك الذكي 
    جاهز، مرحبا بك!") 
    while True:
        cmd = input("أمر > ").strip() 
        if cmd == "help":
            print(show_help()) elif cmd == 
        "apps":
            print(list_installed_apps()) 
        elif cmd.startswith("gitpush"):
            _, *msg = cmd.split(" ") 
            commit_msg = " ".join(msg) or 
            "تحديث من 
            الهاتف" 
            print(github_push(commit_msg))
        elif cmd.startswith("cmd"): _, 
            *sys_cmd = cmd.split(" ") 
            print(run_command(" 
            ".join(sys_cmd)))
        elif cmd == "exit": print("مع 
            السلامة!") break
        else: print("لم أفهم 
            الأمر. كتب help 
            للمساعدة.")
if __name__ == "__main__":
    assistant()+0
+
