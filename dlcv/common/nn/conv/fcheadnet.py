from keras.layers.core import Dropout, Flatten, Dense

class FCHeadNet():
    @staticmethod
    def build(baseModel, classes, D):
        # Initialize the head model that will be placed on top of
        # the base, then add a FC layer
        headModel = baseModel.output
        headModel = Flatten(name="flatten")(headModel)
        headModel = Dense(D, activation="relu")(headModel)
        headModel = Dropout(0.5)(headModel)
        
        # Add a softmax layer
        headModel = Dense(classes, activation="softmax")(headModel)
        
        return headModel