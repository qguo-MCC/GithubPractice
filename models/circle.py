from dataclasses import dataclass
from typing import Union
from typing import ClassVar

@dataclass #use python dataclass to simplify class construction
class CircleGeometry: #class name should be Pascal Cases: cap the first letter of each word
    '''
    Automatically compute geometric properties of a circle.
    :param radius: the radius of a circle
    '''
    radius: Union[int, float]
    PI: ClassVar[float] = 3.14159265359  # constant should be all cap.
    def __post_init__(self):
        self.area = self.PI*(self.radius)**2
        self.circumference = 2*self.PI*self.radius
        self.diameter = 2*self.radius

    def __repr__(self) -> str:
        return f'CircleGeometry(radius={self.radius}, area={self.area}, circumference={self.circumference}, diameter={self.diameter})'
