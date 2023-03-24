# This manifest kills a process called `Killmenow`

$procx_name = 'Killmenow'
exec {"kill_${procx_name}":
  command => "/usr/bin/pkill ${procx_name}",
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
