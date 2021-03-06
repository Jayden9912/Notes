# VNC (Virtual Network Computing) on VPN
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
Download Putty and TightVNC Viewer in Windows **AND**
Download x11vnc in Ubuntu
```
sudo apt-get update && sudo apt-get install x11vnc
```

Set up password file
```
mkdir ~/.x11vnc
x11vnc -storepasswd /home/user/.x11vnc/passwd
```

### 4
Set up SSH connection in Putty

Fill in the username of the Server (optional)

![putty2](https://user-images.githubusercontent.com/85933053/153229811-f308c681-d7eb-4945-98af-84542ae6b73d.jpg) 

Fill in host ip address, give this session a name and click save (change the port if necessary, default ssh port is 22)

![putty1](https://user-images.githubusercontent.com/85933053/153229962-d7eb6543-5b65-4cb8-82f5-a5f61afe7627.jpg) 

After saving, open the session that you just saved under default settings and enter the user's password when prompted.
### 5
Once the SSH connection is established, launch the x11vnc
```
x11vnc -usepwd -display :0
```

### 6
Open TightVNC Viewer  
Type in host_ip_addresss::5900 and click connect  
Enter the x11vnc password when prompted

### VPN is one of the way to secure the VNC connection. SSH and SSL can be used too. SSH have be done by port forwarding to the localhost. However, loopback connection will cause "cascading windows" effect and it defeats the purpose of screensharing.
