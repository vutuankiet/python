from math import dist, fabs, trunc
import pygame
import random
pygame.init()
screen =  pygame.display.set_mode((600,600))
#update manf hing
pygame.display.update()
#set tên game
pygame.display.set_caption("Snake - By Khanh+Kiet")

clock=pygame.time.Clock()#set delay cho game nếu vòng lặp nhanh quá sẽ tràn ram và cpu lên phải set delay 
#thêm ít màu tôi dùng rgb
black=(0,0,0)
red=(255,0,0)#lâu không dùng quên mã rồi...
#set speed
snake_speed=15
snake_size=10
font_style=pygame.font.SysFont(None,20)

# tạo hàm đề thông báo
def message(content,color):
    msg=font_style.render(content,True,color)#tạo 1 dòng chữ với nội dung là content và màu là color
    screen.blit(msg,[600/3,600/3]) #set vị trí và vẽ bằng hàm blit mà không phải rect vì rect sẽ nặng hơn 
    #chỉ dùng rect vẽ các đối tượng cần xử lý nhiều => đối tượng chính 

#chuyển hết thành hàm
#hàm quản lý rắn
def snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(screen,black,[x[0],x[1],snake_block,snake_block])
def showScores(score):
    value=font_style.render("Your Scores: "+str(score),True,(255, 255, 102))
    screen.blit(value,[0,0])
def main():
    #tao 1 snake list
    snake_list=[]
    snake_length=1
    #set tọa độ khởi đầu 
    x1,y1=300,300
    #tọa độ thay đổi
    x1_change,y1_change=0,0
    #làm thức ăn
    foodx=round(random.randrange(0,600-10)/10.0)*10.0
    foody=round(random.randrange(0,600-10)/10.0)*10.0
    #rand toạ độ của thức ăn từ 0->width của màn - width của rắn
    # ok?
    gameClosed=False
    # bien nay dung de thoat han game
    gameOver=False
    #con đây chỉ là chơi lại thôi
    while gameClosed == False:
        
        #hàm thua
        while  gameOver ==True:
            screen.fill((255,255,255))
            message("You Lost ! Press C To PLay Again Or Q to QUIT ",(0,0,0))
            pygame.display.update() 
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameClosed=True
                        gameOver=False
                    if event.key==pygame.K_c:
                        main()
                        
        #main loop này để bắt sự kiện
        for event in pygame.event.get():
            #set quit game
            if event.type == pygame.QUIT:
                gameClosed=True
            #bắt sự kiện ấn phím xuống
            if event.type == pygame.KEYDOWN:
                #key left
                if event.key ==  pygame.K_LEFT:
                    #sang trai 
                    x1_change = -10
                    y1_chancge = 0

                #key right
                if event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                #key up
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                #key down
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10
        #set game over
        #rắn sẽ chết khi chạm ranh giới hoặc cắn vô chính nó
        #chạm ranh giới trước 
        if x1 >= 600 or x1 < 0 or y1 >= 600 or y1 < 0:
            if x1 >= 600:
                x1=0
            if x1 < 0:
                x1=600
            if y1 >= 600:
               y1=0
            if y1 < 0:
                y1=600        
        #cắn vào bản thân 
        #     
       
        #set posi
        x1+=x1_change
        y1+=y1_change
        screen.fill((255,255,255))
         #thêm thức ăn
        pygame.draw.rect(screen,red,[foodx,foody,snake_size,snake_size])
        # draw new food
        # pygame.draw.rect(screen,black,[x1,y1,snake_size,snake_size])
        #cái đằng sau theo thứu tự là : màn , màu đối tượng, vị trí x , vị trí y chiều dài, chiều rộng
        #sau khi ve thi phai update lai nha
        #add block 
        snake_head=[]
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]: #  for từ cuối lên đầu
            #nếu cái x == cái đầu tiền => cắn vào người
            if x==snake_head: 
                gameOver=True#game of
        snake(snake_size,snake_list)
        showScores(snake_length-1)
       
        if  x1 == foodx and y1 == foody:
            foodx=round(random.randrange(0,600-10)/10.0)*10.0 # 
            foody=round(random.randrange(0,600-10)/10.0)*10.0
            snake_length+=1
        pygame.display.update()
       
        #set delay
        clock.tick(snake_speed)

    pygame.quit()
    quit()

#đây là loop của game 1 con game luôn luôn là 1 vòng lặp 
main()


