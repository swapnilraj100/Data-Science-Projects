import unittest
from allocator import allocate_discounts

class TestAllocator(unittest.TestCase):

    def test_normal_case(self):
        data = {
            "siteKitty": 10000,
            "salesAgents": [
                {"id": "A1", "performanceScore": 90, "seniorityMonths": 18, "targetAchievedPercent": 85, "activeClients": 12},
                {"id": "A2", "performanceScore": 70, "seniorityMonths": 6, "targetAchievedPercent": 60, "activeClients": 8}
            ]
        }
        result = allocate_discounts(data["siteKitty"], data["salesAgents"])
        self.assertEqual(sum(agent["assignedDiscount"] for agent in result["allocations"]), 10000)

    def test_all_same(self):
        data = {
            "siteKitty": 10000,
            "salesAgents": [
                {"id": "A1", "performanceScore": 80, "seniorityMonths": 12, "targetAchievedPercent": 70, "activeClients": 10},
                {"id": "A2", "performanceScore": 80, "seniorityMonths": 12, "targetAchievedPercent": 70, "activeClients": 10}
            ]
        }
        result = allocate_discounts(data["siteKitty"], data["salesAgents"])
        discounts = [agent["assignedDiscount"] for agent in result["allocations"]]
        self.assertEqual(discounts[0], discounts[1])

    def test_rounding_case(self):
        data = {
            "siteKitty": 3,
            "salesAgents": [
                {"id": "A1", "performanceScore": 100, "seniorityMonths": 10, "targetAchievedPercent": 100, "activeClients": 10},
                {"id": "A2", "performanceScore": 0, "seniorityMonths": 0, "targetAchievedPercent": 0, "activeClients": 0}
            ]
        }
        result = allocate_discounts(data["siteKitty"], data["salesAgents"])
        total = sum(agent["assignedDiscount"] for agent in result["allocations"])
        self.assertEqual(total, 3)

if __name__ == '__main__':
    unittest.main()
