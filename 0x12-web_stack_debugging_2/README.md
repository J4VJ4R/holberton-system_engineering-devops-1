# Web stack debugging #2, challenge
This repository contains information about bellow applied concepts:
* Web stack debugging

## Requirements
- Ubuntu Linux 14.04 LTS
- Nginx

## Context
![99 little bugs](https://github.com/gogomillan/holberton-system_engineering-devops/blob/master/0x12-web_stack_debugging_2/assets/99littlebugs.jpg)

## Challenges

###  0. Run software as another user
In Linux, a good practice is that one should never be logged in the root user.
Thats why it is preferable to run as a privileged user, meaning that the user
also has the ability to perform tasks that the root user can do.  
Bash script that accepts one argument.

**Example**
```bash wrap
root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeonelese www-data
www-data
root@ubuntu:~# whoami
root
root@ubuntu:~#
```

###  1. Run Nginx as Nginx
It's a good practice not to run your web servers as root (which is the default
for most configurations) and instead run the process as the less privileged
nginx user instead.  
Bash script that Fix this so Nginx will run as the nginx user.

**Example**
```bash wrap
root@ab6f4542747e:~# ps auxff | grep ngin[x]
nginx      884  0.0  0.0  77360  2744 ?        Ss   19:16   0:00 nginx: master process /usr/sbin/nginx
nginx      885  0.0  0.0  77712  2772 ?        S    19:16   0:00  \_ nginx: worker process
nginx      886  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      887  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      888  0.0  0.0  77712  3208 ?        S    19:16   0:00  \_ nginx: worker process
root@ab6f4542747e:~#
root@ab6f4542747e:~# nc -z 0 8080 ; echo $?
0
root@ab6f4542747e:~#
```

###  2. 7 lines or less
Using previos point script:
- Bash script with less than 7 lines long
- Whithout ;
- Whithout &&

**Example**
```bash wrap
root@ab6f4542747e:~# ps auxff | grep ngin[x]
nginx      884  0.0  0.0  77360  2744 ?        Ss   19:16   0:00 nginx: master process /usr/sbin/nginx
nginx      885  0.0  0.0  77712  2772 ?        S    19:16   0:00  \_ nginx: worker process
nginx      886  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      887  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      888  0.0  0.0  77712  3208 ?        S    19:16   0:00  \_ nginx: worker process
root@ab6f4542747e:~#
root@ab6f4542747e:~# nc -z 0 8080 ; echo $?
0
root@ab6f4542747e:~#
```

## Author
Gonzalo Gomez Millan | :octocat: [GitHub](https://github.com/gogomillan)
