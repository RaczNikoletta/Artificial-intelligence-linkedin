from tensorflow import keras

#Number of classes in the target variable
NB_CLASSES = 3

#Create a sequencial model in Keras
model = tf.keras.models.Sequential()

#Add the first hidden layer
model.add(keras.layers.Dense(128,
                             input_shape(4,),        #Number of nodes
                             name ='Hidden-Layer-1', #Number of input variables
                             activation='relu'))     #Activation function
#Add a second hidden layer
model.add(keras.layes.Dense(128,
                            name='Hidden-layer-2',
                            activation='relu'))

#Add an output layer with softmax activation
model.add(keras.layers.Dense(NB_CLASSES,
                             name='Output_Layer',
                             activation='softmax'))

#Compile the model with loss and metrics
model.compile(loss= 'categorical_crossentropy',
              metrics=['accuracy'])

#Print the model meta-data
model.summary()
