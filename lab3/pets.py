class Animal:
    _slots__ = ('__name', '__age','_sex')
    
    def __init__(self, age, sex):
        self.age = age
        self.sex = sex
        self.name =''
        
    def __repr__(self):
        return f'{self.__class__.__name__}: age = {self.age}, sex = {self.sex}'

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError('Animals age uncorrect. Please write correct number')
            
    @property
    def sex(self):
        return self.__sex
    
    @sex.setter
    def sex(self, value):
        match value:
            case 'male' | 'female':
                self.__sex = value
            case _:
                raise ValueError('Ass')
            
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError('name must be str')
            

class Pet(Animal):
    def __init__(self, name, age, sex):
        super().__init__(age, sex)
        self.name = name
        self.is_hungry = bool(random.getrandbits(1)) #глянут че ето такое ЛОЛ
    
    def __repr__(self):
        return f'{self.__class__.__name__}: name = {self.name}, age = {self.age}, sex = {self.sex}'

    def __eq__(self, other):
        try:    # class type & name are unique identifiers
            # print(f'{type(self)} is {type(other)} [{type(self) is type(other)}] and {self.name} == {other.name} [{self.name == other.name}]')
            return type(self) is type(other) and self.name == other.name 
        except Exception:
            return False

    def is_hungry(self):
        return self.is_hungry
        
    def feed(self):
        self.is_hungry = False
    
    def is_voice(self):
        return self.is_voice
        
    def voice_down(self):
        self.is_voice = False

    def action(self):
        print('This pet is abstract therefore it can not act!')

class Cat(Pet):
    def action(self):
        print(f'The cat named {self.name} meows.')

class Dog(Pet):
    def action(self):
        print(f'The dog named {self.name} barks.')

class Parrot(Pet):
    def action(self):
        print(f'The parrot named {self.name}. imitation voice')

# implements a dynamic array as a container, this was overcomplicated
class OwnedPets(object):
    def __init__(self):
        self.size = 0       # actual elements stored
        self.capacity = 1   # current capacity
        self.pets = self.__alloc(self.capacity) # array of pets
        self.__idx = 0                          # hidden index for iteration

    def __repr__(self):
        fstr = str()
        for pet in self:
            fstr += f'\t{pet}\n'

        return f'[\n{fstr}]'
         
    def __len__(self):
        return self.size
     
    def __getitem__(self, index):
        # check out of bounds
        if not 0 <= index < self.size:
            return IndexError(f'{self.__class__.__name__}: index out of bounds')
         
        return self.pets[index] # get element

    def __iter__(self):
        self.__idx = 0  # reset index
        return self     # return self

    def __next__(self):
        # check bounds
        if self.__idx >= self.size:
            raise StopIteration
        # return current iteration pet
        pet = self[self.__idx]
        self.__idx += 1
        return pet

    def __contains__(self, item):
        # this should be better
        for pet in self:
            if pet == item : return True

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f'operands {self} and {other} type mismatch')
        # constuct a new set
        ret = OwnedPets()
        # add all pets we had
        for pet in self:
            ret.push(pet)
        # add all pets we do not already have
        for pet in other:
            ret.push(pet)
        return ret

    def __sub__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f'operands {self} and {other} type mismatch')
        # constuct a new set
        ret = OwnedPets()
        # add all pets we had
        for pet in self:
            ret.push(pet)
        # remove pets listed in other from self
        for pet in other:
            ret.remove(pet)
        return ret
         
    def __resize(self, new_cap):
        new_arr = self.__alloc(new_cap) # new bigger array
         
        for i in range(self.size): # copy all existing objects
            new_arr[i] = self.pets[i]
             
        self.pets = new_arr     # set new array
        self.capacity = new_cap # set new capacity
         
    def __alloc(self, new_cap):
        return (new_cap * ctypes.py_object)()

    def push(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError(f'{pet} is not of type Pet')
        # check if we already have this pet
        if pet in self:
            return self
        # check capacity, double if not enough
        if self.size == self.capacity:
            self.__resize(2 * self.capacity)
         
        # set self.size index to a new pet object
        self.pets[self.size] = pet
        self.size += 1
        return self
 
    def pop(self):
        if self.size == 0:
            return
         
        self.pets[self.size - 1] = None
        self.size -= 1

    def remove(self, pet_to_remove):
        if self.size == 0:
            return False

        # find index of the pet, enumerate is cool, but no
        index = 0
        for pet in self:
            if pet == pet_to_remove:
                break
            index += 1
        # not found
        if index >= self.size:
            return False

        # check if last
        if index == self.size - 1:
            self.pets[index] = None
            self.size -= 1
            return True
        # copy upper part of the array 
        for i in range(index, self.size - 1):
            self.pets[i] = self.pets[i + 1]
        # remove
        self.pets[self.size - 1] = None
        self.size -= 1
        return True

class Person(Animal):
    def __init__(self, name, age, sex):
        super().__init__(age, sex)
        self.name = name
    
    def __repr__(self):
        return f'{self.__class__.__name__}: name = {self.name}, age = {self.age}, sex = {self.sex}'

class Owner(Person):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)
        self.pets = OwnedPets()

    def __repr__(self):
        return f'{self.__class__.__name__}: name = {self.name}, age = {self.age}, sex = {self.sex}'

    # adds one pet to the OwnedPets dynamic container
    def add_pet(self, pet):
        self.pets.push(pet)

    # adds many pets to the OwnedPets dynamic container
    def add_pets(self, pet_list):
        for pet in pet_list:
            self.pets.push(pet)

    # checks is pets are hungry
    def are_pets_hungry(self):
        for pet in self.pets:
            if pet.is_hungry:
                print(f'{pet.name} is hungry, {self.name}!')
    
    # feeds all pets
    def feed_pets(self):
        for pet in self.pets:
            pet.feed()
    
    def are_pets_speak(self):
        for pet in self.pets:
            if pet.is_voice:
                print(f'{pet.name} speak something, {self.name}')
    
    def cant_speak(self):
        for pet in self.pets:
            pet.voice_down()


