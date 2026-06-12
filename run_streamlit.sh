#!/bin/bash

# Nos movemos a la carpeta correcta sin importar desde dónde se llame el script
cd "$(dirname "$0")/02_Modelado_Regresion" || exit

VENV_DIR="venv"

echo "========================================="
echo "🎮 Iniciando Entorno para eSports App"
echo "========================================="

# 1. Comprobamos si el entorno virtual ya existe; si no, lo creamos.
if [ ! -d "$VENV_DIR" ]; then
    echo "📦 Creando entorno virtual ($VENV_DIR)..."
    python3 -m venv $VENV_DIR
else
    echo "✅ Entorno virtual detectado."
fi

# 2. Activamos el entorno virtual
echo "🚀 Activando entorno..."
source $VENV_DIR/bin/activate

# 3. Instalamos dependencias si es la primera vez
# Comprobamos si streamlit ya está instalado en el venv para no reinstalar a cada rato
if ! python3 -c "import streamlit" &> /dev/null; then
    echo "⚙️  Instalando dependencias necesarias... (esto puede tardar un minuto la primera vez)"
    pip install --upgrade pip -q
    pip install streamlit pandas scikit-learn joblib -q
    echo "✅ Dependencias instaladas."
fi

# 4. Levantamos la app
echo "🌐 Levantando Streamlit..."
echo "========================================="
streamlit run app.py
