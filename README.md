# Future Reminder

A Python productivity application that helps you stay focused by periodically asking if you're working or wasting time.

## Features

- **Periodic Reminders**: Shows popup dialogs every 15-30 minutes asking about your productivity
- **Motivational Messages**: Displays encouraging or challenging messages based on your response
- **Random Questions**: Uses a variety of thought-provoking questions to keep you self-aware
- **Automatic Timing**: Runs continuously with random intervals to avoid predictability
- **Configuration File**: Easy editing of questions, messages, and settings via JSON
- **Error Handling**: Robust error handling for popup failures and file issues
- **Usage Logging**: Tracks responses and usage patterns in log file
- **Class-Based Structure**: Clean, organized code using ReminderApp class

## How It Works

1. **Initial Delay**: Waits 5 minutes before starting
2. **Productivity Check**: Shows a dialog asking "Are you working or wasting time?" with motivational questions
3. **Response Handling**:
   - **"Wasting"**: Shows a motivational alert to get back on track
   - **"Working"**: Shows encouragement and continues monitoring
4. **Random Intervals**: Waits 15-30 minutes before the next reminder

## Requirements

```
pyautogui
```

## Files Structure

- `Main.py` - Main application with ReminderApp class
- `config.json` - Configuration file with questions, messages, and settings
- `reminder_log.txt` - Log file tracking usage patterns (auto-generated)

## Installation

1. Clone or download this repository
2. Install the required dependency:
   ```bash
   pip install pyautogui
   ```

## Usage

Run the application:
```bash
python Main.py
```

The program will:
- Wait 5 minutes before the first reminder
- Show periodic popups asking about your productivity
- Log all interactions to `reminder_log.txt`
- Continue running until manually stopped (Ctrl+C)

## Customization

Edit `config.json` to customize:
- Questions and motivational messages
- Timing intervals (initial delay, min/max reminder intervals)
- Success message and timeout settings

## Sample Questions

The app includes thought-provoking questions like:
- "Are you using your potential or wasting your time?"
- "Is this helping you grow or just distracting you?"
- "Are you making progress or just passing the time?"

## Sample Motivational Messages

- "Time is money, don't waste it."
- "You're better than this."
- "Your future self is watching."

## Note

This application uses system-level popup dialogs that will appear on top of other applications. Make sure you're comfortable with periodic interruptions before running.