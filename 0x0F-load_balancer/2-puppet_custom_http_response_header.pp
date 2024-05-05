exec { 'apt-update':
  command => '/usr/bin/apt update',
  refreshonly => true,  # Only execute when needed
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-update'],  # Ensure apt-update runs first
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],  # Ensure nginx is installed first
}

# Add a custom header to nginx configuration
file_line { 'nginx_custom_header':
  path    => '/etc/nginx/sites-available/default',
  line    => '    add_header X-Served-By $hostname;',
  match   => '^    location / {$',
  after   => '^    location / {$',
  require => Package['nginx'],
  notify  => Service['nginx'],  # Restart nginx when the config changes
}

service { 'nginx':
  ensure => running,
  enable => true,
}
