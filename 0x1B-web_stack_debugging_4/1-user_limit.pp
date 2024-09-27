exec { 'change-os-configuration-for-holberton-user':
	command => 'echo "holberton soft nofile 4096" >> /etc/security/limits.conf && echo "holberton hard nofile 4096" >> /etc/security/limits.conf',
	path    => ['/bin', '/usr/bin'],
	unless  => 'grep -q "holberton" /etc/security/limits.conf',
}
