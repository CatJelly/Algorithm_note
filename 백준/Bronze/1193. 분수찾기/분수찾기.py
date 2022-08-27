def act1(num, deno, mode):
    if mode == True: 
        return num+1, deno
    else:
        return num, deno+1

def act2(num, deno, mode):
    if mode == True: 
        return num-1, deno+1
    else:
        return num+1, deno-1

X = int(input())
num, deno = 1, 1

i = 1
act_flag = 0
up_down = False
while True:
    if i == X:
        break
    elif (deno == 1 or num == 1) and act_flag == 0:
        act_flag = 1

    if act_flag == 1:
        num, deno = act1(num, deno, up_down)
        act_flag = -1
    else:
        num, deno = act2(num, deno, up_down)
        act_flag = -1
        if deno == 1 or num == 1:
            act_flag = 0
            up_down = not up_down 

    i += 1


print(f'{num}/{deno}')