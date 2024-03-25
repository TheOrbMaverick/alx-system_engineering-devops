# Define Nginx class
class nginx {
  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('nginx/default.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => "Hello World!\n",
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }
}

# Define Nginx configuration template
file { '/etc/nginx/sites-available/default':
  ensure => file,
  source => 'puppet:///modules/nginx/default.erb',
}

# Apply Nginx class
include nginx