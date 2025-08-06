from redis.asyncio import Redis
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from bot.config import Config

def load_storage(config: Config) -> RedisStorage:
    return RedisStorage(
        redis=Redis(
            host=config.redis.HOST,
            port=config.redis.PORT
        ),
        key_builder=DefaultKeyBuilder(
            with_destiny=True
        )
    )