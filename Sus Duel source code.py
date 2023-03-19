import time
import random
from PIL import Image
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import keyboard


def health_bars(hp, e):
    index = (1, 2)
    sizes = (hp, e)
    labels = ['Your HP', 'Enemy HP']

    figure, axis = plt.subplots(figsize=(16, 10), facecolor='black')
    axis.set_facecolor('black')
    axis.spines['bottom'].set_color('darkred')
    axis.spines['top'].set_color('darkred')
    axis.spines['right'].set_color('darkred')
    axis.spines['left'].set_color('darkred')
    axis.tick_params(axis='x', colors='darkred')
    axis.tick_params(axis='y', colors='darkred')
    ax.set_ylim([0, 25])
    plt.yticks([0, 5, 10, 15, 20, 25])

    plt.bar(index,
            sizes,
            tick_label=labels,
            color='darkslateblue',
            edgecolor='darkred',
            linestyle='--',
            alpha=0.7,
            width=0.1)
    plt.get_current_fig_manager().window.wm_geometry('+0+0')


def power_calculation(a):
    global A
    if a == 1:
        A = 1
    elif a == 2 or a == 24:
        A = 2
    elif a == 0:
        A = 2
    elif a == 3 or a == 5 or a == 23:
        A = 3
    elif a == 4 or a == 6 or a == 22:
        A = 4
    elif a == 7 or a == 21:
        A = 5
    elif a == 8 or a == 20:
        A = 6
    elif a == 9 or a == 13 or a == 19:
        A = 7
    elif a == 10 or a == 12 or a == 14 or a == 18:
        A = 8
    elif a == 11 or a == 15 or a == 17:
        A = 9
    else:
        A = 10


def update(i):
    im1.seek(i)
    image = ax.imshow(im1.convert('RGB'))
    return [image]


def update_qte(i):
    im.seek(i)
    image = ax.imshow(im.convert('RGB'))
    global frame_num
    frame_num = i
    if keyboard.is_pressed(' '):
        ani.pause()
        time.sleep(3)
        plt.close()
    return [image]


HP = 25
E = 25
A = 0
frame_num = 0

# intro animation
path1 = "C:/Users/User/Desktop/GIF/cover.gif"
im1 = Image.open(path1)

fig, ax = plt.subplots(figsize=(8, 10), facecolor='black')
plt.axis('off')
plt.get_current_fig_manager().window.wm_geometry('+485+0')

ani1 = animation.FuncAnimation(fig, update, frames=im1.n_frames, interval=50, blit=True, repeat=False)

plt.show(block=False)
plt.pause(10)
plt.close()

