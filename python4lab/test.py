import unittest
from Bulb import Bulb
from Garland import Garland
from Lamp import Lamp
from LED import LED
from LED_lamp import LedLamp
from Solar_panel import SolarPanel
from LightShopManager import LightShopManager
from Enums.TypeOfEnergyUse import TypeOfEnergyUse

class TestLightShopManager(unittest.TestCase):

    def setUp(self):
        self.a = Bulb("bulb", "China", "Bulb", 16, 10, 100, 50)
        self.b = Bulb("ordinary bulb", "Ukraine", "Maxus", 24, 6, 80, 320)
        self.c = Lamp("modern lamp", "USA", "Philips", 1200, 30, 500, 600, "desktop", "plastic")
        self.d = LED("LED", "Japan", "Lebron", 10, 1, 10, 700, "red")
        self.e = LedLamp("modern LED lamp", "Canada", "Samsung", 1600, 50, 200, 365, "white", "day light")
        self.f = Garland("X-Mas garland", "China", "ICICLE", 250, 300, 220, 120, "green", 250)
        self.g = SolarPanel("Sun Shine", "German", "Solar Energy", 3000, 300, 350, 1500, "green", 10000, 60)

        all_objects = [self.a, self.b, self.c, self.d, self.e, self.f, self.g]
        self.light_shop_manager = LightShopManager(all_objects)

    def test_sort_by_price(self):
        self.assertEqual(self.light_shop_manager.sort_by_price(True), [self.g, self.e, self.c, self.f, self.b, self.a, self.d])

    def test_sort_by_power(self):
        self.assertEqual(self.light_shop_manager.sort_by_power(True), [self.c, self.g, self.f, self.e, self.a, self.b, self.d])

    def test_find_by_type(self):
        self.assertEqual(self.light_shop_manager.find_by_type(TypeOfEnergyUse.ORDINARY), [self.c, self.a, self.b])

if __name__ == "__main__":
     unittest.main()
