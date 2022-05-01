from keras.models import model_from_json

def load_model():
    json_file = open("models/model.json")
    loaded_model_json = json_file.read()
    json_file.close()
    load_model = model_from_json(loaded_model_json)

    load_model.load_weights('models/model.h5')
    return load_model
    # print("loaded model from disk")

model = load_model()
