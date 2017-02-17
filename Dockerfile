FROM ubuntu:14.04
ENV DEBIAN_FRONTEND noninteractive
MAINTAINER Everton Gago <everton.gago@dextra-sw.com>

RUN apt-get update
RUN apt-get install -y openssh-server && apt-get install rsync
RUN mkdir /var/run/sshd
RUN echo 'root:screencast' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

RUN apt-get -y install software-properties-common
RUN apt-get -y install python-pip python-dev build-essential
RUN pip install --upgrade pip
RUN apt-get -y install vim
RUN apt-get -y install git

RUN pip install pyyaml
RUN pip install numpy
RUN pip install WebOb
RUN pip install Paste
RUN pip install webapp2
RUN pip install pycrypto

RUN wget -P /root/ https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-142.0.0-linux-x86_64.tar.gz
RUN tar zxf /root/google-cloud-sdk-142.0.0-linux-x86_64.tar.gz -C /root/
RUN rm /root/google-cloud-sdk-142.0.0-linux-x86_64.tar.gz
#RUN cp /root/google-cloud-sdk/platform/google_appengine/lib/fancy_urllib/fancy_urllib/__init__.py /root/google-cloud-sdk/platform/google_appengine/lib/fancy_urllib/__init__.py

RUN mkdir /root/.ssh
RUN ssh-keygen -t rsa -P '' -f /root/.ssh/id_rsa
RUN cat /root/.ssh/id_rsa.pub > /root/.ssh/authorized_keys
