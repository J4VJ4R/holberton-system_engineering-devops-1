# Firewall challenge
This repository contains information about firewall and web stack debugging:

## Topics
- What is a firewall
- Tools for server and web debugging
- telnet
- ufw

## Context
![firewall diagram](https://github.com/gogomillan/holberton-system_engineering-devops/blob/master/0x13-firewall/assets/firewall.png)
  
**BTW:** Your servers **_without_** a firewall...  
  
![firewall gif](https://github.com/gogomillan/holberton-system_engineering-devops/blob/master/0x13-firewall/assets/without-firewall.gif)

## Challenges

###  1. Block all incoming traffic but
Using the ufw firewall to setup a few rules.

**Example**
```bash wrap
vagrant@gc-server-1585025307:~$ sudo ufw status verbose
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), deny (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW IN    Anywhere
80/tcp                     ALLOW IN    Anywhere
443/tcp                    ALLOW IN    Anywhere
22/tcp (v6)                ALLOW IN    Anywhere (v6)
80/tcp (v6)                ALLOW IN    Anywhere (v6)
443/tcp (v6)               ALLOW IN    Anywhere (v6)

vagrant@gc-server-1585025307:~$
```

###  2. Port forwarding
Firewalls can not only filter requests, they can also forward them.
