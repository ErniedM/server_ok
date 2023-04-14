from crontab import CronTab

def schedule_check_toevoegen(user, service, interval):
    '''Toevoegen van een cronjob'''
    my_cron=CronTab(user=user)
    job=my_cron.new(command=f"python /home/s127280/Python/Labo6/server_ok/code/{service}", comment=f"{service}")
    job.minute.every(interval)
    my_cron.write()

def scheduled_check_verwijderen(user, service):
    '''Verwijderen van een cronjob'''
    my_cron=CronTab(user=user)
    my_cron.remove_all(comment=f"{service}")
    my_cron.write()