while HP > 0:

    # idle animation
    health_bars(HP, E)

    time.sleep(1)
    path2 = "C:/Users/User/Desktop/GIF/main.gif"
    im1 = Image.open(path2)

    fig, ax = plt.subplots(figsize=(8, 10), facecolor='black')
    plt.get_current_fig_manager().window.wm_geometry('+485+0')

    ani1 = animation.FuncAnimation(fig, update, frames=im1.n_frames, interval=500, blit=True, repeat=False)

    plt.show(block=False)
    plt.axis('off')
    plt.pause(7)
    plt.close()
    plt.close()

    print('your turn, press [SPACE] to define attack power')

    # attack power QTE
    path3 = "C:/Users/User/Desktop/GIF/QTEpower.gif"
    im = Image.open(path3)

    fig, ax = plt.subplots(figsize=(8, 10), facecolor='black')
    plt.get_current_fig_manager().window.wm_geometry('+485+0')

    ani = animation.FuncAnimation(fig, update_qte, frames=im.n_frames, interval=50, blit=True)

    plt.axis('off')
    plt.show()

    # attack power calculation
    power_calculation(frame_num)

    print(' ')
    print(f'attack power: {A}')

    # attack animation
    path4 = "C:/Users/User/Desktop/GIF/attack.gif"
    im1 = Image.open(path4)

    fig, ax = plt.subplots(figsize=(8, 10), facecolor='black')
    plt.get_current_fig_manager().window.wm_geometry('+485+0')

    ani1 = animation.FuncAnimation(fig, update, frames=im1.n_frames, interval=50, blit=True, repeat=False)

    plt.show(block=False)
    plt.axis('off')
    plt.pause(2)
    plt.close()

    # value of 'x' defines enemy action
    x = random.randint(1, 3)

    if x == 1:

        print('enemy blocks!')

        # enemy block animation
        path5 = "C:/Users/User/Desktop/GIF/enemyblock.gif"
        im1 = Image.open(path5)

        fig, ax = plt.subplots(figsize=(8, 10), facecolor='black')
        plt.get_current_fig_manager().window.wm_geometry('+485+0')

        ani1 = animation.FuncAnimation(fig, update, frames=im1.n_frames, interval=50, blit=True, repeat=False)

        plt.show(block=False)
        plt.axis('off')
        plt.pause(3)
        plt.close()

        E = E - A*0.2

        print(f'damage: {A*0.2}')
        print(f'enemy HP: {E}')

    elif x == 2:

        # value of 'chance' defines whether the enymy is going to dodge/parry succesfully or not
        chance = random.randint(1, 10)

        if chance > 6:

            print("enemy dodge failed!")

            # enemy fail animation
            path6 = "C:/Users/User/Desktop/GIF/enemyfail.gif"
            im1 = Image.open(path6)

            fig, ax = plt.subplots(figsize=(8, 10), facecolor='black')
            plt.get_current_fig_manager().window.wm_geometry('+485+0')

            ani1 = animation.FuncAnimation(fig, update, frames=im1.n_frames, interval=50, blit=True, repeat=False)

            plt.show(block=False)
            plt.axis('off')
            plt.pause(3)
            plt.close()

            E = E - A

            print(f'damage: {A}')
            print(f'enemy HP: {E}')

        else:

            # enemy dodge animation
            print('enemy dodges!')

            path7 = "C:/Users/User/Desktop/GIF/enemydodge.gif"
            im1 = Image.open(path7)

            fig, ax = plt.subplots(figsize=(8, 10), facecolor='black')
            plt.get_current_fig_manager().window.wm_geometry('+485+0')

            ani1 = animation.FuncAnimation(fig, update, frames=im1.n_frames, interval=50, blit=True, repeat=False)

            plt.show(block=False)
            plt.axis('off')
            plt.pause(3)
            plt.close()

            print('damage: 0')
            print(f'enemy HP: {E}')

    else:

        chance = random.randint(1, 2)

        if chance == 1:

            # enemy parry animation
            print('enemy parries!')

            path8 = "C:/Users/User/Desktop/GIF/enemyparry.gif"
            im1 = Image.open(path8)

            fig, ax = plt.subplots(figsize=(8, 10), facecolor='black')
            plt.get_current_fig_manager().window.wm_geometry('+485+0')

            ani1 = animation.FuncAnimation(fig, update, frames=im1.n_frames, interval=50, blit=True, repeat=False)

            plt.show(block=False)
            plt.axis('off')
            plt.pause(3)
            plt.close()

            HP = HP - A

            print(f'damage: {A}')
            print(f'your HP: {HP}')

        else:

            # enemy fail animation
            print('enemy parry failed')

            path9 = "C:/Users/User/Desktop/GIF/enemyfail.gif"
            im1 = Image.open(path9)

            fig, ax = plt.subplots(figsize=(8, 10), facecolor='black')
            plt.get_current_fig_manager().window.wm_geometry('+485+0')

            ani1 = animation.FuncAnimation(fig, update, frames=im1.n_frames, interval=50, blit=True, repeat=False)

            plt.axis('off')
            plt.show(block=False)
            plt.pause(3)
            plt.close()

            E = E - A

            print(f'damage: {A}')
            print(f'enemy HP: {E}')

    if HP <= 0 or E <= 0:
        break

    print(' ')
    print('end of turn')
    print(f'your HP: {HP}')
    print(f'enemy HP: {E}')
    print(' ')
    print('enemy turn')

    # idle animation
    health_bars(HP, E)

    time.sleep(1)

    path10 = "C:/Users/User/Desktop/GIF/main.gif"
    im1 = Image.open(path10)

    fig, ax = plt.subplots(figsize=(8, 10), facecolor='black')
    plt.get_current_fig_manager().window.wm_geometry('+485+0')

    ani1 = animation.FuncAnimation(fig, update, frames=im1.n_frames, interval=500, blit=True, repeat=False)

    plt.show(block=False)
    plt.axis('off')
    plt.pause(7)
    plt.close()
    plt.close()

    # enemy attack animation
    path11 = "C:/Users/User/Desktop/GIF/enemyattack.gif"
    im1 = Image.open(path11)

    fig, ax = plt.subplots(figsize=(8, 10), facecolor='black')
    plt.get_current_fig_manager().window.wm_geometry('+485+0')

    ani1 = animation.FuncAnimation(fig, update, frames=im1.n_frames, interval=50, blit=True, repeat=False)

    plt.show(block=False)
    plt.axis('off')
    plt.pause(2)
    plt.close()

    # action choice QTE
    path12 = "C:/Users/User/Desktop/GIF/action.gif"
    im = Image.open(path12)

    fig, ax = plt.subplots(figsize=(8, 10), facecolor='black')
    plt.get_current_fig_manager().window.wm_geometry('+485+0')

    ani = animation.FuncAnimation(fig, update_qte, frames=im.n_frames, interval=70, blit=True)

    plt.axis('off')
    plt.show()

    # value of 'EA' defines enemy attack power
    EA = random.randint(4, 10)

    print(f'enemy attack power: {EA}')

    if 1 <= frame_num <= 5:

        # block animation
        print('block!')

        path13 = "C:/Users/User/Desktop/GIF/block.gif"
        im1 = Image.open(path13)

        fig, ax = plt.subplots(figsize=(8, 10), facecolor='black')
        plt.get_current_fig_manager().window.wm_geometry('+485+0')

        ani1 = animation.FuncAnimation(fig, update, frames=im1.n_frames, interval=50, blit=True, repeat=False)

        plt.show(block=False)
        plt.axis('off')
        plt.pause(3)
        plt.close()

        HP = HP - EA*0.2
        print(f'damage: {EA*0.2}')
        print(f'your HP: {HP}')

    elif 6 <= frame_num <= 10:

        # dodge QTE
        path14 = "C:/Users/User/Desktop/GIF/QTEdodge.gif"
        im = Image.open(path14)

        fig, ax = plt.subplots(figsize=(8, 10), facecolor='black')
        plt.get_current_fig_manager().window.wm_geometry('+485+0')

        ani = animation.FuncAnimation(fig, update_qte, frames=im.n_frames, interval=50, blit=True)

        plt.axis('off')
        plt.show()

        if frame_num == 6:

            print('successful dodge')

            # dodge animation
            path15 = "C:/Users/User/Desktop/GIF/dodge.gif"
            im1 = Image.open(path15)

            fig, ax = plt.subplots(figsize=(8, 10), facecolor='black')
            plt.get_current_fig_manager().window.wm_geometry('+485+0')

            ani1 = animation.FuncAnimation(fig, update, frames=im1.n_frames, interval=50, blit=True, repeat=False)

            plt.show(block=False)
            plt.axis('off')
            plt.pause(3)
            plt.close()

            print(f'damage: 0')
            print(f'your HP: {HP}')

        else:

            print('dodge failed')

            # fail animation
            path16 = "C:/Users/User/Desktop/GIF/fail.gif"
            im1 = Image.open(path16)

            fig, ax = plt.subplots(figsize=(8, 10), facecolor='black')
            plt.get_current_fig_manager().window.wm_geometry('+485+0')

            ani1 = animation.FuncAnimation(fig, update, frames=im1.n_frames, interval=50, blit=True, repeat=False)

            plt.show(block=False)
            plt.axis('off')
            plt.pause(3)
            plt.close()

            HP = HP - EA

            print(f'damage: {EA}')
            print(f'your HP: {HP}')

    else:

        # parry QTE
        path17 = "C:/Users/User/Desktop/GIF/QTE_parry.gif"
        im = Image.open(path17)

        fig, ax = plt.subplots(figsize=(8, 10), facecolor='black')
        plt.get_current_fig_manager().window.wm_geometry('+485+0')

        ani = animation.FuncAnimation(fig, update_qte, frames=im.n_frames, interval=25, blit=True)

        plt.axis('off')
        plt.show()

        if 2 < frame_num < 10:

            print('successful parry!')

            # parry animation
            path18 = "C:/Users/User/Desktop/GIF/parry.gif"
            im1 = Image.open(path18)

            fig, ax = plt.subplots(figsize=(8, 10), facecolor='black')
            plt.get_current_fig_manager().window.wm_geometry('+485+0')

            ani1 = animation.FuncAnimation(fig, update, frames=im1.n_frames, interval=50, blit=True, repeat=False)

            plt.show(block=False)
            plt.axis('off')
            plt.pause(3)
            plt.close()

            # parry damage calculation
            if frame_num == 6:
                E = E - EA
                print(f'damage: {EA}')
                print(f'enemy HP: {E}')
            elif frame_num == 5 or frame_num == 7:
                E = E - EA*0.7
                print(f'damage: {EA*0.7}')
                print(f'enemy HP: {E}')
            elif frame_num == 4 or frame_num == 8:
                E = E - EA*0.5
                print(f'damage: {EA*0.5}')
                print(f'enemy HP: {E}')
            elif frame_num == 3 or frame_num == 9:
                E = E - EA*0.3
                print(f'damage: {EA*0.3}')
                print(f'enemy HP: {E}')

        else:

            HP = HP - EA

            print('parry failed!')
            print(f'damage: {EA}')
            print(f'your HP: {HP}')

            # fail animation
            path19 = "C:/Users/User/Desktop/GIF/fail.gif"
            im1 = Image.open(path19)

            fig, ax = plt.subplots(figsize=(8, 10), facecolor='black')
            plt.get_current_fig_manager().window.wm_geometry('+485+0')

            ani1 = animation.FuncAnimation(fig, update, frames=im1.n_frames, interval=50, blit=True, repeat=False)

            plt.axis('off')
            plt.show(block=False)
            plt.pause(3)
            plt.close()

        if HP <= 0 or E <= 0:
            break

if HP > 0:

    # victory screen
    path20 = "C:/Users/User/Desktop/GIF/victory.gif"
    im1 = Image.open(path20)

    fig, ax = plt.subplots(figsize=(8, 10), facecolor='black')
    plt.get_current_fig_manager().window.wm_geometry('+485+0')

    ani1 = animation.FuncAnimation(fig, update, frames=im1.n_frames, interval=200, blit=True, repeat=False)

    plt.axis('off')
    plt.show(block=False)
    plt.pause(15)
    plt.close()

else:

    # death screen
    path21 = "C:/Users/User/Desktop/GIF/death.gif"
    im1 = Image.open(path21)

    fig, ax = plt.subplots(figsize=(8, 10), facecolor='black')
    plt.get_current_fig_manager().window.wm_geometry('+485+0')

    ani1 = animation.FuncAnimation(fig, update, frames=im1.n_frames, interval=200, blit=True, repeat=False)

    plt.axis('off')
    plt.show(block=False)
    plt.pause(15)
    plt.close()
