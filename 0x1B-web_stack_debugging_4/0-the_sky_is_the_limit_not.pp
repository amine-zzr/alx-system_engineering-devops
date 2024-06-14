# Increase the ULIMIT for Nginx
exec { 'increase_ulimit_for_nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin', '/usr/bin', '/sbin', '/usr/sbin'],
  onlyif  => 'grep -q "ULIMIT" /etc/default/nginx',
  notify  => Exec['restart_nginx'],
}

# Restart Nginx
exec { 'restart_nginx':
  command     => 'service nginx restart',
  path        => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
  refreshonly => true,
}
