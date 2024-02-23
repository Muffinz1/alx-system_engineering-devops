# installing the flask package @ 2.1.0
exec { 'install-flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
}
