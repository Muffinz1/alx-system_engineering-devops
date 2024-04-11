# fixing the 500 error msg and automate it with puppet
exec { 'fixing-500-error':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
