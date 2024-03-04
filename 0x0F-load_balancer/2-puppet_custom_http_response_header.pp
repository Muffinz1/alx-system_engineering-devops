#!/usr/bin/env puppet
# creating a custom HTTP header response, but with Puppet
exec {'header_response':
  command  => "sudo apt-get update;
               sudo apt-get -y install nginx;
               sudo sed -i '19 i \\\tadd_header X-Served-By $HOSTNAME;' /etc/nginx/sites-available/default;
               sudo service nginx restart;",
  provider => 'shell',
}
