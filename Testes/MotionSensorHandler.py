import json
import boto3

def lambda_handler(event, context):
    # Lógica da função Lambda quando acionada
    print("Movimento detectado!")

    # Configurar cliente SNS
    sns_client = boto3.client('sns')

    # Detalhes da mensagem SNS
    topic_arn = 'arn:aws:sns:us-east-1:123456789012:MotionSensorAlarm'  # Substitua pelo ARN do seu tópico SNS
    message = 'Movimento detectado na porta da sala!'
    subject = 'Alerta de Movimento'

    # Publicar mensagem no tópico SNS
    response = sns_client.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject=subject
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Função Lambda acionada com sucesso e alarme SNS enviado!')
    }
