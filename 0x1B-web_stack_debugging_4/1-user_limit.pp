# Increase file descriptor limits for the holberton user
file { '/etc/security/limits.conf':
  ensure  => file,
  content => 'holberton soft nofile 4096
holberton hard nofile 8192',
}
