from loader import db
from utils.db_api import db_gino




async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    print("Подключаем базу данных")
    await db_gino.on_startup(dp)
    #print("Чистим")
    #print("Чистим")
    #await db.gino.drop_all()
   
    print("Создаем")
    await db.gino.create_all()


    await on_startup_notify(dp)



if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
