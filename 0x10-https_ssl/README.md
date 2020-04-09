# 0x10. HTTPS SSL challenge
This repository contains information about bellow applied conceptsr.

## Topics
- DNS
- What is HTTPS?
- What are the 2 main elements that SSL is providing
- HAProxy SSL termination on Ubuntu16.04
- SSL termination
- Bash function

## Requirements
- Linux Ubuntu 16.04 LTS
- Shellcheck (version 0.3.7)

## Context
![https](https://github.com/gogomillan/holberton-system_engineering-devops/blob/master/0x10-https_ssl/assets/https_haproxy.png)

## Challenges

###  1. World wide web
Bash script that will display information about subdomains,
after configuration the domain zone so that the subdomain www points to your load-balancer IP (lb-01).

**Example:**
```bash wrap
sylvain@ubuntu$ dig www.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
www.holberton.online.   87  IN  A   54.210.47.110
sylvain@ubuntu$ dig lb-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
lb-01.holberton.online. 101 IN  A   54.210.47.110
sylvain@ubuntu$ dig web-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-01.holberton.online. 212    IN  A   34.198.248.145
sylvain@ubuntu$ dig web-02.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-02.holberton.online. 298    IN  A   54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$
sylvain@ubuntu$ ./1-world_wide_web holberton.online
The subdomain www is a A record and points to 54.210.47.110
The subdomain lb-01 is a A record and points to 54.210.47.110
The subdomain web-01 is a A record and points to 34.198.248.145
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$ ./1-world_wide_web holberton.online web-02
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
```

###  2. HAproxy SSL termination
Terminating SSL on HAproxy means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.
With a certificate using certbot it is configured a HAproxy to accept encrypted traffic for subdomain www.


**Example:**
```
sylvain@ubuntu$ curl -sI https://www.holberton.online
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 01:52:04 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes
sylvain@ubuntu$
sylvain@ubuntu$ curl https://www.holberton.online
Holberton School for the win!
sylvain@ubuntu$
```
