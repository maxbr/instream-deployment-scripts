#!/bin/bash


function api_response {
    curl -skL http://127.0.0.1:8080/v2/tasks -H "Accept: text/plain"
}

function header {
cat <<EOF
global
  daemon
  log 127.0.0.1 local0
  log 127.0.0.1 local1 notice
  maxconn 4096

defaults
  log            global
  retries             3
  maxconn          2000
  timeout connect  5000
  timeout client  50000
  timeout server  50000

listen stats
  bind 127.0.0.1:9090
  balance
  mode http
  stats enable
  stats auth admin:admin
EOF
}

function apps {
  (until api_response; do [ $# -lt 2 ] && return 1 || shift; done) | while read -r row; do
    set -- $row
    local app="$1"
    local port="$2"

    shift 2

    if [ ! -z "${port##*[!0-9]*}" ]; then
      cat <<EOF

listen ${app}-${port}
  bind 0.0.0.0:${port}
  mode tcp
  option tcplog
  balance leastconn
EOF
      while [[ $# -ne 0 ]]; do
        printf '%s\n' "  server ${app}-$# $1 check" ;
        shift
      done
    fi
  done
}

header > /etc/haproxy/haproxy.cfg.new
apps >> /etc/haproxy/haproxy.cfg.new

if ! cmp -s /etc/haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg.new; then
  mv /etc/haproxy/haproxy.cfg.new /etc/haproxy/haproxy.cfg
  ports=`grep listen /etc/haproxy/haproxy.cfg | sed -n 's/listen \(.*\)\-\([0-9]*\)/\2/p'`

  for port in "${ports[@]}"; do
    iptables -I INPUT -p tcp --dport ${port} --syn -j DROP
  done

  /usr/sbin/haproxy -f /etc/haproxy/haproxy.cfg -p /var/run/haproxy.pid -sf $(cat /var/run/haproxy.pid)

  for port in "${ports[@]}"; do
    iptables -D INPUT -p tcp --dport ${port} --syn -j DROP
  done
fi