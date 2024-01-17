class TV:

    def __init__(self,ch,vol):
        self.channel = ch
        self.volume = vol
        self.power = True
    def on_off(self):
        if(self.power == True):
             self.power = False
             print("Turn off")
        else:
            self.power = True
            print("turn on")

    def info(self):
                print("파워:",self.power)
                print("채널:",self.channel)
                print("소리:",self.volume)
    def set_ch(self,n):
             if(self_power == True):
                set_ch =ch
             else:
                print("power off")
    def set_vol(self,n):
             if(self_power == True):
                set_vol=vol
             else:
                print("power off")

tv = TV("1","16")
tv .info()
tv.on_off()
tv.on_off()
