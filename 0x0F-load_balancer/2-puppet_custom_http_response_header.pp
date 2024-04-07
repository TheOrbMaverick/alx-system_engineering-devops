# 2-puppet_custom_http_response_header.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define a custom fact to get the hostname
$hostname = $facts['hostname']

# Configure Nginx to add custom HTTP header
file { '/etc/nginx/sites-available/itaenang.tech':
  ensure  => present,
  content => "
server {
    listen 80;
    server_name itaenang.tech www.itaenang.tech;
    add_header X-Served-By $hostname;
    root /var/www/html;
    index index.html index.htm;
    location / {
        # Additional configuration directives if needed
    }
}
",
  notify  => Service['nginx'],
}

# Enable the site
file { '/etc/nginx/sites-enabled/itaenang.tech':
  ensure => link,
  target => '/etc/nginx/sites-available/itaenang.tech',
  notify => Service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/itaenang.tech'],
}