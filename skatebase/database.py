from tortoise import Tortoise

#     "postgres",
#     user="docker",
#     password="chusaiyu3Xah8eefees3ealohgh0uJeiw9oeh1oh",
#     host="db",
#     database="skate",

async def startDB():
    await Tortoise.init(
        db_url="postgres://docker:chusaiyu3Xah8eefees3ealohgh0uJeiw9oeh1oh@db:5432/skate",
        modules={"models": ["skatebase.models"]})
    print('generate tortoise schemas')
    await Tortoise.generate_schemas()
