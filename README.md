# simulador-iot-aws
Proyecto de simulación de un sistema de invernadero inteligente utilizando Python y AWS IoT Core. El dispositivo simulado envía datos en tiempo real de temperatura y humedad a la nube mediante conexión MQTT segura con certificados X.509.

:::writing{"variant":"document","id":"48291"}
🌱 Simulador IoT con AWS IoT Core (Python + MQTT)
📌 Descripción del proyecto

Este proyecto simula un dispositivo IoT de invernadero que envía datos en tiempo real a AWS IoT Core utilizando el protocolo MQTT sobre TLS.
El sistema genera métricas de temperatura y humedad y las publica de forma continua hacia la nube para su procesamiento.

El objetivo es demostrar una arquitectura básica de IoT en la nube con AWS, simulando un caso real de monitoreo agrícola inteligente.

🏗️ Arquitectura del sistema (nivel cloud)
Dispositivo IoT (Python)
        ↓ MQTT (TLS)
AWS IoT Core
        ↓ Rules Engine
Servicios AWS opcionales:
   ├── AWS Lambda (procesamiento)
   ├── Amazon DynamoDB (almacenamiento)
   ├── Amazon CloudWatch (monitoreo)
   └── Amazon S3 (data histórica)
⚙️ Tecnologías utilizadas
Python 3
AWS IoT Core
MQTT Protocol
AWSIoTPythonSDK
TLS X.509 Certificates
Random (simulación de sensores)
📡 Funcionamiento

El script:

Simula un dispositivo IoT llamado Invernadero_01
Genera datos aleatorios de:
🌡️ Temperatura (20°C - 30°C)
💧 Humedad (40% - 80%)
Se conecta de forma segura a AWS IoT Core usando certificados X.509
Publica mensajes MQTT cada 5 segundos al topic:
sdk/test/python
🔐 Seguridad

La conexión se realiza mediante:

Certificado del dispositivo (.cert.pem)
Clave privada (.private.key)
Amazon Root CA
Comunicación TLS (puerto 8883)

⚠️ Las credenciales NO deben subirse a GitHub (protegidas con .gitignore).

🚀 Ejecución del proyecto
pip install AWSIoTPythonSDK
python simulador_iot.py
📊 Ejemplo de payload
{
  "dispositivo": "Invernadero_01",
  "temperatura": 24.58,
  "humedad": 62.31
}
🎯 Casos de uso
Monitoreo de invernaderos inteligentes
Sistemas de agricultura IoT
Simulación de dispositivos conectados a AWS
Pruebas de arquitectura cloud IoT
💡 Mejoras futuras
Integración con AWS Lambda
Almacenamiento en DynamoDB
Dashboard en tiempo real (AWS QuickSight o Grafana)
Alertas con Amazon SNS
Uso de sensores reales (ESP32 / Raspberry Pi)
👨‍💻 Autor

Diego Luis González
Proyecto personal – IoT + AWS Cloud Engineering

📌 Nota

Este proyecto es una simulación educativa de arquitectura IoT en AWS, enfocado en aprendizaje de servicios cloud, MQTT y comunicación segura con dispositivos.
