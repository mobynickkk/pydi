from enum import Enum


class ComponentModeEnum(Enum):
    """
    Enum for component building mode. Components are created in singleton mode, while bricks not
    """
    COMPONENT = 1
    BRICK = 2
