Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  config.vm.network "public_network", type: "dhcp", bridge: "Intel(R) Ethernet Connection"
  config.vm.network "public_network", bridge: true

  config.vm.hostname = "mail-server"
  
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get upgrade -y
    
    sudo apt-get install -y postfix dovecot-core dovecot-imapd dovecot-pop3d

    sudo apt-get install -y roundcube roundcube-core apache2 libapache2-mod-php
    
    sudo postconf -e 'home_mailbox = Maildir/'
    sudo postconf -e 'mailbox_command ='
    sudo postconf -e 'inet_interfaces = all'
    sudo postconf -e 'inet_protocols = all'
    
    sudo sed -i 's/#mail_location =/mail_location = maildir:~\/Maildir/' /etc/dovecot/conf.d/10-mail.conf
    sudo sed -i 's/#disable_plaintext_auth = yes/disable_plaintext_auth = no/' /etc/dovecot/conf.d/10-auth.conf
    
    sudo systemctl restart postfix
    sudo systemctl restart dovecot
    sudo systemctl restart apache2
    
    sudo adduser user1 --gecos "User One,,," --disabled-password
    echo "user1:password" | sudo chpasswd
  SHELL
  
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 25, host: 2525
  config.vm.network "forwarded_port", guest: 143, host: 1143
  config.vm.network "forwarded_port", guest: 110, host: 1010
end
