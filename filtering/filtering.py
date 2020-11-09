class Filter:
    @staticmethod
    def filter(fn):
        def inner(obj):
            filtered_tasks = []

            conditions = obj.filter_config.keys()

            for event in fn(obj):
                counter = 0

                for condition in conditions:
                    min_val = obj.filter_config[condition]['min']
                    max_val = obj.filter_config[condition]['max']

                    value = getattr(event, condition)

                    min_val = value if min_val is None else min_val
                    max_val = value if max_val is None else max_val

                    if min_val <= value <= max_val:
                        counter += 1
                if counter == len(conditions):
                    filtered_tasks.append(event)

            return filtered_tasks

        return inner


# class Filter:
#     @staticmethod
#     def filter(fn):
#         def inner(obj):
#             def custom_filter(event):
#                 min_val = obj.filter_config['duration']['min']
#                 max_val = obj.filter_config['duration']['max']
#
#                 value = getattr(event, list(obj.filter_config.keys())[0])
#
#                 min_val = value if min_val is None else min_val
#                 max_val = value if max_val is None else max_val
#
#                 return min_val <= value <= max_val
#
#             result = filter(custom_filter, fn(obj))
#             return result
#
#         return inner

# key = [*obj.filter_config][0]
# val = obj.filter_config[key]
# return filter(lambda x: getattr(x, key) == val, fn(obj))
# keys = [*obj.filter_config]
# filtered_events = fn(obj)
# for key in keys:
#     filtered_events = list(filter(lambda x: getattr(x, key) == obj.filter_config[key], filtered_events))
# return filtered_events
