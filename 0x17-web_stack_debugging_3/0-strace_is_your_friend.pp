# Fix Apache configuration to resolve 500 error

# Ensure Apache package is installed
package { 'apache2':
  ensure => 'installed',
}

# Ensure Apache service is running and enabled
service { 'apache2':
  ensure  => 'running',
  enable  => true,
  require => Package['apache2'],
}

# Manage Apache configuration file (e.g., /etc/apache2/apache2.conf)
file { '/etc/apache2/apache2.conf':
  ensure  => file,
  content => template('apache/apache2.conf.erb'), # Use a template to manage configuration content
  notify  => Service['apache2'],
}
