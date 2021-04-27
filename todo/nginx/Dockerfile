FROM nginx

WORKDIR /etc/nginx

RUN mkdir /etc/nginx/ssl

COPY ssl_certs/fullchain.pem /etc/nginx/ssl/
COPY ssl_certs/privkey.pem /etc/nginx/ssl/

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d/