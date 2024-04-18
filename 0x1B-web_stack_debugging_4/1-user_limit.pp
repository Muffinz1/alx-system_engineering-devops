# user holberton safe landing

exec { 'hard file limit':
  command => 'sed -i "/holberton hard/s/5/5000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'soft file limit':
  command => 'sed -i "/holberton soft/s/4/5000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
