#!/usr/bin/env puppet
# creating a custom HTTP header response, but with Puppet

package {'mginx':
ensure   => installed,
}

file_line {'header_response':
ensure => 'present',
path   => '/etc/nginx/sites-available/default',
}

exec { 'add_x_header':
command  => "sudo sed -i '19 i \\tadd_header X-Served-By ${hostname};' /etc/nginx/sites-available/default",
provider => 'shell',
}
