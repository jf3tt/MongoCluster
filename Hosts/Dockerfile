### Debian for Ansible ###
FROM debian:latest
MAINTAINER Rodion Nosankov "geforce.exe@gmail.com"

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y openssh-server\
		vim

COPY ./keys/id_rsa.pub ./root/.ssh/authorized_keys
RUN sed -i '32 i\PermitRootLogin yes' /etc/ssh/sshd_config

CMD ["/usr/sbin/sshd", "-D"]
