FROM ubuntu:22.04
ARG USER_PASSWORD="default"
ARG PY_VERSION="3.11.4"
ARG APP_DATA="./apps/requirements.txt"

# タイムゾーンの設定
ENV DEBIAN_FRONTEND noninteractive
ENV TZ=Asia/Tokyo

RUN apt update \
    # tzdataはpythonの導入に必要なパッケージの依存パッケージなので先にinstall
    && apt install -y tzdata \
    sudo \
    curl \
    git \
    gcc \
    make \
    zip \
    vim \
    nginx \
    systemctl \
    mysql-client \
    python3-dev \
    libsqlite3-dev  \
    libbz2-dev  \
    libreadline-dev \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libxml2-dev \
    libxmlsec1-dev \
    libffi-dev \
    liblzma-dev \
    default-libmysqlclient-dev \
    pkg-config \
    libcurl4-openssl-dev \
    graphviz \
    libgraphviz-dev \
    # ロケールに関するパッケージ
    locales \
    language-pack-ja-base \
    language-pack-ja \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# ロケールの設定
# ロケールの設定
RUN locale-gen en_US.UTF-8 ja_JP.UTF-8 \
    && update-locale LANG=ja_JP.UTF-8 LC_MESSAGES=en_US.UTF-8

RUN systemctl enable nginx

# 日本語フォント追加
RUN curl -L -O https://noto-website.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip \
 && unzip -d noto NotoSansCJKjp-hinted.zip \
 && mkdir -p /usr/share/fonts/opentype \
 && mv -fv noto /usr/share/fonts/opentype/noto \
 && rm -rfv NotoSansCJKjp-hinted.zip \
 && fc-cache -fv \
 && chmod -Rf a+r /usr/share/fonts/*

WORKDIR /var/www/django

ADD $APP_DATA /var/www/django/
ADD ./nginx /etc/nginx/conf.d

RUN useradd -ms /bin/bash django && \
    echo "django:${USER_PASSWORD}" | chpasswd && \
    echo "django ALL=(ALL) ALL" >> /etc/sudoers && \
    usermod -aG www-data django

RUN chmod 2775 /var/log/nginx && chgrp -R www-data /var/log/nginx && \
    chown -R django /var/www/django

USER django

ENV HOME=/home/django

RUN cd ${HOME} && git clone https://github.com/yyuu/pyenv.git .pyenv
ENV PYENV_ROOT ${HOME}/.pyenv
ENV PATH ${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}
RUN export CPPFLAGS=-I/usr/include/openssl11 \
 && export LDFLAGS=-L/usr/lib64/openssl11 \
 && pyenv install ${PY_VERSION} \
 && pyenv rehash \
 && pyenv global ${PY_VERSION}

RUN pip install --no-cache-dir --upgrade wheel \
 && pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "/bin/bash", "-c", \
   "python manage.py collectstatic --no-input && \
   python manage.py migrate && \
   uwsgi --ini atma/wsgi.ini && \
   echo ${USER_PASSWORD} | sudo -S /usr/sbin/nginx -g \"daemon off;\""]