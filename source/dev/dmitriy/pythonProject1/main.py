"""
This is a echo bot.
It echoes any incoming text messages.
"""
from botCore import *
from sandbox.pose import get_statistics


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def echo(message):  # : types.Video

    video_file = f'{message.video.file_id}.mp4'
    original_video = os.path.join(original_video_folder, video_file)

    await message.video.download(destination_file=original_video)
    await message.reply("Thx!\nYour video was successfully uploaded!\nProcessing.😺")
    # @TODO Estimate pose
    image_size = (message.video['width'], message.video['height'])
    get_statistics(video_file, image_size, fps=30)
    await message.reply("Your video was preprocessed!\nSending back to You!\nHave a Nice Day!\nPowered by aiogram.😺")
    target_video = open(os.path.join(processed_video_folder, video_file), 'rb')
    await bot.send_video(message.chat.id, target_video)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
