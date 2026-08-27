class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_infos = []
        for i in range(len(position)):
            car_infos.append((position[i], speed[i], (target-position[i])/speed[i]))
        
        car_infos = sorted(car_infos, key=lambda x: x[0], reverse=True)
        stack = []
        for car_info in car_infos:
            if not stack:
                stack.append(car_info[2])
                continue
            if car_info[2] <= stack[-1]:
                continue
            else:
                stack.append(car_info[2])

        return len(stack)