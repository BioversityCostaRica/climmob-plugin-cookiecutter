{% if cookiecutter.plugin_hasCeleryTasks == 'Y' or cookiecutter.plugin_hasCeleryTasks == 'y' %}
from climmob.config.celery_app import celeryApp
import time

@celeryApp.task
def pluginTask():
    time.sleep(30) #Just to test that such sleep is handled by celery and does not hang Climmob
    print "pluginTask finished"
{% endif %}