FROM alpine:latest

RUN echo -e '@testing http://nl.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories && \
    apk update && apk add 3proxy@testing

COPY ./3proxy.cfg.tpl /etc/3proxy.cfg.tpl
COPY ./entrypoint.sh /opt/entrypoint.sh
RUN chmod +x /opt/entrypoint.sh

EXPOSE 10301 10302

ENTRYPOINT ["/opt/entrypoint.sh"]
