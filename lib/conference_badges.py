def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    rooms = list(range(1,9))
    room_assignments = []

    for name in names:
       if rooms:
        room = rooms.pop(0)
        assignment = f"Hello, {name}! You'll be assigned to room {room}!"
        room_assignments.append(assignment)
       else:
        break
    return room_assignments
    
def printer(names):
    badge_messages = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
    
    for badge in badge_messages:
        print(badge)
    
    for assignment in room_assignments:
        print(assignment)