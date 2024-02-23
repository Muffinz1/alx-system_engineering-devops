# a puppet file to install flask @ version 2.1.0
# enusres the package existance
# then executes a command to install the file

package { 'python3-pip':
  ensure => installed,
}

exec { 'install-flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  require => Package['python3-pip'],
}
