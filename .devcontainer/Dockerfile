FROM mcr.microsoft.com/devcontainers/java:1-21-bullseye

# Install dependencies for noVNC + websockify
RUN apt-get update && \
    apt-get install -y \
        git \
        python3 \
        python3-pip \
        net-tools \
        x11vnc \
        xvfb \
        fluxbox \
        wget \
        supervisor && \
    rm -rf /var/lib/apt/lists/*

# Clone noVNC + websockify
RUN git clone https://github.com/novnc/noVNC.git /opt/novnc && \
    git clone https://github.com/novnc/websockify.git /opt/novnc/utils/websockify && \
    ln -s /opt/novnc/vnc.html /opt/novnc/index.html

# Expose noVNC default port
EXPOSE 6080

# Add supervisor config to launch Xvfb, x11vnc, and noVNC proxy
RUN mkdir -p /etc/supervisor/conf.d
RUN mkdir -p /var/supervisor
RUN mkdir -p /var/libs

RUN chown -R vscode /var/supervisor
RUN chown -R vscode /var/libs

COPY supervisord-novnc.conf /etc/supervisor/conf.d/supervisord-novnc.conf
COPY stdlib.jar /var/libs/stdlib.jar

RUN echo "export DISPLAY=:0" >> /home/vscode/.bashrc
RUN echo "export CLASSPATH=/var/libs/stdlib.jar:." >> /home/vscode/.bashrc
