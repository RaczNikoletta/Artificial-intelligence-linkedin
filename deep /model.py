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


#Make it verbose so we can see the progress
VERBOSE = 1

#Setup Hyper Parameters for training

#Set Batch size
BATCH_SIZE=16
#Set number of epochs
EPOCHS=10
#Set validation split. 20% of the training data will be used for validation
#after each epoch
VALIDATION_SPLIT=0.2

print("\nTraining Progress:\n--------------------------")

#Fit the model. This will perform the entire training cycle, including
#forward propagation, loss computation, backward propagation and gradient descent.
#execute for the specified batch sizes and epoch
#Perform validation after each epoch


    
