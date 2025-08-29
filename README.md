'n- add / healthz note
##run (window PowerShell)
<br>
#1) 가상환경 활성화 
py -m venv . venv 
. .\.\venv\scripts\Activate.ps1
<br>
#2) 패키지 설치
pip install -r requirements.txt
<br>
#3) 서버 실행
uvicorn app.main:app --reload
<br>
# 브라우저 https:127.0.0.1:8000/healthz -> {"status":"oK"}
