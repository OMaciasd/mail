# **Mail Server Setup and Contribution Guide for Ubuntu** ✉️

## **Contents** 📚

- [Mail Server Setup on Ubuntu](#mail-server-setup-on-ubuntu)
  - 🔄 **Restart Postfix**
  - 📥 **Setting Up Dovecot**
    - [**Install Dovecot**](#install-dovecot)     
    - [⚙️Configure Dovecot](#configure-dovecot-)
    - [🔄 Restart Dovecot](#restart-dovecot-)
  - [🔐 Configuring SSL/TLS with Certbot](#configuring-ssltls-with-certbot)
    - [🔧 Install Certbot](#install-certbot-)
    - [🔑 Obtain SSL Certificates](#obtain-ssl-certificates-)
    - [🔒 Configure Postfix and Dovecot to Use SSL/TLS](#configure-postfix-and-dovecot-to-use-ssltls-)
    - [🔄 Restart Both Services](#restart-both-services-)
  - [🛠️ Workflow](#workflow)
    - [👤 Creating Mailboxes and Users](#creating-mailboxes-and-users-)
  - [🔍 Testing and Verification](#testing-and-verification)
    - [📧 Testing Mail Sending/Receiving](#testing-mail-sendingreceiving-)
    - [📂 Log File Analysis](#log-file-analysis-)
  - [✏️ Commit Messages](#commit-messages)
  - [🚀 Submitting Pull Requests](#submitting-pull-requests)
  - [🧐 Code Review](#code-review)
  - [📂 Verifying the Mail Server Pipeline](#verifying-the-mail-server-pipeline)
    - [CI/CD Pipeline](#cicd-pipeline)
    - [View Logs](#view-logs)
  - [📝 Documentation Contributions](#documentation-contributions)

## 🧩 **Project Structure**

- **config/**: Contains configuration files for Postfix, Dovecot, SSL certificates, and other mail-related setups.  
- **scripts/**: Scripts for automating mail server tasks such as creating users, setting up SSL certificates, or testing mail functionality.  
- **tests/**: Test cases and logs for verifying mail server operations, including sending/receiving emails.

## 🔒 **Managing Sensitive Files**

### `.env` Files

- **Description**: The **`.env`** file contains sensitive information such as email server credentials, API keys for mail-related services, and SSL configuration settings.
- **Setup**: Create a **`.env`** file in the root of the project based on the **`.env-example.txt`** template. This file should contain sensitive email server credentials, like SMTP and IMAP details.
- **Important**: The **`.env`** file is added to **`.gitignore`** to prevent sensitive information from being committed to version control.

### Configuration Files

- **Description**: The configuration files define the settings for the mail server, including SMTP (Postfix) and IMAP/POP3 (Dovecot) settings, as well as SSL/TLS configurations.
- **Example Files**: Use **`config-example.txt`** as a template to set up your mail configurations.

## ⚙️ **Setting Up the Mail Server Environment**

### 📤 **Installing Postfix**

1. **Install Postfix**: Postfix will be used to send emails through SMTP.

   ```bash
   sudo apt update
   sudo apt install postfix

   ```

## ⚙️ **Setting Up the Mail Server Environment**

### 📤 **Configure Postfix**

1. **Install Postfix**:  
   Postfix is used for sending emails through SMTP.

   ```bash
   sudo apt update
   sudo apt install postfix

   ```

## 📤 **Postfix Configuration**

### ⚙️ **Edit `/etc/postfix/main.cf` to configure basic SMTP settings**

```bash
sudo nano /etc/postfix/main.cf

```

## **Example Configuration**

### Postfix Configuration Example:

```bash
myhostname = mail.example.com
mydomain = example.com
myorigin = $mydomain
inet_interfaces = all
inet_protocols = ipv4

```


## 🔄 **Restart Postfix**

To apply the changes, restart the Postfix service:

```bash
sudo systemctl restart postfix

```

## 📥 **Setting Up Dovecot**

### 📩 **Install Dovecot**

Dovecot will handle the IMAP/POP3 protocols for retrieving mail.

```bash
sudo apt install dovecot-core dovecot-imapd

```

## **⚙️ Configure Dovecot**

1. **Edit `/etc/dovecot/dovecot.conf`** to configure mail retrieval settings:

    ```bash
    sudo nano /etc/dovecot/dovecot.conf
    
    ```

2. **Example Configuration**:

    ```bash
    listen = *
    mail_location = maildir:~/Maildir
    service imap-login {
        inet_listener imap {
            port = 0
        }
        inet_listener imaps {
            port = 993
            ssl = yes
        }
    }
    
    ```

## **🔄 Restart Dovecot**

- **Restart Dovecot** to apply the configuration:

    ```bash
    sudo systemctl restart dovecot
    
    ```

## **🔐 Configuring SSL/TLS with Certbot**

### **🔧 Install Certbot**

- **Certbot** is used to enable SSL encryption for secure email communication:

    ```bash
    sudo apt install certbot
    
    ```

### **🔑 Obtain SSL Certificates**

- Use Certbot to obtain SSL certificates for your mail domain:

    ```bash
    sudo certbot certonly --standalone -d mail.example.com
    
    ```

### **🔒 Configure Postfix and Dovecot to Use SSL/TLS**

- **For Postfix**, edit `/etc/postfix/main.cf`:

    ```bash
    smtpd_tls_cert_file=/etc/letsencrypt/live/mail.example.com/fullchain.pem
    smtpd_tls_key_file=/etc/letsencrypt/live/mail.example.com/privkey.pem
    smtpd_use_tls=yes
    ```

- **For Dovecot**, edit `/etc/dovecot/conf.d/10-ssl.conf`:

    ```bash
    ssl = required
    ssl_cert = </etc/letsencrypt/live/mail.example.com/fullchain.pem
    ssl_key = </etc/letsencrypt/live/mail.example.com/privkey.pem
    ```

### **🔄 Restart Both Services**

- **Restart both Postfix and Dovecot**:

    ```bash
    sudo systemctl restart postfix
    sudo systemctl restart dovecot
    ```

---

## **🛠️ Workflow**

### **👤 Creating Mailboxes and Users**

- Use **Postfix** and **Dovecot** together to create and manage user mailboxes. You can create system users who will have their mailboxes.

    To add a user, run:

    ```bash
    sudo adduser user@example.com
    ```

    This will create the user and a corresponding mailbox.

---

## **🔍 Testing and Verification**

### **📧 Testing Mail Sending/Receiving**

- **Sending Email**: To verify that Postfix is working, use `mail` or another mail client to send an email.

    Example using `mail`:

    ```bash
    echo "Test Email" | mail -s "Subject" user@example.com
    ```

- **Receiving Email**: Check that you can retrieve email via IMAP. You can use a mail client like Thunderbird or use the command line with `telnet` to connect to the IMAP server on port 993.

### **📂 Log File Analysis**

- **Check mail logs** in `/var/log/mail.log` to troubleshoot any issues.

---

## **✏️ Commit Messages**

- Use clear and descriptive commit messages to document changes to the mail server setup, such as:

    - `Add Postfix configuration for secure email sending`
    - `Configure Dovecot to handle IMAP with SSL`

---

## **🚀 Submitting Pull Requests**

- When submitting pull requests, include descriptions of the changes made and their impact on mail server setup or security.

---

## **🧐 Code Review**

- **Pull requests** will be reviewed to ensure compliance with best practices for email server setup and security.

---

## **📂 Verifying the Mail Server Pipeline**

### **CI/CD Pipeline**

- Verify that the **CI/CD pipeline** includes tests for email functionality.

### **View Logs**

- Each pipeline step should provide logs for mail server setup, email sending/receiving, and SSL verification.

---

## **📝 Documentation Contributions**

- Contributions to documentation should be submitted as part of a pull request, describing any new configuration setups, troubleshooting steps, or changes to mail server components.
