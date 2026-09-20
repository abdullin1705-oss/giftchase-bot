import random
from typing import List

def generate_mines(grid_size: int = 25, mines_count: int = 3) -> List[int]:
    return random.sample(range(grid_size), mines_count)

def play_mines(bet: int, mines_count: int, revealed: List[int], cashout: bool = False) -> dict:
    if mines_count < 1 or mines_count > 20:
        return {"success": False, "error": "Неверное количество мин"}
    
    grid_size = 25
    mines = generate_mines(grid_size, mines_count)
    
    for pos in revealed:
        if pos in mines:
            return {
                "success": True,
                "win":
