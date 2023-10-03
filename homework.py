from dataclasses import dataclass

M_IN_KM = 1000
LEN_STEP = (0.65, 1.38)


class InfoMessage:
    """Информационное сообщение о тренировке."""
    @dataclass
    def __init__(self) -> None:
        training_type : str
        duration : float
        distance : float
        speed : float
        calories : str

    def get_message(self):
        return f'Тип тренировки: {self.training_type}; Длительность: {self.duration:.2f} ч.; Дистанция: {self.distance:.2f} км; Ср. скорость: {self.speed:.2f} км/ч; Потрачено ккал: {self.calories:.2f}.'
        

class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        pass

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
         return self.action * LEN_STEP / M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage
        pass


class Running(Training):
    """Тренировка: бег."""
    def __init__(self, action: int, duration: float, weight: float, LEN_STEP = 0.65) -> None:
        super().__init__(action, duration, weight)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self, action: int, duration: float, weight: float, LEN_STEP = 0.65) -> None:
        super().__init__(action, duration, weight)


class Swimming(Training):
    """Тренировка: плавание."""
    def __init__(self, action: int, duration: float, weight: float, LEN_STEP = 1.38) -> None:
        super().__init__(action, duration, weight)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

