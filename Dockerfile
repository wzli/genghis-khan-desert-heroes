# Container runtime for 成吉思汗之大漠英雄傳 (Genghis Khan 1999)
FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Install Wine 32-bit/64-bit and graphics/audio dependencies
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        wine \
        wine32 \
        wine64 \
        libwine \
        libwine:i386 \
        x11-utils \
        p7zip-full \
        timidity \
        freepats \
        pulseaudio \
        libpulse0 \
        libpulse0:i386 \
        locales \
    && rm -rf /var/lib/apt/lists/*

# Generate Big5 and UTF-8 Chinese locales
RUN echo "zh_TW.UTF-8 UTF-8" >> /etc/locale.gen && \
    echo "zh_TW BIG5" >> /etc/locale.gen && \
    locale-gen

WORKDIR /game

# Run with host X11 display and PulseAudio
CMD ["./run_native.sh", "--lang", "en"]
