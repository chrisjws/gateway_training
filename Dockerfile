FROM quay.io/bluecat/gateway:20.6.1
USER root 
# RUN pip3 install package==x.x.x
LABEL "customizations"=""
#Keep the stuff more prone to change at the bottom of the file to take advantage 
#of caching
ADD --chown=flask:flask . /portal/bluecat_portal
USER flask
