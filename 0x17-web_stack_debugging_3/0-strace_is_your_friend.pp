# Configure Apache and update wp-settings.php to use correct PHP version

exec { 'update_wp_settings':
  command =>'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin:/bin/',
  onlyif  => 'grep -q phpp /var/www/html/wp-settings.php',
}
