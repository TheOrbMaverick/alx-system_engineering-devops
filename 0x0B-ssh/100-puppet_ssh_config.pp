# Define SSH client configuration file path
$file_path = '/etc/ssh/ssh_config'

# Ensure SSH client configuration file has correct permissions
file { $file_path:
  owner => 'root',
  group => 'root',
  mode  => '0644',
}

# Ensure SSH client uses the private key ~/.ssh/school
file_line { 'Declare identity file':
  path    => $file_path,
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^#?IdentityFile',
  require => File[$file_path],
}

# Ensure SSH client refuses to authenticate using a password
file_line { 'Turn off passwd auth':
  path    => $file_path,
  line    => 'PasswordAuthentication no',
  match   => '^#?PasswordAuthentication',
  require => File[$file_path],
}
