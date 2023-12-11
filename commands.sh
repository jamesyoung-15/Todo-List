sudo docker-compose -f docker-compose.prod.yml exec web python manage.py migrate &&
sudo docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear &&
sudo docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser