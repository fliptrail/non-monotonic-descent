import tensorflow as tf
import tensorflow_addons as tfa

class mlp:
    def __init__(self, input_shape:int) -> None:
        input = tf.keras.layers.Input(shape=(input_shape, ), dtype=tf.float32)
        node = tf.keras.layers.Dense(units=1, activation=tfa.activations.snake)(input)

        self.model = tf.keras.Model(inputs=input, outputs=node, name='mlp')
