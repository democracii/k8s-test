FROM nginx:latest

# useradd 명령으로 UID가 0-99인 일반 계정과 중복하지 않은 1000이상 UID 지정
RUN useradd -u 1001 mzc # 1001 UID를 지정하고 사용자(mzc)를 추가

# 생성한 사용자 권한을 추가하지 않으면 컨테이너가 실행되지 않음
RUN chown -R mzc:mzc /etc/nginx/conf.d &&\
    chown -R mzc:mzc /var/log/nginx/ && \
    chown -R mzc:mzc /var/cache/nginx  && \
    chown -R mzc:mzc /usr/share/nginx/

RUN touch /var/run/nginx.pid && \
    chown -R mzc:mzc /var/run/nginx.pid
