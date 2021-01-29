FROM continuumio/anaconda3:latest

# Install.
RUN \
  apt update && \
  apt -y upgrade && \
  apt install -y gcc git libjpeg-dev libz-dev python-dev libffi-dev libssl-dev libxslt1-dev libpq-dev systemd


# Set environment variables.
ENV HOME /root

# Define working directory.
WORKDIR /root

# Define default command.
CMD ["bash"]
COPY install.sh /tmp/install.sh
RUN /bin/bash /tmp/install.sh
COPY config.py /opt/conda/envs/privacyidea/config.py
COPY wsgi.py /opt/conda/envs/privacyidea/wsgi.py
COPY gunicorn.py /opt/conda/envs/privacyidea/gunicorn.py

COPY run.sh /opt/conda/envs/privacyidea/bin/run.sh
RUN chmod +x /opt/conda/envs/privacyidea/bin/run.sh
# EXPOSE 8000
# ENTRYPOINT ["/opt/conda/envs/privacyidea/bin/run.sh"]

WORKDIR /opt/conda/envs/privacyidea
ENTRYPOINT ["conda","run","-n","privacyidea","gunicorn","--bind","0.0.0.0:5000","--log-level","debug","--access-logfile","/var/log/gunicorn-access.log","--error-logfile","/var/log/gunicorn-error.log","wsgi:app"]
