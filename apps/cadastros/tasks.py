import logging
from celery import shared_task
from propostas.celery import app
from celery.schedules import crontab
from apps.cadastros.models import PropostasModel
from datetime import timedelta

log = logging.getLogger(__name__)


@shared_task()
def avaliacao_propostas():
    """
    Método que agenda a avaliação das propostas.
    """
    try:
        qs = PropostasModel.objects.all()
        n = 1
        for i in qs:
            if i.pk % 2 == 0:
                i.status = 'Aprovada'
                i.avaliada = True
                i.save(update_fields=['avaliada', 'status'])
            else:
                i.status = 'Reprovada'
                i.avaliada = True
                i.save(update_fields=['avaliada', 'status'])
            n + 1
            print("Proposta {} de {} avaliada".format(n, qs.count()))
    except Exception as e:
        log.error('Erro ao avaliar as propostas: {}'.format(e))


app.conf.beat_schedule = {
    'execução a cada 5 minutos': {
        'task': 'apps.cadastros.tasks.avaliacao_propostas',
        'schedule': timedelta(minutes=5),

    }
}
