# import mediapipe as mp
import logging
import os
from aiogram import Bot, Dispatcher, executor, filters, types

API_TOKEN = '5119282527:AAGmvaAiqGaM0pPAZ-lBGPDCZMYJ1gVJU1c'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

original_video_folder = 'original'
if not os.path.exists(original_video_folder):
    os.mkdir(original_video_folder)

processed_video_folder = 'processed'
if not os.path.exists(processed_video_folder):
    os.mkdir(processed_video_folder)
