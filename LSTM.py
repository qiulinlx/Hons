#BiDirectional Multi-Class LSTM

import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.optimizers import SGD

#Label data
GOdf= pd.read_csv('GOfreq.csv')
labels_categorical= GOdf.values.tolist()

#Sequence data
Seqdf= pd.read_csv('Sequence.csv')
sequences= Seqdf.values.tolist()

#Tokenize the sequence
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sequences)
sequences_int = tokenizer.texts_to_sequences(sequences)

# Pad the sequences to a maximum length
max_length = 34,350
sequences_padded = pad_sequences(sequences_int, maxlen=max_length, padding='post', truncating='post')

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(sequences_padded, labels_categorical, test_size=0.2, random_state=42)


from keras.models import Sequential
from keras.layers import Bidirectional, LSTM, Dense

# Define the number of units in the LSTM layer
lstm_units = 64
num_classes= len(GOdf.columns)
input_dim=1

# Build the bidirectional LSTM model
model = Sequential()
model.add(Bidirectional(LSTM(64), input_shape=(max_length,)))
model.add(Dense(len(tokenizer.word_index) + 1, activation='softmax'))

# Modify the last layer for multi-class classification
num_classes = len(tokenizer.word_index) + 1
model.add(Dense(num_classes, activation='softmax'))

# Compile the model

opt = SGD(lr=0.01, momentum=0)
model.compile(loss='sparse_categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

# Train the model
for epoch in range(100):
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=1, batch_size=32)

yhat = model.predict(X_test, verbose=0)

