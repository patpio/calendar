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
