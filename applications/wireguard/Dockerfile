FROM alpine:latest

ENV WG_QUICK_URL https://git.zx2c4.com/WireGuard/plain/src/tools/wg-quick/linux.bash

RUN apk add --no-cache bash wget openresolv iptables sysctl wireguard-tools-wg-quick
RUN wget -O /bin/wg-quick $WG_QUICK_URL \
    && chmod +x /bin/wg-quick

COPY docker-entrypoint.sh /usr/bin/

VOLUME ["/etc/wireguard"]
EXPOSE 10401/udp

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["wg-quick", "up", "wg0"]
