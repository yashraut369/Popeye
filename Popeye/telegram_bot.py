import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

class TelegramBot:
    def __init__(self):
        self.commands = ["start", "stop", "status"]
        self.updater = Updater(token=os.getenv("TELEGRAM_BOT_TOKEN"), use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")

        start_handler = CommandHandler('start', self.start)
        stop_handler = CommandHandler('stop', self.stop)
        status_handler = CommandHandler('status', self.status)
        message_handler = MessageHandler(Filters.text & (~Filters.command), self.handle_message)

        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(stop_handler)
        self.dispatcher.add_handler(status_handler)
        self.dispatcher.add_handler(message_handler)

        self.updater.start_polling()

    def start(self, update, context):
        context.bot.send_message(chat_id=self.chat_id, text="Popeye AI Assistant started.")

    def stop(self, update, context):
        context.bot.send_message(chat_id=self.chat_id, text="Popeye AI Assistant stopped.")
        self.updater.stop()

    def status(self, update, context):
        context.bot.send_message(chat_id=self.chat_id, text="Popeye AI Assistant is running.")

    def handle_message(self, update, context):
        command = update.message.text
        context.bot.send_message(chat_id=self.chat_id, text=f"Executing command: {command}")
        return command

    def check_messages(self):
        updates = self.updater.bot.get_updates()
        for update in updates:
            if update.message:
                return update.message.text
        return None