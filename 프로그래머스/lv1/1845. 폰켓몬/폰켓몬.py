def solution(nums):
    select = len(nums)//2
    set_pokemon = set(nums)
    if len(set_pokemon) <= select:
        return len(set_pokemon)
    else:
        return select