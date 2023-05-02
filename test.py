from unittest import TestCase, main
from whiteboard import solution


class WhiteboardTestCase(TestCase):
    
    def test_1_30_sec(self):
        self.assertEqual(solution(30), "0H 0M 30S")
    
    def test_2_1_minute(self):
        self.assertEqual(solution(60), "0H 1M 0S")

    def test_3_1_and_half_minute(self):
        self.assertEqual(solution(90), "0H 1M 30S") 

    def test_4_1_hour(self):
        self.assertEqual(solution(3600), "1H 0M 0S") 
    
    def test_5_1_hour_1_min_30_sec(self):
        self.assertEqual(solution(3690), "1H 1M 30S") 

    def test_6_24_hour_1_min_30_sec(self):
        self.assertEqual(solution(86490), "24H 1M 30S")    
    
      

if __name__ == "__main__":
    main()