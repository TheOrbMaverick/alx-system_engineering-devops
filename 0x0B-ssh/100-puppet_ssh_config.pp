file { '/home/ubuntu/.ssh/config':
  ensure  => 'file',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => "
Host ubuntu@35.174.200.243
    HostName 35.174.200.243
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
",
}
