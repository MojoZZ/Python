#字符串相乘表示字符串的复制
print('-'*20,' 欢迎关林《唐僧大战白骨精》 ','-'*20)
print('请选择你的身份：\n\t\t1.唐僧\n\t\t2.白骨精')

identity = input('请选择[1-2]：')

print('-'*66)

player_life = 2
player_attack = 2

boss_life = 10
boss_attack = 10

if identity == '1' :
	print('你已经选择了1，你将以->唐僧<-的身份来进行游戏！')
elif identity == '2' :
	print('你竟然选择了白骨精，太不要脸，你将以->唐僧<-的身份来进行游戏！')
else :
	print('你的选择有误，系统将自动分配身份，你将以->唐僧<-的身份来进行游戏！')

print('-'*66)
print(f'唐僧，你的生命值是{player_life}，你的攻击力是{player_attack}')
print('-'*66)

# op = '1'
# while op == '1' :
while True :

	print('请选择你要进行的操作：\n\t\t1.练级\n\t\t2.打BOSS\n\t\t3.逃跑')
	op = input('请选择要做的操作[1-3]：')

	if op == '1' :
		player_life += 2
		player_attack += 2
		print(f'唐僧，你的生命值是{player_life}，你的攻击力是{player_attack}')
	elif op == '2' :
		boss_life -= player_attack
		if boss_life <= 0:
			print('白骨精已经成功消灭，恭喜你闯关成功!')
			break

		player_life -= boss_attack
		if player_life <= 0 :
			print('你已经死亡，闯关失败!')
			break
	elif op == '3' :
		print('-'*66)
		print('你竟然逃跑!')
		break
	else :
		print('-'*66)
		print('你的选择有误，请重新选择！')




