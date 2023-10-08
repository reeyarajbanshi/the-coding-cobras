from hub import light_matrix
import motor_pair
import motor
import runloop
from hub import port

left_motor = port.A
right_motor = port.C
forklift = port.F
dozer = port.E

async def forklift_up():
    motor.run_for_degrees(port.F,250,280)

async def forklift_down():
    motor.run_for_degrees(port.F,-200,280)


async def mission_1():
    # Pair motors on port A and C
    motor_pair.pair(motor_pair.PAIR_1,port.A, port.C)
    # moving forklift down
    # await motor.run_for_degrees(forklift,-100, 280)
    # Move straight at a specific velocity for 1 second; moves forward
    await motor_pair.move_for_time(motor_pair.PAIR_1,1000,0,velocity=280)
    # Run at 1000 velocity for 0.5 seconds; moving left
    await motor.run_for_time(right_motor, 300,300)
    # moves straight at angle
    await motor_pair.move_for_time(motor_pair.PAIR_1,750, 0, velocity=280)
    # turning right
    await motor.run_for_time(left_motor,300,-400)
    # move backwards
    await motor_pair.move_for_time(motor_pair.PAIR_1,1750,0,velocity=-280)

async def mission_2():
    # # pairing motor A and C to motor pair
    # motor_pair.pair(motor_pair.PAIR_1,port.A,port.C)
    # # moving robot forward to reach theater scene change
    # await motor_pair.move_for_time(motor_pair.PAIR_1,3000,0,velocity=280)
    # # moving forklift up 100 degrees
    # await motor.run_for_degrees(forklift,50,280)
    # # turning left 200 miliseconds
    # await motor.run_for_time(right_motor, 200,500)
    # # moving forward
    # await motor_pair.move_for_time(motor_pair.PAIR_1,500,0,velocity=280)
    for i in range(3):
        # moving forlift down 200 degrees
        await motor.run_for_degrees(forklift,-300,300)
        # sleep one second
        runloop.sleep_ms(1)
        # move forklift up
        await motor.run_for_degrees(forklift,280,300)
    # await motor.run_for_degrees(forklift,-250,280)
        

async def mission_3():
    # pairing motor A and C to motor pair
    motor_pair.pair(motor_pair.PAIR_1,port.A,port.C)
    # moving forward toward tallest mission
    await motor_pair.move_for_time(motor_pair.PAIR_1,3000,0,velocity=280)
    # turning left towards mission 3
    await motor.run_for_degrees(right_motor,150,280)
    # moving forward toward mission 3
    await motor_pair.move_for_time(motor_pair.PAIR_1,1525,0,velocity=280)
    # moving forklift down to complete mission
    await motor.run_for_degrees(forklift,-300,300)

async def mission_4():
    # pairing motor A and C to motor pair
    motor_pair.pair(motor_pair.PAIR_1,port.A,port.C)

runloop.run(mission_3())
