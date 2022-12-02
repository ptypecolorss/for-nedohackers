import os

os.system('REG ADD "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /f /v "DisableTaskMgr" /t REG_DWORD /d 0')
