# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Configure Nginx server block
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html;

    location / {
        return 200 'Hello World!\n';
    }

    add_header X-Served-By ${hostname};
    location /redirect_me {
        return 301 https://github.com/amine-zzr;
    }
}
",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Enable default server block
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}
