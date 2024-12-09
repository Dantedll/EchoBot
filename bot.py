# bot.py

# Importar las librerías necesarias y BOT_TOKEN desde config.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from config import BOT_TOKEN

# Función para el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responde al comando /start."""
    await update.message.reply_text(
        "¡Hola soy Dantedll! Soy tu bot de Telegram. Envíame un mensaje y te responderé. 😊"
    )

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responde a los mensajes de texto enviados por el usuario."""
    user_message = update.message.text.lower()  # Convertir a minúsculas para evitar problemas con mayúsculas/minúsculas

    # Respuestas específicas
    if "hola" in user_message:
        await update.message.reply_text("¡Hola! 😊 ¿Cómo estás?")
    elif "adiós" in user_message or "adios" in user_message:
        await update.message.reply_text("¡Adiós! Que tengas un buen día. 👋")
    else:
        # Respuesta genérica para otros mensajes
        await update.message.reply_text(f"Recibí tu mensaje correctamente: '{user_message}'")

# Función principal para inicializar el bot
def main() -> None:
    """Inicializa el bot y configura los manejadores."""
    # Crear la aplicación del bot
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Configurar manejadores de comandos y mensajes
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    # Iniciar el bot
    print("El bot está funcionando. Presiona Ctrl+C para detenerlo.")
    app.run_polling()

# Ejecutar la función principal
if __name__ == "__main__":
    main()


