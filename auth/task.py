from models import Sample
from celery.decorators import task

@task()
def add():
	try:
		a = sample.objects.all(pk=1)
	except:
		sc = sample()
	sc.num = sc.num + 1
	sc.save()