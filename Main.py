import pyautogui as pag
import json
import logging
import os
from datetime import datetime
from random import randint, choice


class ReminderApp:
    def __init__(self, config_file='config.json'):
        self.setup_logging()
        self.config = self.load_config(config_file)
        self.logger.info("ReminderApp initialized successfully")
    
    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            filename='reminder_log.txt',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger(__name__)
    
    def load_config(self, config_file):
        """Load configuration from JSON file"""
        try:
            if not os.path.exists(config_file):
                self.logger.error(f"Config file {config_file} not found")
                raise FileNotFoundError(f"Config file {config_file} not found")
            
            with open(config_file, 'r') as f:
                config = json.load(f)
            
            self.logger.info("Configuration loaded successfully")
            return config
        
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON in config file: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Error loading config: {e}")
            raise
    
    def show_reminder(self):
        """Show productivity reminder popup"""
        try:
            question = choice(self.config['questions'])
            popup_text = f'{question}\n\n{" " * 10}Are you working or wasting time?'
            
            self.logger.info(f"Showing reminder: {question}")
            
            response = pag.confirm(
                text=popup_text,
                title='Future Reminder',
                buttons=['Wasting', 'Working']
            )
            
            self.log_response(question, response)
            return response
        
        except Exception as e:
            self.logger.error(f"Error showing reminder: {e}")
            return None
    
    def show_motivational_message(self):
        """Show motivational message for wasting time"""
        try:
            message = choice(self.config['motivational_messages'])
            self.logger.info(f"Showing motivational message: {message}")
            
            pag.alert(
                text=message,
                title='Future Reminder',
                button='OK'
            )
        
        except Exception as e:
            self.logger.error(f"Error showing motivational message: {e}")
    
    def show_success_message(self):
        """Show success message for working"""
        try:
            message = self.config['success_message']
            timeout = self.config['settings']['working_timeout_seconds']
            
            self.logger.info("Showing success message")
            
            pag.alert(
                text=message,
                title='Future Reminder',
                timeout=timeout
            )
        
        except Exception as e:
            self.logger.error(f"Error showing success message: {e}")
    
    def log_response(self, question, response):
        """Log user response for tracking"""
        self.logger.info(f"User response: {response} to question: {question}")
    
    def get_random_interval(self):
        """Get random interval between reminders"""
        min_interval = self.config['settings']['min_interval_minutes']
        max_interval = self.config['settings']['max_interval_minutes']
        return randint(min_interval, max_interval)
    
    def run(self):
        """Main application loop"""
        try:
            initial_delay = self.config['settings']['initial_delay_minutes']
            self.logger.info(f"Starting reminder app with {initial_delay} minute initial delay")
            
            # Initial delay
            pag.sleep(60 * initial_delay)
            
            while True:
                response = self.show_reminder()
                
                if response == "Wasting":
                    self.show_motivational_message()
                elif response == "Working":
                    self.show_success_message()
                
                # Wait for next reminder
                interval = self.get_random_interval()
                self.logger.info(f"Next reminder in {interval} minutes")
                pag.sleep(60 * interval)
        
        except KeyboardInterrupt:
            self.logger.info("Application stopped by user")
            print("\nReminder app stopped.")
        
        except Exception as e:
            self.logger.error(f"Unexpected error in main loop: {e}")
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    try:
        app = ReminderApp()
        app.run()
    except Exception as e:
        print(f"Failed to start application: {e}")