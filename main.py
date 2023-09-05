def padel_court_cost(court_type):
    if court_type=='indoor':
        return 30
    elif court_type=='outdoor':
        return 20
def rackets_cost(racket_brand):
    if racket_brand=='bullpadel':
        return 100
    elif racket_brand=='nox':
        return 140
    elif racket_brand=='siux':
        return 200
def padel_balls_cost(ball_boxes):
    if ball_boxes=='box':
        return 2
    elif ball_boxes=='two_boxes':
        return 3.5
    elif ball_boxes=='three_boxes':
        return 5
def padel_game_cost():
    court_type=input('court_type''indoor''outdoor')
    racket_brand=input('racket_brand''bullpadel''nox''siux')
    ball_boxes=input('ball_boxes''box''two_boxes''three_boxes')
    total_cost = padel_court_cost(court_type) + rackets_cost(racket_brand) + padel_balls_cost(ball_boxes)
    return total_cost
print(padel_game_cost())