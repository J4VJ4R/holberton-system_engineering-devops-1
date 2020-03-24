# Create a file in /tmp

file { '/tmp/holberton':
  mode => '0744',
  owner => 'www-data',
  grup => 'www-data',
  content => 'I love Puppet',
}
