sudo amazon-linux-extras install epel -y
sudo yum install stress -y

stress --cpu 4 --timeout 300s