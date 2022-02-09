# VNC (Virtual Network Computing)
### Host: Ubuntu
### Client: Windows

This method only works if **both host and client** are on the **same** network. If the host is not on the same network as client, port forwarding is required.

### 1
First, check if openssh is installed in Ubuntu
```
ssh localhost
```
If the output is connection refused etc, install ssh server
```
sudo apt-get install openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh
```
Check if the ssh service is running
```
sudo service ssh status
```
### 2
Check that connection can be established between host and client.
In windows, open powershell
```
ping username@server_private_ip_address
```
Ip address can be checked by (in Ubuntu)
```
ifconfig
```
or in Windows
```
ipconfig
```
### 3
Download Putty and TightVNC Viewer in Windows

### 4
Set up SSH tunnel in Putty

