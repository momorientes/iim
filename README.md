# Infodesk Help Database v2

## Install

Get `docker` and `docker-compose` for your plattform (sorry for the hipster)

Then `alias dc=docker-compose`
```
dc build
dc up -d
dc run web migrate
dc run web createsuperuser
```

Go to `http://localhost:8000` and login with the superuser credentials. You're good to go!

## Nginx (optional)
```
upstream infodesk_server{
     server localhost:8000; 
}

server {
    listen 80;
    listen [::]:80;
    server_name infodesk.xyz; 
    server_name infodesk.xyz;

    access_log /var/log/ihdb2-nginx-access.log;
    error_log /var/log/ihdb2-nginx-error.log;

    client_max_body_size 32M;


    location / {
        proxy_redirect off;
        proxy_buffering off;
        proxy_set_header        Host            $http_host;
        proxy_set_header        X-Real-IP       $remote_addr;
        proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header        X-Forwarded-Proto $scheme;
        if (!-f $request_filename) {
            proxy_pass http://infodesk_server;
            break;
        }
    }
}
```
