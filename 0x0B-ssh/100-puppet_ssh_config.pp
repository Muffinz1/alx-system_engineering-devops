#!/usr/bin/pup
# a puppet file to change the authentication to no 
# change the file host to school

file_line{'host school':
path    => '/etc/ssh/ssh_config',
line    => 'IdentityFile ~/.ssh/school',
replace => true,
}


file_line{'PasswordAuthentication':
path    => '/etc/ssh/ssh_config',
line    => 'PasswordAuthentication no',
replace => true,
}
