'use strict'

const mqtt = require('../..')
//const client = mqtt.connect()
const client = mqtt.connect({ port: 1883, host: '192.168.1.100', keepalive: 10000});

client.subscribe('presence')
client.publish('presence', 'bin hier')
client.on('message', function (topic, message) {
  console.log(message)
  invokeLambda();
})
client.end()


const AWS = require('aws-sdk');
AWS.config.update({ region: 'us-east-2' });

const lambda = new AWS.Lambda();

function invokeLambda() {
    const params = {
        FunctionName: 'MotionSensorHandler', // Nome da função Lambda criada
        InvocationType: 'Event', // 'Event' para invocação assíncrona, 'RequestResponse' para síncrona
        Payload: JSON.stringify({ key: 'value' }) // Dados que você quer passar para a função Lambda
    };

    lambda.invoke(params, function(err, data) {
        if (err) {
            console.error(err);
        } else {
            console.log('Função Lambda invocada com sucesso:', data);
        }
    });
}

// Chame essa função quando o sensor de movimento detectar movimento
invokeLambda();
