# kills a process named killmenow.

exec { 'kill_process':
    command => 'pkill killmenow',
    path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
}
