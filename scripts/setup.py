import subprocess
import os

# Definir variables
domain = "localhost"
postfix_log = "/var/log/mail.log"
apache_log = "/var/log/apache2/error.log"
roundcube_dir = "/var/www/html/roundcube"
postfix_conf = "/etc/postfix/main.cf"
apache_conf = "/etc/apache2/sites-available/000-default.conf"
roundcube_conf = "/usr/share/roundcube/config/config.inc.php"

# Función para ejecutar comandos del sistema
def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"Error ejecutando comando: {command}")
        print(f"Error: {result.stderr.decode()}")
        exit(1)
    return result.stdout.decode()

# 1. Configuración de Apache: Habilitar FollowSymLinks en Apache
print("Verificando configuración de Apache para FollowSymLinks...")
if "Options FollowSymLinks" not in open(apache_conf).read():
    print("Añadiendo 'Options FollowSymLinks' a la configuración de Apache...")
    run_command(f"sudo sed -i '/<Directory /var/www/html/roundcube>/a \ \ Options FollowSymLinks' {apache_conf}")
    run_command("sudo systemctl restart apache2")
else:
    print("Ya está habilitado FollowSymLinks en la configuración de Apache.")

# 2. Verificar y reiniciar Apache
print("Reiniciando Apache...")
run_command("sudo systemctl restart apache2")
if "active (running)" not in run_command("systemctl status apache2"):
    print("Apache no pudo iniciarse. Revisa los logs de errores.")
    print(run_command(f"tail -n 20 {apache_log}"))
    exit(1)

# 3. Configuración de Postfix: Verificar configuración básica
print("Verificando configuración de Postfix...")
with open(postfix_conf, 'r') as f:
    if 'mydomain' not in f.read():
        print("Configurando dominio en Postfix...")
        run_command(f"sudo sed -i 's/#mydomain = /mydomain = {domain}/' {postfix_conf}")
        run_command("sudo systemctl restart postfix")

# 4. Verificar estado de Postfix
print("Verificando el estado de Postfix...")
if "active (running)" not in run_command("systemctl status postfix"):
    print("Postfix no pudo iniciarse. Revisa los logs de Postfix.")
    print(run_command(f"tail -n 20 {postfix_log}"))
    exit(1)

# 5. Verificación de Dovecot (si se usa)
print("Revisando el estado de Dovecot...")
if "active (running)" not in run_command("systemctl status dovecot"):
    print("Dovecot no está activo. Reiniciando...")
    run_command("sudo systemctl restart dovecot")
    if "active (running)" not in run_command("systemctl status dovecot"):
        print("Dovecot no pudo iniciarse. Revisa los logs de Dovecot.")
        exit(1)

# 6. Verificar los logs de Roundcube
print("Revisando logs de Roundcube...")
if os.path.exists("/var/log/roundcube/errors"):
    print(run_command("tail -n 20 /var/log/roundcube/errors"))
else:
    print("No se encontró el archivo de log de Roundcube. Verifica su configuración.")

# 7. Verificación del puerto de Postfix
print("Verificando si el puerto 25 está disponible (SMTP)...")
telnet_result = subprocess.run("telnet localhost 25", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if telnet_result.returncode == 0:
    print("Postfix está escuchando en el puerto 25.")
else:
    print("No se pudo conectar al puerto 25. Verifica si Postfix está correctamente configurado.")
    exit(1)

print("Proceso de configuración automatizado completado.")
