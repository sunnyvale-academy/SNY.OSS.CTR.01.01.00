FROM php:7.0-apache
ARG PORT 80
RUN sed -s -i -e "s/80/${PORT}/" /etc/apache2/ports.conf /etc/apache2/sites-available/*.conf
VOLUME /var/www/html
