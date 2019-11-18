import abc

SAMPLE_CONSTANT = ["a", "b", "c"]

_private_constant = []


def _private_method():
    return "Json is good!"


def sample_global_method():
    return "YaMl! YAMl! yaml!"


class SampleClass(object):
    def inner(self, a=[]):
        pass


class SecondSampleClass(SampleClass):
    pass
