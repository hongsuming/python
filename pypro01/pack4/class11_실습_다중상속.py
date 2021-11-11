# 다중 상속 : 가전 제품의 소리 조절 기능 (메소드)의 이름을 동일하게 주고 다형성 처리
from astropy.units import TV
from bokeh.core.json_encoder import rd
class ElecProduct:
    volume = 0
    
    def volumControl(self, volume):
        pass
    
class ElectTv(ElecProduct):
    def volumControl(self, volume): # 오버라이딩
        self.volume += volume
        print('TV 소리 크기 : ', self.volume)
        
class ElectRadio(ElecProduct):
    def volumControl(self, volume): # 오버라이딩
        vol = volume
        self.volume += vol
        print('Radio 소리 크기 : ', self.volume)
        
    def showProduct(self):
        print('Radio 고유 메소드')
        
tv = ElectTv()
tv.volumControl(5)
tv.volumControl(-2)

rd = ElectRadio()
rd.volumControl(10)
rd.volumControl(-2)
rd.showProduct()

p = tv
p.volumControl(3)
p = rd
p.volumControl(8)