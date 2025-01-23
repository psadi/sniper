FROM python:3.13.1-alpine3.21

COPY dist/sniper-*.tar.gz sniper.tar.gz

RUN python3 -m pip --no-cache-dir install sniper.tar.gz --root-user-action=ignore && \
    rm -rf sniper.tar.gz

ENTRYPOINT [ "sniper" ]

