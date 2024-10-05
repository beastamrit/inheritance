class vechile:
    def __init__(self,name,max_speed):
        self.name=name
        self.max_speed=max_speed
class bus(vechile):
    pass
schoolbus=bus("lamborgini",max_speed=150)
print(schoolbus.name,schoolbus.max_speed)
