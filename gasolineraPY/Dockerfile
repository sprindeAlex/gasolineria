# Use the official PHP image with Apache
FROM php:8.1.1-apache

# Install necessary extensions and tools
RUN apt-get update && apt-get install -y \
    libpng-dev \
    libjpeg-dev \
    libfreetype6-dev \
    zip \
    unzip \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install gd \
    && docker-php-ext-install pdo pdo_mysql

# Enable Apache mod_rewrite
RUN a2enmod rewrite

# Set the ServerName to localhost to suppress the warning
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Copy the application code to the container
COPY . /var/www/html/

# Set the working directory
WORKDIR /var/www/html/

# Set proper permissions
RUN chown -R www-data:www-data /var/www/html

# Expose port 80
EXPOSE 80

# Start Apache server
CMD ["apache2-foreground"]
