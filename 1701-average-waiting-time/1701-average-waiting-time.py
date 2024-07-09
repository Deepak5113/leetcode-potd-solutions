class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait_time=0
        next_idle_time=0
        for customer in customers:
            next_idle_time=max(customer[0],next_idle_time)+customer[1]
            wait_time+=next_idle_time-customer[1]
        avg_wait_time=wait_time/len(customers)