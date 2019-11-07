import abc

SAMPLE_CONSTANT = ["a", "b", "c"]

_private_constant = []


def _private_method():
    pass


def sample_global_method():
    pass


class SampleClass(object):
    def inner(self):
        pass


class SecondSampleClass(SampleClass):
    pass
