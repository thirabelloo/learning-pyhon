from datetime import datetime, timedelta

class DatasBr:
    def __init__(self) -> None:
        self.momento_cadastro = datetime.today()
    
    def __str__(self) -> str:
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]
    
    def dia_semana(self):
        dias_da_semana = [
            "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira",
            "Sexta-feira", "Sabado", "Domingo"  
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dias_da_semana[dia_semana]
    
    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada
    
    def tempo_cadastro(self):
        return (datetime.today() + timedelta(days=30) )- self.momento_cadastro