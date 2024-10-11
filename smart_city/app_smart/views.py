from django.shortcuts import render
from django.http import HttpResponse
import os
import csv
import django
from app_smart.models import Sensor, Tipos_sensor, TemperaturaData, UmidadeData, ContadorData, LuminosidadeData
from datetime import datetime
from dateutil import parser
from .form import CSVUploadForm
import pytz

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_city.settings')
django.setup()



# Create your views here.

# def load_temperature_data(csv_file_path):
#     print("Início da importação:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#     with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
#         reader = csv.DictReader(csvfile)
#         line_count = 0
#         for row in reader:
#             sensor_id = int(row['sensor_id'])
#             valor = float(row['valor'])
#             timestamp = parser.parse(row['timestamp']) 
#             sensor = Sensor.objects.get(id=sensor_id)
#             TemperaturaData.objects.create(sensor=sensor, valor=valor, 
#             timestamp=timestamp)
#             line_count += 1
#             if line_count % 10000 == 0:
#                 print(f"{line_count} linhas processadas...")
#             print("Fim da importação:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#             print(f"Dados carregados com sucesso de {csv_file_path}")
# # Chame a função para carregar os dados do arquivo CSV
# load_temperature_data('dados/temperatura_data.csv')

# def load_temperature_data(request):
#     if request.method == 'POST':
#         form_temperatura = CSVUploadForm(request.POST, request.FILES)
        
#         if form_temperatura.is_valid():
#             csv_file = request.FILES['file']
            
#             if not csv_file.name.endswith('.csv'):
#                 form_temperatura.add_error('file', 'Este não é um arquivo CSV válido.')
#             else:
                
#                 file_data = csv_file.read().decode('ISO-8859-1').splitlines()
#                 reader = csv.DictReader(file_data, delimiter=',')  # Altere para ',' se necessário
                
#                 for row in reader:
                    
                    
                    
                    
#                     try:
#                         sensor = Sensor.objects.get(id=int(row['sensor_id']))
#                         TemperaturaData.objects.create(
#                             sensor=sensor, 
#                             valor=float(row['valor']), 
#                             timestamp=parser.parse(row['timestamp'])
#                         )
#                     except KeyError as e:
#                         print(f"Chave não encontrada: {e} na linha: {row}")  # Exibe o erro e a linha problemática
                

#     else:
#         form_temperatura = CSVUploadForm()

#     return render(request, 'sensores.html', {'form_temperatura': form_temperatura})


def upload_csv_view(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        
        form_temperatura = CSVUploadForm(request.POST, request.FILES)
        
        
        form_umidade = CSVUploadForm(request.POST, request.FILES)
        
        if form_temperatura.is_valid():
            csv_file = request.FILES['file']
            
            if not csv_file.name.endswith('.csv'):
                form_temperatura.add_error('file', 'Este não é um arquivo CSV válido.')
            else:
                
                file_data = csv_file.read().decode('ISO-8859-1').splitlines()
                reader = csv.DictReader(file_data, delimiter=',')  # Altere para ',' se necessário
                
                for row in reader:
                    
                    
                    
                    
                    try:
                        sensor = Sensor.objects.get(id=int(row['sensor_id']))
                        TemperaturaData.objects.create(
                            sensor=sensor, 
                            valor=float(row['valor']), 
                            timestamp=parser.parse(row['timestamp'])
                        )
                    except KeyError as e:
                        print(f"Chave não encontrada: {e} na linha: {row}")
                        
                        
        else:
            form_temperatura = CSVUploadForm()
        
        if form.is_valid():
            csv_file = request.FILES['file']
            
            if not csv_file.name.endswith('.csv'):
                form.add_error('file', 'Este não é um arquivo CSV válido.')
            else:
                
                file_data = csv_file.read().decode('ISO-8859-1').splitlines()
                reader = csv.DictReader(file_data, delimiter=',')  # Altere para ',' se necessário
                
                for row in reader:
                    
                    
                    
                    try:
                        id_tipo = Tipos_sensor.objects.filter(tipo=row['tipo']).first()
                    except Tipos_sensor.DoesNotExist:
                        Tipos_sensor.objects.create(tipo=row['tipo'])
                        id_tipo = Tipos_sensor.objects.filter(tipo=row['tipo']).first()
                    
                    try:
                        Sensor.objects.create(
                            tipo=id_tipo,
                            unidade_medida=row['unidade_medida'] if row['unidade_medida'] else None,
                            latitude=float(row['latitude'].replace(',', '.')),
                            longitude=float(row['longitude'].replace(',', '.')),
                            localizacao=row['localizacao'],
                            responsavel=row['responsavel'] if row['responsavel'] else '',
                            status_operacional=True if row['status_operacional'] == 'True' else False,
                            observacao=row['observacao'] if row['observacao'] else '',
                            mac_address=row['mac_address'] if row['mac_address'] else None
                        )
                    except KeyError as e:
                        print(f"Chave não encontrada: {e} na linha: {row}")  # Exibe o erro e a linha problemática
                

        else:
            form = CSVUploadForm()
            
        
        if form_umidade.is_valid():
            csv_file = request.FILES['file']
            
            if not csv_file.name.endswith('.csv'):
                form_umidade.add_error('file', 'Este não é um arquivo CSV válido.')
            else:
                
                file_data = csv_file.read().decode('ISO-8859-1').splitlines()
                reader = csv.DictReader(file_data, delimiter=',')  # Altere para ',' se necessário
                
                for row in reader:
                    
                    
                    
                    try:
                        id_tipo = Tipos_sensor.objects.filter(tipo=row['tipo']).first()
                    except Tipos_sensor.DoesNotExist:
                        Tipos_sensor.objects.create(tipo=row['tipo'])
                        id_tipo = Tipos_sensor.objects.filter(tipo=row['tipo']).first()
                    
                    try:
                        UmidadeData.objects.create(
                            sensor=Sensor.objects.get(id=int(row['sensor_id'])), 
                            valor=float(row['valor']), 
                            timestamp=parser.parse(row['timestamp']).astimezone(pytz.timezone('America/Sao_Paulo'))

                        )

                    except KeyError as e:
                        print(f"Chave não encontrada: {e} na linha: {row}")  # Exibe o erro e a linha problemática
                

        else:
            form_umidade = CSVUploadForm()
           

    return render(request, 'sensores.html', {'form': form, 'form_temperatura': form_temperatura, 'form_umidade': form_umidade})

