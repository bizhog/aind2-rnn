import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras
import string


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = []
    y = []

    y = series[window_size:]
    i=0
    while i < len(series) - window_size:
        X.append(series[i:i+window_size])
        i+=1

    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)

    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    model = Sequential()
    model.add(LSTM(5,input_shape=(window_size,1)))
    model.add(Dense(1))
    return model


### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    punctuation = ['!', ',', '.', ':', ';', '?']
    
    norm_char = ''.join(punctuation)
    norm_char = norm_char+string.ascii_lowercase

    text = text.lower()

    for char in text:
        if not char in norm_char:
            text = text.replace(char,' ')

    return text

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []

    i,start = 0,0
    while start < len(text) - window_size:
        inputs.append(text[start: start+window_size])
        outputs.append(text[start+window_size: start+window_size+1])
        i+=1
        start = i*step_size 

    return inputs,outputs

# TODO build the required RNN model: 
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss 
def build_part2_RNN(window_size, num_chars):
    model = Sequential()
    model.add(LSTM(200,input_shape=(window_size,num_chars)))
    model.add(Dense(num_chars, activation='softmax'))

    return model
