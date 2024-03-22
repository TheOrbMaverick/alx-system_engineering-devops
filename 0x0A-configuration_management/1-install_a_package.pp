# Puppet Manifest: Install Flask version 2.1.0 using pip3

exec { 'install python packages':
     command   => 'pip3 install flask',
     ensure   => '2.1.0'
}

