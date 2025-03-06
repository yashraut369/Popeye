import config
from voice_commands import VoiceCommandHandler
from automation import AutomationManager
from dark_web_monitoring import DarkWebMonitor
from freelancing import FreelancingManager
from content_creation import ContentCreator
from self_learning import SelfLearning
from osint import OSINTManager
from security import SecurityManager
from telegram_bot import TelegramBot
from twilio_calls import TwilioCalls

def main():
    print("Starting Popeye AI Assistant...")

    # Initialize components
    voice_handler = VoiceCommandHandler()
    automation_manager = AutomationManager()
    dark_web_monitor = DarkWebMonitor()
    freelancing_manager = FreelancingManager()
    content_creator = ContentCreator()
    self_learning = SelfLearning()
    osint_manager = OSINTManager()
    security_manager = SecurityManager()
    telegram_bot = TelegramBot()
    twilio_calls = TwilioCalls()

    # Main loop
    while True:
        command = voice_handler.listen() or telegram_bot.check_messages()
        if command:
            if "call" in command:
                phone_number = command.split()[-1]
                twilio_calls.make_call(phone_number)
            elif command == "exit":
                break
            elif command in automation_manager.commands:
                automation_manager.execute(command)
            elif command in dark_web_monitor.commands:
                dark_web_monitor.execute(command)
            elif command in freelancing_manager.commands:
                freelancing_manager.execute(command)
            elif command in content_creator.commands:
                content_creator.execute(command)
            elif command in self_learning.commands:
                self_learning.execute(command)
            elif command in osint_manager.commands:
                osint_manager.execute(command)
            elif command in security_manager.commands:
                security_manager.execute(command)

    print("Shutting down Popeye AI Assistant...")

if __name__ == "__main__":
    main()