import asyncio
import logging
import keyboard as k

running = True
spam_task = None

# Config
message_text = "123"
msg_time = 0.8
wait_time = 5
logging.basicConfig(level=logging.INFO)


async def spam():
    logging.debug("Spam task started")
    while True:
        for _ in range(9):
            k.write(message_text, 0.02)
            k.send("enter")
            await asyncio.sleep(msg_time)
        await asyncio.sleep(wait_time)


def toggle_spam(loop):
    global spam_task
    if spam_task:
        spam_task.cancel()
        spam_task = None
    else:
        spam_task = loop.create_task(spam())
    logging.info(f"Spamming:  {spam_task is not None}")


def cancel():
    global running
    running = False
    logging.info("Exiting...")


async def main():
    while running:
        await asyncio.sleep(0.1)


if __name__ == "__main__":
    print("Welcome to the Discord Spam Script.\nPress <F3> to toggle spamming, and <F4> to exit.")
    event_loop = asyncio.get_event_loop()
    k.add_hotkey("F3", toggle_spam, args=(event_loop,))
    k.add_hotkey("F4", cancel)
    event_loop.run_until_complete(main())
