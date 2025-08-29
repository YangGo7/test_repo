'n- add / healthz note
##run (window PowerShell)
#1) 가상환경 활성화 
py -m venv . venv 
. .\.\venv\scripts\Activate.ps1
#2) 패키지 설치
pip install -r requirements.txt
#3) 서버 실행
uvicorn app.main:app --reload
# 브라우저 https:127.0.0.1:8000/healthz -> {"status":"oK"}
