from chalice import Chalice

app = Chalice(app_name='scheduled')

# como e um disparo agendado usa a app.schedule
# timeout maximo de 15 min
@app.schedule("cron(0 7 ? * * *)")
def scheduled(event):
    print("Executou a funcao com sucesso!")
    return True

