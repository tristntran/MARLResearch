FROM python:3.10
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
RUN apt-get update
RUN apt-get install -y \
    libopenmpi-dev \
    netcat \
    gcc \
    g++ \
    lsof \
    git-lfs \
    cmake \
    libz-dev \
    ffmpeg
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
