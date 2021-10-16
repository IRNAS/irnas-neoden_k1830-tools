# Raspberry Pi Security configration

## Change default password
1. Set a new root password using `passwd`

## Change default username
1. Create new user with `sudo adduser <user>`
2. Set selected password and enter data
3. Add user to the `sudo` group with `sudo usermod -a -G adm,dialout,cdrom,sudo,audio,video,plugdev,games,users,input,netdev,gpio,i2c,spi <user>`

## Make sudo require a password
1. Force sudo to require a password with `sudo visudo /etc/sudoers.d/010_pi-nopasswd`
2. Change the content of the file to 
```
pi ALL=(ALL) PASSWD: ALL
<user> ALL=(ALL) PASSWD: ALL
```

## Allow only certain users to login using ssh
1. Edit the sshd configuration with `sudo nano /etc/ssh/sshd_config`
2. Append the following line to the end of the file: 
```
AllowUsers <user>
DenyUsers pi
```
3. Restart the sshd service for the changes to take effect `sudo systemctl restart ssh`

## Install a Firewall
1. Install `ufw` using `sudo apt install ufw`
2. Enable the firewall with `sudo ufw enable`
3. Allow the ssh service through the firewall with `sudo ufw allow ssh`

## Configure firewall to allow Neoden local traffic (cameras will not work without this)
1. Run command `sudo ufw allow from 192.168.1.0/24`

## Install fail2ban
1. Install `fail2ban` using `sudo apt install fail2ban`
2. Copy `jail.conf` to `jail.local` to enable `fail2ban` using
```
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
sudo nano /etc/fail2ban/jail.local
```
3. To allow a maximum of 6 retries on login attempts append the following:
```
[ssh]
enabled  = true
port     = ssh
filter   = sshd
logpath  = /var/log/auth.log
maxretry = 6
```
4. After the maximum number of retries has been reached `fail2ban` will ban all access on all ports
