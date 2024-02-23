# a puppet file to install a package
# ensure that the pip is installed 
# form it install flask

package{'python3-pip':
	ensure => installed,
}

exec { 'install-flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  require => Package['python3-pip'],
}
