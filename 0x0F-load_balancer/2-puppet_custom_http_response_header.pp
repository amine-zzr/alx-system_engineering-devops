# Custom HTTP header in a nginx server

# update ubuntu server
exec { 'update package list':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}

# install nginx on server
package { 'nginx':
  ensure   => present,
  provider => 'apt'
}

# custom Nginx response header
file_line { 'configure X-Served-By header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
  provider => 'augeas',
}

# start the service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}
