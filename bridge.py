import paho.mqtt.client as mqtt
import boto3
import json

# Configurações do MQTT
MQTT_BROKER = '172.20.10.3'
MQTT_PORT = 1883
MQTT_TOPIC = 'sensor-de-presenca'

# Configurações da AWS SNS
AWS_REGION = 'us-east-2'
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-2:851725618481:MotionSensor'

# Inicializar o cliente SNS
sns_client = boto3.client('sns', region_name=AWS_REGION)

# Função chamada quando a conexão MQTT é estabelecida
def on_connect(client, userdata, flags, rc):
    print(f"Conectado com o código de resultado {rc}")
    client.subscribe(MQTT_TOPIC)

# Função chamada quando uma mensagem é recebida no tópico subscrito
def on_message(client, userdata, msg):
    print(f"Mensagem recebida no tópico {msg.topic}: {msg.payload.decode()}")
    enviar_email_sns(msg.payload.decode())

# Função para enviar um email via SNS
def enviar_email_sns(mensagem):
    response = sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=mensagem,
        Subject='Nova Mensagem MQTT'
    )
    print(f"Email enviado. ID da mensagem: {response['MessageId']}")

# Inicializar o cliente MQTT
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Conectar ao broker MQTT
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Manter a conexão ativa e processar mensagens
mqtt_client.loop_forever()
