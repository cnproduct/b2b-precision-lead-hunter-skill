@echo off
chcp 65001 >nul
echo ========================================================
echo   B2B Precision Lead Hunter Skill - 一键自动同步到 GitHub
echo   Target: github.com/cnproduct/b2b-precision-lead-hunter-skill
echo ========================================================
echo.

python "%~dp0scripts\auto_sync_to_github.py" "Auto update from local workspace"

echo.
echo 同步执行完成，按任意键退出...
pause >nul

