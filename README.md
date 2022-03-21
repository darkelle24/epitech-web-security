# epitech-web-security

[http://api.epitech-owasp-2022.com/](http://api.epitech-owasp-2022.com/)

[http://epitech-owasp-2022.com/](http://epitech-owasp-2022.com/)


```
#!/bin/bash

sudo yum update

sudo yum install docker

wget https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) 

sudo mv docker-compose-$(uname -s)-$(uname -m) /usr/local/bin/docker-compose

sudo chmod -v +x /usr/local/bin/docker-compose

sudo systemctl enable docker.service

sudo systemctl start docker.service

```