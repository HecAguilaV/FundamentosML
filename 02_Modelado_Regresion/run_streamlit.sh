#!/bin/bash

# Nos movemos a la carpeta del script
cd "$(dirname "$0")" || exit

echo "========================================="
echo "Iniciando App de Regresión eSports"
echo "========================================="

# 1. Detectar entorno virtual (prioriza el global de la raíz, fallback a local)
if [ -d "../.venv" ]; then
    VENV_PATH="../.venv"
elif [ -d "venv" ]; then
    VENV_PATH="venv"
else
    VENV_PATH="venv"
    echo "Creando entorno virtual local ($VENV_PATH)..."
    python3 -m venv "$VENV_PATH"
fi

# 2. Activar entorno virtual
echo "Activando entorno virtual desde $VENV_PATH..."
source "$VENV_PATH/bin/activate"

# 3. Validar e instalar dependencias si es necesario
if ! python3 -c "import streamlit" &> /dev/null; then
    echo "Instalando dependencias necesarias..."
    pip install --upgrade pip -q
    pip install streamlit pandas scikit-learn joblib matplotlib seaborn -q
fi

# 4. Levantar la aplicación
echo "Levantando Streamlit..."
echo "========================================="
streamlit run app.py
