class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        max_water_bottles=numBottles
        while numBottles>=numExchange:
            full_bottles_after_exchange=numBottles//numExchange
            max_water_bottles+=full_bottles_after_exchange
            remaining_empty_bottles=numBottles-(full_bottles_after_exchange*numExchange)
            numBottles=full_bottles_after_exchange+remaining_empty_bottles     
        return max_water_bottles