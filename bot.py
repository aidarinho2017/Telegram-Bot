import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define states for the conversation
START, COPY_MESSAGE = range(2)

# Dictionary to store user messages
user_messages = {}

# Start command handler
def start(update, context):
    update.message.reply_text("Hello! I'm your message copier bot. Send me a message, and I'll copy it.")

    return COPY_MESSAGE

# Message handler to copy and echo user messages
def copy_message(update, context):
    user_id = update.message.from_user.id
    message_text = update.message.text
    user_messages[user_id] = message_text

    update.message.reply_text("Message copied: " + message_text)

# Main function to run the bot
def main():
    # Initialize the Updater
    updater = Updater(token='*****************************')

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Define a conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            COPY_MESSAGE: [MessageHandler(Filters.text & ~Filters.command, copy_message)]
        },
        fallbacks=[]
    )

    dp.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
