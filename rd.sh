#!/bin/bash
DEBIAN_FRONTEND=noninteractive \
apt install --assume-yes xfce4 desktop-base dbus-x11 xscreensaver && \
wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb && \
dpkg -i chrome-remote-desktop_current_amd64.deb && \
apt install -f && \
bash -c 'echo "exec /etc/X11/Xsession /usr/bin/xfce4-session" > /etc/chrome-remote-desktop-session' && \
systemctl disable lightdm.service
