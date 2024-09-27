# Puppet script to fix Apache 500 error 

file { '/var/www/html/index.php':
   ensure => file,
   owner   => 'www-data',
   group   => 'www-data',
   mode     => '0644',
} 

service { 'apache2':
   ensure         => running,
   enable         => true,
   hasrestart => true,
   subscribe   => File['/var/www/html/index.php'],
} 

exec { 'fix-wordpress':
   command => '/usr/bin/chown -R www-data:www-data /var/www/html',
   onlyif   => 'test $(stat -c %U /var/www/html/index.php) != "www-data"',
   notify   => Service['apache2'],
}
