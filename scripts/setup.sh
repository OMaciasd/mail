#!/bin/bash

# Definir variables
DOMAIN="localhost"
POSTFIX_LOG="/var/log/mail.log"
APACHE_LOG="/var/log/apache2/error.log"
ROUND_CUBE_DIR="/var/www/html/roundcube"
POSTFIX_CONF="/etc/postfix/main.cf"
APACHE_CONF="/etc/apache2/sites-available/000-default.conf"
ROUNDCUBE_CONF="/usr/share/roundcube/config/config.inc.php"

# 1. Configuración de Apache: Habilitar FollowSymLinks en Apache
echo "Verificando configuración de Apache para FollowSymLinks..."
if ! grep -q "Options FollowSymLinks" $APACHE_CONF; then
    echo "Añadiendo 'Options FollowSymLinks' a $APACHE_CONF..."
    sudo sed -i '/<Directory \/var\/www\/html\/roundcube>/a \ \ Options FollowSymLinks' $APACHE_CONF
    sudo systemctl restart apache2
else
    echo "Ya está habilitado FollowSymLinks en la configuración de Apache."
fi

# 2. Verificar y reiniciar Apache
echo "Reiniciando Apache..."
sudo systemctl restart apache2
if systemctl is-active --quiet apache2; then
    echo "Apache está activo y funcionando."
else
    echo "Apache no pudo iniciarse. Revisa los logs de errores: $APACHE_LOG"
    tail -n 20 $APACHE_LOG
    exit 1
fi

# 3. Configuración de Postfix: Verificar configuración básica
echo "Verificando configuración de Postfix..."
if ! grep -q "mydomain" $POSTFIX_CONF; then
    echo "Configurando dominio en Postfix..."
    sudo sed -i "s/#mydomain = /mydomain = $DOMAIN/" $POSTFIX_CONF
    sudo systemctl restart postfix
fi

# 4. Verificar estado de Postfix
echo "Verificando el estado de Postfix..."
if systemctl is-active --quiet postfix; then
    echo "Postfix está activo y funcionando."
else
    echo "Postfix no pudo iniciarse. Revisa los logs de Postfix: $POSTFIX_LOG"
    tail -n 20 $POSTFIX_LOG
    exit 1
fi

# 5. Verificación de Dovecot (si se usa)
echo "Revisando el estado de Dovecot..."
if systemctl is-active --quiet dovecot; then
    echo "Dovecot está activo y funcionando."
else
    echo "Dovecot no está activo. Reiniciando..."
    sudo systemctl restart dovecot
    if systemctl is-active --quiet dovecot; then
        echo "Dovecot ahora está activo."
    else
        echo "Dovecot no pudo iniciarse. Revisa los logs de Dovecot."
        exit 1
    fi
fi

# 6. Verificar los logs de Roundcube
echo "Revisando logs de Roundcube..."
if [ -f "/var/log/roundcube/errors" ]; then
    tail -n 20 /var/log/roundcube/errors
else
    echo "No se encontró el archivo de log de Roundcube. Verifica su configuración."
fi

# 7. Verificación del puerto de Postfix
echo "Verificando si el puerto 25 está disponible (SMTP)..."
telnet localhost 25
if [ $? -eq 0 ]; then
    echo "Postfix está escuchando en el puerto 25."
else
    echo "No se pudo conectar al puerto 25. Verifica si Postfix está correctamente configurado."
    exit 1
fi

echo "Proceso de configuración automatizado completado."
