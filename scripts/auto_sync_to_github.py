# -*- coding: utf-8 -*-
"""
Auto Sync Tool for B2B Precision Lead Hunter Skill
自动将本地修改推送到 GitHub 远程仓库 (github.com/cnproduct/b2b-precision-lead-hunter-skill)
"""

import os
import subprocess
import sys
import datetime

def run_git(args, cwd):
    res = subprocess.run(['git'] + args, cwd=cwd, capture_output=True, text=True, encoding='utf-8')
    return res.returncode, res.stdout.strip(), res.stderr.strip()

def auto_sync(commit_msg=None):
    repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"[+] Starting sync for repository: {repo_dir}")
    
    if not commit_msg:
        now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        commit_msg = f"Auto update: {now_str}"
    
    # 1. git add
    code, out, err = run_git(['add', '-A'], repo_dir)
    if code != 0:
        print(f"[-] git add failed: {err}")
        return False
    print("[+] Staged all changes.")
    
    # 2. git status check
    code, out, err = run_git(['status', '--porcelain'], repo_dir)
    if not out:
        print("[!] No local changes to commit. Everything is up to date.")
        return True
    
    # 3. git commit
    code, out, err = run_git(['commit', '-m', commit_msg], repo_dir)
    if code != 0:
        print(f"[-] git commit failed: {err}")
        return False
    print(f"[+] Committed changes: {commit_msg}")
    
    # 4. git push
    code, out, err = run_git(['push', 'origin', 'main'], repo_dir)
    if code != 0:
        code, out, err = run_git(['push', '-u', 'origin', 'main'], repo_dir)
        if code != 0:
            print(f"[-] git push failed: {err}")
            return False
    
    print("[SUCCESS] Successfully pushed all updates to github.com/cnproduct/b2b-precision-lead-hunter-skill!")
    return True

if __name__ == '__main__':
    msg = sys.argv[1] if len(sys.argv) > 1 else None
    auto_sync(msg)

