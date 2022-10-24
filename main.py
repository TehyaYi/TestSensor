# comment by Peter: //4real-boolean/ILOVEYOU,#gang
# Tehya Yi 10/23/2022
import config
import pymongo
import datetime

client = pymongo.MongoClient(f"mongodb+srv://raspi:{config.password}"
                             f"@cluster0.tev7xup.mongodb.net/?retryWrites=true&w=majority",
                             server_api=pymongo.server_api.ServerApi('1'))
db = client.test

def main():
    """Send some sensor data to a mongo db."""
    print(db.list_collection_names())
    # TODO: make new collection if collection for curr not made
    first_collection = db.test_collection
    num = 5  # random number for testing

    machine = {
        "id": str(num),
        "date": str(datetime.datetime.utcnow()),
        "data1": "test 1",
        "data2": "test 2",
        "data3": "test 3",
    }

    result = first_collection.insert_one(machine)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
