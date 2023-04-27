import os
from dotenv import load_dotenv
from pathlib import Path
from email.message import EmailMessage
import smtplib

# loading env vars
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# mailing port and server



