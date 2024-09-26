 Puppet manifest to fix Apache 500 error due to file permissions

file { '/var/www/html/wp-config.php':
	ensure => file,
	owner  => 'www-data',
	group  => 'www-data',
	mode   => '0644',
}

# You can add more resources if needed to address other issues discovered
