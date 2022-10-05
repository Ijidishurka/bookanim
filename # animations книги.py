# animations книги
# Канал - @modwini
from .. import loader
from asyncio import sleep


@loader.tds
class book(loader.Module):
    strings = {"name": "book"}

    @loader.owner
    async def bookcmd(self, message):
        for _ in range(10):
            for book in ["📙", "📘", "📗", "📓", "📕", "📔"]:
                await message.edit(book)
                await sleep(0.3)