# Define a class for Nginx configuration
class nginx_config {

    # Install Nginx package
    package { 'nginx':
        ensure  => installed,
    }

    # Define Nginx service
    service { 'nginx':
        ensure  => running,
        enable  => true,
        require => Package['nginx'],
    }

    # Set up Nginx configuration file
    file { '/etc/nginx/sites-available/default':
        ensure  => file,
        content => "
server {
    listen 80;
    server_name _;
    root /var/www/html;
    index index.html;

    location / {
        return 200 'Hello World!';
        add_header Content-Type text/plain;
    }

    location /redirect_me {
        return 301 https://youtube.com/@AfroPlayerOne?si=BueiWNt5G6RIRvJe;
    }

    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
}
",
        require => Package['nginx'],
        notify  => Service['nginx'],
    }

    # Create a 404.html page
    file { '/var/www/html/404.html':
        ensure  => file,
        content => 'Ceci n\'est pas une page',
        require => Package['nginx'],
        notify  => Service['nginx'],
    }
}

# Apply the class
include nginx_config
