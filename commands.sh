docker-compose -f docker-compose.prod.yml exec web python manage.py migrate
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser