import pickle
import base64

object = input("Pickled object= ")
serial_object = base64.b64decode(object)
deserial_object = pickle.loads(serial_object)
print(dir(deserial_object))