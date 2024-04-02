# Ensure SSH client configuration directory exists
file { '/home/ubuntu/.ssh':
  ensure  => directory,
  mode    => '0700',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create SSH client configuration file
file { '/home/ubuntu/.ssh/config':
  ensure  => present,
  mode    => '0600',
  content => "\
Host <YOUR_SERVER_IP>
  IdentityFile ~/.ssh/school
  PasswordAuthentication no\n",
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Restart SSH service after making changes
service { 'ssh':
  ensure    => running,
  enable    => true,
  subscribe => File['/home/ubuntu/.ssh/config'],
}
