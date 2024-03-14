sudo yum update -y

sudo yum install -y httpd

sudo systemctl start httpd

echo "Salam Level Up In Tech2 from $(hostname -f)" >  /var/www/html/index.html 