from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    current_weight = 0
    bridge_queue = deque([0] * bridge_length)

    truck_index = 0

    while truck_index < len(truck_weights) or current_weight > 0:
        answer += 1

        current_weight -= bridge_queue.popleft()

        if truck_index < len(truck_weights):
            if current_weight + truck_weights[truck_index] <= weight:
                bridge_queue.append(truck_weights[truck_index])
                current_weight += truck_weights[truck_index]
                truck_index += 1
            else:
                bridge_queue.append(0)

    return answer