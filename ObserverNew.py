import random
import time
import os


class SerialReceiver:
    DATA = [0, 0, 0, 0, 0, 0, 0]

    def __init__(self):
        self._filters_list = []

    @classmethod
    def update(cls):
        cls.DATA = [random.randint(0, 10) for x in range(0, 7)]
        return cls.DATA

    def receive_new_data(self):
        print("new data appeared {}".format(SerialReceiver.DATA))
        self.notify_filters()

    def register(self, data_filter):
        self._filters_list.append(data_filter)

    def unregister(self, data_filter):
        self._filters_list.append(data_filter)

    def notify_filters(self):
        for filters in self._filters_list:
            filters.update()

    @staticmethod
    def timer(arg):
        time.sleep(arg)


class FilterScale:
    INSTANCES_AMOUNT = 0

    def __init__(self, name, data_multiplier=1):
        self._name = name
        self._data_multiplier = data_multiplier
        self._data = []

    def update(self):
        self._data = [x * self._data_multiplier for x in SerialReceiver.DATA]

    @classmethod
    def append_member(cls):
        cls.INSTANCES_AMOUNT += 1
        return cls.INSTANCES_AMOUNT

    def return_members(self):
        return self._data, self._name, self._data_multiplier

    @classmethod
    def __str__(cls):
        return "In filter {} - received data changed ! Altered data: {} Multiplier: {} Instance number {}".format\
            (cls.return_members()[1], cls.return_members()[0], cls.return_members()[2])


class Client:
    test_serial_receiver = SerialReceiver()
    test_filter_double = FilterScale("doubler", 2)
    test_filter_quad = FilterScale("Quadruped", 4)
    test_serial_receiver.register(test_filter_quad)
    test_serial_receiver.register(test_filter_double)
    # test_serial_receiver.register(fython_pile.DataSaver(SerialReceiver.DATA))

    test_serial_receiver.receive_new_data()
    test_serial_receiver.update()
    test_serial_receiver.receive_new_data()


Client()
