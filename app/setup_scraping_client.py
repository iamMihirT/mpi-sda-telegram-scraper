from logging import Logger
from telethon import TelegramClient


def get_scraping_client(
    job_id: int,
    logger: Logger,
    telegram_api_id: str,
    telegram_api_hash: str,
    telegram_phone_number: str | None = None,
    telegram_password: str | None = None,
    telegram_bot_token: str | None = None,
) -> TelegramClient:
    try:

        logger.info(f"{job_id}: Setting up Telegram client.")

        if not all([telegram_api_id, telegram_api_hash]):
            logger.error(
                f"{job_id}: TELEGRAM_API_ID and TELEGRAM_API_HASH must be set."
            )
            raise ValueError("TELEGRAM_API_ID and TELEGRAM_API_HASH must be set.")

        client = TelegramClient(
            "sda-telegram-scraper", telegram_api_id, telegram_api_hash
        )

        if telegram_phone_number and telegram_password:
            logger.info(f"{job_id}: Starting Telegram client with phone number")
            client.start(
                phone=telegram_phone_number,
                password=telegram_password,
            )

        elif telegram_bot_token:
            logger.info(f"{job_id}: Starting Telegram client with bot token")
            client.start(
                bot_token=telegram_bot_token,
            )

        else:
            raise ValueError(
                "Either TELEGRAM_PHONE and TELEGRAM_PASSWORD, or TELEGRAM_BOT_TOKEN must be set."
            )

        logger.info(f"{job_id}: Telegram client started successfully")

        return client

    except Exception as error:
        logger.error(f"{job_id}: Unable to setup the Telegram client. Error:\n{error}")
        raise error
