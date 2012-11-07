#!/bin/sh

sed "s|STATIC_ROOT|$(pwd)/static_root/|" nginx.conf.template > nginx.conf
nginx -c $(pwd)/nginx.conf

./manage.py collectstatic --noinput --settings=demo_site.nginx_settings

echo "**** Access running server at http://localhost:8080 ****"
./manage.py runserver --settings=demo_site.nginx_settings

echo "**** App-server stopped. Stopping nginx... ****"
nginx -s stop
echo "**** nginx stopped. ****"
