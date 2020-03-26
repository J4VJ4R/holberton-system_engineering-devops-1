# Puppet manifest to install nginx

package { 'nginx':
  ensure => installed,
}

file { 'default_page':
  path    => '/var/www/html/index.html',
  content => 'Holberton School',
}

file_line { 'redirection':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
