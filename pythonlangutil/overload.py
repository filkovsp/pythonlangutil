
def signature(*types):
    def func(f):
        def inner_func(callingObj, *args, **kwargs):
            return f(callingObj, *args, **kwargs)
        inner_func.signature = types
        return inner_func
    return func

class Overload(object):
    def __init__(self, func):
        self.owner = None
        self.signatures = []
        self.methods = []
        self.methods.append(func)
        self.signatures.append(func.signature)

    def __get__(self, owner, ownerType=None):
        self.owner = owner or self
        return self

    def __call__(self, *args, **kwargs):
        signature = []
        for arg in args:
            signature.append(arg.__class__)
        for k, v in kwargs.items():
            signature.append(v.__class__)

        signature = tuple(signature)

        # 1) filer self.signatures by count of elements
        # 2) find the match for `signature` in there
        signatures = filter(lambda s: len(s) == len(signature), self.signatures)
        for sig in signatures:
            if all(map(lambda s: issubclass(s, sig[signature.index(s)]), signature)):
                index = self.signatures.index(sig)
                return self.methods[index](self.owner, *args, **kwargs)
                # TODO:
                # in theory, with using issubclass() method
                # there might be the case when we can get more than one match.
                # might take place in multi-level subclassing.
                # in this case the best match needs to be found.

        raise Exception(f"There is no overload for method with signature: {signature}")

    def overload(self, func):
        self.methods.append(func)
        self.signatures.append(func.signature)
        return self
