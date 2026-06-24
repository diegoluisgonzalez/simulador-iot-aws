import streamlit as st
import boto3
import pandas as pd
import time

st.set_page_config(page_title="IoT Invernadero AWS", layout="wide")

st.title("🌱 IoT Dashboard en Tiempo Real (AWS + DynamoDB)")

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.Table("SensoresInvernadero")

placeholder = st.empty()

while True:
    try:
        response = table.scan()
        items = response.get("Items", [])

        df = pd.DataFrame(items)

        if not df.empty:
            df = df.sort_values(by="timestamp", ascending=False)

            col1, col2, col3 = st.columns(3)

            col1.metric("🌡 Temperatura", df.iloc[0]["temperatura"])
            col2.metric("💧 Humedad", df.iloc[0]["humedad"])
            col3.metric("📡 Dispositivo", df.iloc[0]["dispositivo"])

        with placeholder.container():
            st.subheader("📊 Datos en tiempo real")
            st.dataframe(df)

        time.sleep(3)

    except Exception as e:
        st.error(f"Error: {e}")
        break