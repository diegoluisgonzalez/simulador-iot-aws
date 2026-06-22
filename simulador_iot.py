from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
import json
import random
import os

# 1. PEGA AQUÍ TU ENDPOINT (el que copiaste de 'Settings' en AWS IoT)
ENDPOINT = "axzmbfedjc2w3-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "basicPubSub"

# 2. RUTAS A TUS ARCHIVOS (Están en tu carpeta 'certificados')
PATH_TO_CERT = "certificados/Invernadero_01.cert.pem"
PATH_TO_KEY = "certificados/Invernadero_01.private.key"
PATH_TO_ROOT = "certificados/AmazonRootCA1.pem"



print(os.path.exists(PATH_TO_ROOT))
print(os.path.exists(PATH_TO_KEY))
print(os.path.exists(PATH_TO_CERT))

# 3. Inicialización del cliente
mqttClient = AWSIoTMQTTClient(CLIENT_ID)
mqttClient.configureEndpoint(ENDPOINT, 8883)
mqttClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)

# Conectar al Broker
print("Conectando a AWS IoT Core...")
mqttClient.connect()
print("¡Conectado! Enviando datos...")

# 4. Bucle principal
try:
    while True:
        payload = {
            "dispositivo": "Invernadero_01",
            "temperatura": round(random.uniform(20.0, 30.0), 2),
            "humedad": round(random.uniform(40.0, 80.0), 2)
        }

        # Publicar al tópico que AWS está esperando
        mqttClient.publish("sdk/test/python", json.dumps(payload), 1)
        print(f"Enviado: {payload}")

        time.sleep(5)
except KeyboardInterrupt:
    print("Simulación detenida.")
    mqttClient.disconnect()