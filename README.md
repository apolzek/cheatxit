# cheatxit
📑 Cheat sheet for professionals working with technology


## Topics

### Python

* Use venv on Linux (Debian10)
```
sudo pip3 install virtualenv
virtualenv venv
source venv/bin/activate
deactivate
pip install -r requirements.txt
```

### Linux

* Check if port is in use on Linux
```
cat /etc/services
grep -w '443/tcp' /etc/services
egrep -w '22/(tcp|udp)' /etc/services

sudo lsof -i -P -n | grep LISTEN
sudo netstat -tulpn | grep LISTEN
sudo lsof -i:22 ## see a specific port such as 22
sudo lsof -nP -iTCP -sTCP:LISTEN

sudo watch ss -tulpn
sudo ss -tulw
sudo ss -tulwn 
# -t : Show only TCP sockets on Linux
# -u : Display only UDP sockets on Linux
# -l : Show listening sockets. For example, TCP port 22 is opened by SSHD server.
# -p : List process name that opened sockets
# -n : Don’t resolve service names i.e. don’t use DNS

sudo nmap -sT -O localhost
sudo nmap -sU -O 192.168.2.13 ##[ list open UDP ports ]##
sudo nmap -sT -O 192.168.2.13 ##[ list open TCP ports ]##

```
