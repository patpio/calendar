class Filter:
    @staticmethod
    def filter(fn):

        def inner(obj):
            # key = [*obj.filter_config][0]
            # val = obj.filter_config[key]
            # return filter(lambda x: getattr(x, key) == val, fn(obj))
            keys = [*obj.filter_config]
            filtered_events = fn(obj)
            for key in keys:
                filtered_events = list(filter(lambda x: getattr(x, key) == obj.filter_config[key], filtered_events))
            return filtered_events

        return inner

