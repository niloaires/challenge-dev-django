import datetime
import logging
from celery import shared_task
from apps.cadastros.models import PropostasModel

log = logging.getLogger(__name__)


@shared_task()
def avaliar_propostas(pk):
    """
    Método que avalia as propostas e define se será aprovada ou não.
    O desafio menciona nos requistos que metada das propostas devem
    ser aprovadas. Em uma aplicação real, esse método deveria contar o
    número de propostas aceitas e recusadas para com base nessa informação,
    decidir sobre a proposta em análise, como segue.
    .
    """
    agora = datetime.datetime.now()
    proposta_em_analise = PropostasModel.objects.get(pk=pk)
    propostas_aprovadas = PropostasModel.objects. \
        filter(aprovada=True).count()
    propostas_reprovadas = PropostasModel.objects. \
        filter(aprovada=False).count()
    """
    Se não houver propostas aprovadas ou reprovadas, 
    aprovará a proposta.
    """

    if propostas_aprovadas is None and propostas_reprovadas is None:
        proposta_em_analise.data_avaliacao = agora
        proposta_em_analise.aprovada = True
        proposta_em_analise.save()
        log.info('Proposta aprovada: {}'.format(proposta_em_analise))
    elif propostas_aprovadas > propostas_reprovadas:
        """
        Se o número de propostas aprovadas 
        for maior que o número de propostas aprovadas,
        a proposta será reprovada.
        """
        proposta_em_analise.data_avaliacao = agora
        proposta_em_analise.aprovada = False
        proposta_em_analise.save()
        log.info('Proposta reprovada: {}'.format(proposta_em_analise))
    elif propostas_aprovadas < propostas_reprovadas:
        """
        Se o número de propostas aprovadas 
        for menor que o número de propostas reprovadas,
        a proposta será aprovada.
        """
        proposta_em_analise.data_avaliacao = agora
        proposta_em_analise.aprovada = True
        proposta_em_analise.save()
        log.info('Proposta aprovada: {}'.format(proposta_em_analise))
    else:
        proposta_em_analise.data_avaliacao = agora
        proposta_em_analise.aprovada = False
        proposta_em_analise.save()
        log.info('Proposta reprovada: {}'.format(proposta_em_analise))
