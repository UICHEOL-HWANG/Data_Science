c = get_config()

# 주피터 서버의 IP 및 포트 설정
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 8888

# 주피터 노트북 서버를 실행할 디렉토리 지정
c.NotebookApp.notebook_dir = '/home/jovyan/work'

# 브라우저 자동 열림 비활성화
c.NotebookApp.open_browser = False

# 데이터 전송 속도 제한 해제
c.NotebookApp.iopub_data_rate_limit = 1.0e10

# 터미널 기본 셸을 bash로 설정
c.NotebookApp.terminado_settings = {'shell_command': ['/bin/bash']}