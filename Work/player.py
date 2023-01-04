# DO NOT MODIFY AN CLASS ATTRIBUTE , Always modify through a method
from pathlib import Path
class Player:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.health = 100

    def move(self ,dx, dy):
        self.x += dx
        self.y += dy

    def damage(self, pts):
        self.health -= pts

class Car:
    def __init__(self, name):
        self.name = name
        self.color = "RED"
        self.state = "OFF"

    def start(self):
        self.state = "ON"

    def stop(self):
        self.state = "OFF"

    def is_on(self):
        if self.state == "ON":
            return True
        else:
            return False


class File_Path:
    def __init__(self, f_path):
        self.f_path = f_path

    def relative_path(self):
        '''build/reports/checkDependencyConstraint/allCheckDependencyConstraint.json
        returns - True / False'''
        return Path(self.f_path).is_absolute()

    def abs_path(self):
        '''/Users/nvelmuru/tony-projects/icosmigrateapi
         returns - True / False'''
        return Path(self.f_path).is_relative_to()

    def base_name(self):
        '''build/reports/checkDependencyConstraint/allCheckDependencyConstraint.json
         Return allCheckDependencyConstraint.json'''

    def append(self, subpath):
        ''' f= File_path("/home/tom/downloads")
        f.base_name - should return downloads
        f.append("story.txt")
        f.base_name should return story.txt'''



class Foo:
    def bar(self, a):
        print(self)

    @classmethod
    def spam(cls):
        print(cls)
