import os
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from tqdm import tqdm


class ModelTrainer:
    def __init__(self, data_path):
        self.data_path = data_path
        self.model = None
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.seq_length = 10
    
    def load_data(self):
        data = pd.read_csv(self.data_path)
        return data
    
    def preprocess_data(self, data):
        scaled_data = self.scaler.fit_transform(data['Adj Close'].values.reshape(-1, 1))
        return scaled_data
    
    def create_sequences(self, data):
        X, Y = [], []
        for i in range(len(data) - self.seq_length):
            X.append(data[i:(i + self.seq_length), 0])
            Y.append(data[i + self.seq_length, 0])
        return np.array(X), np.array(Y)
    
    def build_model(self):
        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.LSTM(units=50, return_sequences=True, input_shape=(self.seq_length, 1)))
        model.add(tf.keras.layers.LSTM(units=50))
        model.add(tf.keras.layers.Dense(units=1))
        model.compile(optimizer='adam', loss='mean_squared_error')
        self.model = model
        return "Model built successfully!"
    
    def train_model(self, X_train, y_train, X_test, y_test, model_name, epochs=30, batch_size=32):
        checkpoint = tf.keras.callbacks.ModelCheckpoint(model_name, monitor='val_loss', save_best_only=True, mode='min', verbose=1)
        history = self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, 
                                  validation_data=(X_test, y_test), callbacks=[checkpoint])
        pd.DataFrame(history.history).plot(figsize=(10, 7))
        return "Model trained successfully!"
    
    def save_model(self, model_path):
        self.model.save(model_path)
        return "Model saved successfully!"

if __name__ == "__main__":
    for file in tqdm(os.listdir(os.path.join(os.getcwd(), "lstm", "data"))):
        data_path = os.path.join(os.path.join(os.getcwd(), "lstm", "data"), file)
        model_trainer = ModelTrainer(data_path)
        data = model_trainer.load_data()
        scaled_data = model_trainer.preprocess_data(data)
        X, Y = model_trainer.create_sequences(scaled_data)
        X = X.reshape(X.shape[0], X.shape[1], 1)
        split = int(0.8 * len(X))
        X_train, y_train, X_test, y_test = X[:split], Y[:split], X[split:], Y[split:]
        model_trainer.build_model()
        model_trainer.train_model(X_train, y_train, X_test, y_test, model_name=f'{file.split(".")[0]}.h5')
        model_trainer.save_model(f'{file.split(".")[0]}.h5')