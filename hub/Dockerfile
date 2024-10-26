FROM jupyter/minimal-notebook

# 주피터랩 활성화 (JupyterLab 사용 설정)
RUN jupyter server extension enable --py jupyter_http_over_ws

COPY jupyter_notebook_config.py /home/jovyan/.jupyter/jupyter_notebook_config.py

# 디렉토리 권한 설정 (권한 문제가 발생할 수 있으므로 파일 소유권 수정)
USER root
RUN chown -R jovyan:users /home/jovyan/.jupyter

# 다시 jovyan 사용자로 전환
USER $NB_UID