def main(args):
    man = Owner('Valeriy', 54, 'male')
    woman = Owner('Natasha', 42, 'female')
    
    # add pets individualy
    man.add_pet(Cat('Felix', 2, 'male'))   
    man.add_pet(Cat('Vasya', 14, 'male'))
    man.add_pet(Dog('July', 1, 'female'))
    man.add_pet(Parrot('Vasuliy', 5, 'female'))
    print(man)
    
    # add a list of pets
    woman.add_pets([Cat('Sweetie', 3, 'female'), Dog('Terry', 3, 'male'), Cat('Felix', 2, 'male')])
    print(woman)

    # check different pets Valeriy Albertovich has
    print('\nChecking is Valeriy Albertovich has specific pets...')
    ret = Cat('Polosatik', 1, 'male') in man.pets
    print(f'Valeriy Albertovich has a cat named Polosatik?\t{ret}')
    ret = Parrot('Vaas', 5, 'female') in man.pets
    print(f'Valeriy Albertovichhas a parrot named Vaas?\t{ret}')
    ret = Dog('Felix', 2, 'male') in man.pets
    print(f'Valeriy Albertovich has a dog named Felix?\t{ret}')

    # check if Natasha's pets are hungry and feed then feed them
    print('\nChecking if Natasha\'s pets are hungry...')
    woman.are_pets_hungry()
    print('\nFeeding them if they are...')
    woman.feed_pets()
    print('\nChecking again...')
    woman.are_pets_hungry()
    print('\n Checkinh if pets say something ...')
    woman.are_pets_speak()
    print('\n Not saying :(')
    woman.cant_speak()


    # pets do something
    print('\nValeriy Albertovich\'s pets doing something...')
    for pet in man.pets:
        pet.action()

    ret = man.pets.remove(Parrot('Vaas', 5, 'female'))
    print(f'\nRemoving a parrot named Vasuliy from Valeriy Albertovich...\t{ret}')
    ret = man.pets.remove(Dog('July', 1, 'female'))
    print(f'Removing a dog named July from Valeriy Albertovich...\t{ret}\n')
    print(man)
    print(woman)

    print(f'\nValeriy Albertovich \'s + Natasha\'s pets = {man.pets + woman.pets}')
    print(f'\nValeriy Albertovich\'s - Natasha\'s pets = {man.pets - woman.pets}')

    return 0

if __name__ == '__main__':
    import sys
    import random
    import ctypes
    sys.exit(main(sys.argv))
