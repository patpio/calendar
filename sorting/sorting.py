class Sort:
    @staticmethod
    def sort(fn):

        def inner(obj):

            return sorted(fn(obj), key=lambda x: [getattr(x, condition) for condition in obj.sort_config])
        return inner
