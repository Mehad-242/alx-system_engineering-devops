# Puppet script to create ssh config file
file_line {'Turn off passwrd auth':
	ensure => 'preent',
	path => '/etc/ssh/ssh_config',
	line => '    passwordAuthentication no',
}
file_line {'Declare identity file':
	ensure => 'preent',
	path => '/etc/ssh/ssh_config',
	line => '    IdentityFile ~/.ssh/school',
}
