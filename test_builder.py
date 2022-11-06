import unittest
from Account import *
from State import *

class TestBuilder(unittest.TestCase):
    def test_if_state_is_online(self):
        
        #ARRANGE
        expectedValue = Online()

        #ACT
        actualValue = UserAccount()
        actualValue.alert()

        #ASSERT
        self.assertEqual(actualValue.currentState, expectedValue)

    def test_if_state_is_offline(self):
        
        #ARRANGE
        expectedValue = Offline()

        #ACT
        actualValue = UserAccount()
        actualValue.setState(Offline())

        #ASSERT
        self.assertEqual(actualValue.currentState, expectedValue)

    def test_if_state_is_busy(self):
        
        #ARRANGE
        expectedValue = Busy()

        #ACT
        actualValue = UserAccount()
        actualValue.setState(Busy())

        #ASSERT
        self.assertEqual(actualValue.currentState, expectedValue)

    def test_if_state_is_dnd(self):
        
        #ARRANGE
        expectedValue = DnD()

        #ACT
        actualValue = UserAccount()
        actualValue.setState(DnD())

        #ASSERT
        self.assertEqual(actualValue.currentState, expectedValue)

    def test_if_state_is_away(self):
        
        #ARRANGE
        expectedValue = Away()

        #ACT
        actualValue = UserAccount()
        actualValue.setState(Away())

        #ASSERT
        self.assertEqual(actualValue.currentState, expectedValue)

    def test_if_state_is_meeting(self):
        
        #ARRANGE
        expectedValue = Meeting()

        #ACT
        actualValue = UserAccount()
        actualValue.setState(Meeting())

        #ASSERT
        self.assertEqual(actualValue.currentState, expectedValue)
    
if __name__ == '__main__':
    unittest.main()