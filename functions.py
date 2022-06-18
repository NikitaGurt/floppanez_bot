import docx
from os.path import join



from aiogram import Bot

from config import stories_path

def get_file_content_docx(file):
    content = []
    document = docx.Document(join(stories_path, file))

    for para in document.paragraphs:
        content.append(para.text)

    return '\n'.join(content)


def get_file_content(file):
    with open(join(stories_path, file), 'r') as file:
        content = file.read()
        return content


async def send_story(bot: Bot, chat, file, title, send_count=0):
    filename, ext = file.split('.')

    file_content = 'Не указан'

    if ext == 'docx':
        file_content = get_file_content_docx(file)
    elif ext == 'txt':
        file_content = get_file_content(file)

    content_size = len(file_content)


    if content_size > 4096:
        await bot.send_message(chat, f'Новая часть истории {title}!')

        for x in range(0, content_size, 4096):
            await bot.send_message(chat, file_content[x:x + 4096])
    else:
        await bot.send_message(chat, f'<b>Новая часть истории {title}!</b>')

        await bot.send_message(chat, file_content)

    return 'hello'


