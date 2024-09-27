exec { 'change-os-configuration-for-holberton-user':
  command => '/bin/bash -c "echo \'holberton soft nofile 4096\' >> /etc/security/limits.conf && echo \'holberton hard nofile 4096\' >> /etc/security/limits.conf"',
}
