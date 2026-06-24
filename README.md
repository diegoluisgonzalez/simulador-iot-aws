# 🌱 IoT Smart Greenhouse System (AWS + Streamlit + MQTT)

## 📌 Descripción del Proyecto

Este proyecto implementa un sistema de **IoT simulado en tiempo real** para monitoreo de un invernadero inteligente, utilizando servicios de AWS y una arquitectura orientada a eventos.

Los dispositivos IoT envían datos de sensores (temperatura y humedad) a la nube, donde son procesados, almacenados y visualizados en un dashboard en tiempo real.

---

## 🏗️ Arquitectura del Sistema

El flujo de datos del sistema es el siguiente:

```
Dispositivo IoT (Simulador Python)
        ↓ MQTT
AWS IoT Core
        ↓ IoT Rule
AWS Lambda
        ↓
Amazon DynamoDB
        ↓
EC2 (Streamlit Dashboard)
        ↓
Visualización en tiempo real
```

---

## ⚙️ Tecnologías Utilizadas

* 🟡 AWS IoT Core (mensajería MQTT)
* ⚡ AWS Lambda (procesamiento serverless)
* 🗄 Amazon DynamoDB (base de datos NoSQL)
* 🖥 Amazon EC2 (hosting del dashboard)
* 📊 Streamlit (visualización de datos)
* 🐍 Python 3
* 🔐 AWS IAM Roles y Policies

---

## 📡 Funcionamiento del Sistema

1. El simulador IoT genera datos de sensores (temperatura y humedad).
2. Los datos se publican en AWS IoT Core mediante MQTT.
3. Una regla de IoT activa una función Lambda.
4. Lambda procesa y guarda los datos en DynamoDB.
5. El dashboard en EC2 consulta DynamoDB en tiempo real.
6. Streamlit muestra métricas y tabla actualizada cada pocos segundos.

---

## 📊 Dashboard

El dashboard muestra:

* 🌡 Temperatura en tiempo real
* 💧 Humedad del ambiente
* 📡 ID del dispositivo
* 📊 Tabla de datos históricos recientes

---

## 🚀 Cómo ejecutar el proyecto

### 1. Clonar repositorio

```bash
git clone https://github.com/usuario/simulador-iot-aws.git
cd simulador-iot-aws
```

---

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 3. Ejecutar simulador IoT

```bash
python simulador_iot.py
```

---

### 4. Ejecutar dashboard

```bash
streamlit run dashboard_realtime.py --server.port 8501 --server.address 0.0.0.0
```

---

## ☁️ Arquitectura en la nube

Este proyecto demuestra habilidades en:

* Arquitecturas serverless en AWS
* Integración IoT con MQTT
* Procesamiento de eventos en tiempo real
* Bases de datos NoSQL escalables
* Despliegue de aplicaciones en EC2

---

## 🔐 Seguridad

* Uso de IAM Roles para acceso a DynamoDB
* Comunicación segura mediante MQTT con AWS IoT Core
* Separación de responsabilidades entre servicios

---

## 📈 Posibles mejoras

* Alertas en tiempo real con Amazon SNS
* Visualización avanzada con Grafana
* Autenticación en dashboard
* Escalamiento con AWS Greengrass

---

## 👨‍💻 Autor
Autor: Diego González - Electronic Engineer | IoT & Cloud Developer

Proyecto desarrollado como parte de formación en:

* IoT
* Cloud Computing (AWS)
* Desarrollo backend en Python

---

## ⭐ Resultado

Este sistema demuestra una arquitectura IoT completa en la nube, desde la generación de datos hasta la visualización en tiempo real, simulando un caso real de industria agrícola inteligente.

