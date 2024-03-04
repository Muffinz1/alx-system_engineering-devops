# creating a custom HTTP header response, but with Puppet
package { 'nginx':
ensure => installed,
}

file_line { 'header_response':
ensure => present,
path   => '/etc/nginx/sites-available/default',
line   => 'add_header X-Served-By $hostname;',
}
