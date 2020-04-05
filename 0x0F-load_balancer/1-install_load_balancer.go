#!/usr/bin/env bash
#configures a new Ubuntu machine haproxy

sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:vbernat/haproxy-1.8
sudo apt-get -y update
sudo apt-get -y install haproxy
sudo bash -c 'echo "ENABLED=1" >> /etc/default/haproxy'
sudo cp /etc/haproxy/haproxy.cfg .

sudo bash -c 'echo "frontend front
        bind *:80
        mode http
        default_backend back
backend back
    balance roundrobin
    server 1240-web-01 35.196.121.157:80 check
    server 1240-web-02 184.72.77.114:80 check" >> /etc/haproxy/haproxy.cfg'

sudo service haproxy restart
