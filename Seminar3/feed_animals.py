from typing import List

def max_fed_animals(animals: List[int], food: List[int]) -> int:
    animals_sorted = sorted(animals)
    food_sorted = sorted(food)
    
    animal_ptr = 0
    food_ptr = 0
    count = 0
    
    while animal_ptr < len(animals_sorted) and food_ptr < len(food_sorted):
        if food_sorted[food_ptr] >= animals_sorted[animal_ptr]:
            count += 1
            animal_ptr += 1
            food_ptr += 1
        else:
            food_ptr += 1
    
    return count