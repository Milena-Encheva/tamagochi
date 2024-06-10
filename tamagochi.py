from abc import ABC, abstractmethod

"""
Tamagochi

It has two animals - Cat and Dog.

All animals have mood, hungry level, energy level with range 1-10

By default they start with values of 5.

The used can interact with each animal in the following ways:
- put to sleep----> This action will increase energy, will make the animal hungry
- feed----> This action will decrease hungriness, increase mood and the animal will make a sound
- play----> This action will increase mood, decrease energy and the animal will make a sound
"""


class Animal(ABC):
    def __init__(self, name) -> None:
        self.name = name
        self._energy_level = 5
        self._hungry_level = 5
        self._mood = 5

    @abstractmethod
    def make_sound(self):
        pass

    def put_to_sleep(self):
        if self._energy_level < 10:
            self._energy_level += 1
        else:
            return f'{self.name} is not tired!'
        if self._hungry_level > 2:
            self._hungry_level -= 1
        else:
            return f'{self.name} is too hungry to sleep!'
        return (f'You put your {self.name} to sleep - its energy increased to {self._energy_level}'
                f' but will get up hungrier - its hungry lever decreased to {self._hungry_level}.')

    def feed(self):
        if self._hungry_level < 10:
            self._hungry_level += 1
        else:
            return f'{self.name} is not hungry!'
        if self._mood < 10:
            self._mood += 1
        else:
            return f'{self.name} is too excited!'
        sound = self.make_sound()
        return (f'You have fed you {self.name} - it less less hungry '
                f'(hungry level increased to {self._hungry_level}) and'
                f' more happy - mood increased to {self._mood} points.{sound}!')

    def play(self):
        if self._mood < 10:
            self._mood += 1
        else:
            return f'{self.name} does not want to play!'
        if self._energy_level < 2:
            return f'{self.name} is too tired'
        self._energy_level -= 1
        sound = self.make_sound()
        return (f'You have played with your {self.name} - it got a little tired energy level decreased '
                f'to {self._energy_level}) but is happy now - mood increased to {self._mood} points. {sound}!')


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return f"Meow, Meow"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return f"Woof, woof"


def main():

    cat = Cat('Maca')
    dog = Dog('Jack')
    pets = cat, dog

    for pet in pets:
        print(pet.feed())
        print(pet.play())
        print(pet.make_sound())
        print(pet.put_to_sleep())


if __name__ == "__main__":
    main()
