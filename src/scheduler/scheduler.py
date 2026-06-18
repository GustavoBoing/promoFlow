
#from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.jobstores.memory import MemoryJobStore

from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

from apscheduler import events

from src.providers.mercado_livre_provider import MercadoLivreProvider
from src.services.pipeline_service import PipelineService

#backgroundScheduler
#cron e interval

# ==========================================
# 1. DEFINIÇÃO DAS FUNÇÕES (TASKS / JOBS)
# ==========================================

async def send_promotions():
    """Tarefa executada via cron as 9horas"""
    provider = MercadoLivreProvider()
    offers = provider.get_offers()
    pipeline = PipelineService(offers)
    await pipeline.run()

# ==========================================
# 2. CONFIGURAÇÃO DE LISTENERS (OUVINTES)
# ==========================================

def error_monitor(event):
    """
    Função listener. O APScheduler dispara eventos nativos.
    Podemos capturar falhas globais aqui (útil para mandar alertas ou salvar logs).
    """
    if event.exception:
        print(f"Ocorreu um erro crítico na tarefa {event.job_id}: {event.exception}")
    else:
        print(f"Tarefa: {event.job_id} executada com sucesso absoluto")

def initializer_system_promotions():
    jobstores = {
        'memory': MemoryJobStore(),
        'default': SQLAlchemyJobStore(url='postgresql+pg8000://postgres:admin@localhost:5432/PromoFlow')
    }

    executors = {
        #Ideal para tarefas mais leves
        'default': ThreadPoolExecutor(max_workers=10), #Limite de 10 threads simultâneas

        #Ideal para tarefas mais pesadas
        'processpool': ProcessPoolExecutor(max_workers=3)
    }

    job_defaults = {
        # se uma tarefa travar ou o sistema cair, ela acumula execuções perdidas.
        # coalesce=True diz: 'Se perdeu 5 execuções enquanto estava fora, rode apenas 1 vez quando voltar'
        'coalesce': True,

        # max_instances: Quantas instâncias da MESMA tarefa podem rodar juntas.
        # Se uma verificação de sensor demorar mais que o intervalo dela, ela não roda duplicada.
        'max_instances': 1,

        # misfire_grace_time: Se o sistema travar, dá uma tolerância de 30 segundos
        # para a tarefa atrasada tentar rodar antes de ser cancelada por completo.
        'misfire_grace_time': 60
    }

    #Instanciando o Scheduler com toda a configuração ja imposta
    scheduler = AsyncIOScheduler(
        jobstores=jobstores,
        executors=executors,
        job_defaults=job_defaults,
        timezone='America/Sao_Paulo'
    )

    #Atrelando o listener de eventos ao scheduler
    scheduler.add_listener(error_monitor, events.EVENT_JOB_EXECUTED | events.EVENT_JOB_ERROR)

    print("Iniciando o agendador de tarefas do sistema de promoções")

    schedules = [
        (9,0),
        (12,0),
        (16,30),
        (19,30),
        (21,30)
    ]

    for hour,minute in schedules:
        scheduler.add_job(
            func=send_promotions,
            trigger=CronTrigger(hour=hour, minute=minute),
            jobstore='default',
            id=f"promotion_{hour}_{minute}"
        )
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()