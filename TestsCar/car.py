class Car:
    def __init__(self, brand: str, model: str, miles_limit=0):
        self.__brand = brand
        self.__model = model
        self.__miles_limit = miles_limit
        self.__is_engine_started = False

    @property
    def miles_limit(self):
        return self.__miles_limit

    def start_engine(self):
        if not self.__is_engine_started:
            self.__is_engine_started = True
            return "Engine started."
        else:
            return "Engine is already running."

    def stop_engine(self):
        if self.__is_engine_started:
            self.__is_engine_started = False
            return "Engine stopped."
        else:
            return "Engine is already off."

    def drive(self, miles_to_drive: int):
        if self.__is_engine_started:
            if self.__miles_limit >= miles_to_drive:
                self.__miles_limit -= miles_to_drive
                return f"Driving {miles_to_drive} miles."
            else:
                return f"The miles limit has been exceeded"
        else:
            return "Cannot drive. Engine is off."
