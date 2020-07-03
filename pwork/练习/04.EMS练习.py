## EMS（Employee Manager System 员工管理系统） 练习
    # - 做命令行版本的员工管理系统
    # - 功能：
    #     四个：
    #         1.查询
    #             - 显示当前系统当中的所有员工
    #         2.添加
    #             - 将员工添加到当前系统中
    #         3.删除
    #             - 将员工从系统当中删除
    #         4.退出
    #             - 退出系统
    # - 员工信息要保存到哪里？ 列表，在系统中应该有一个列表，专门用来保存所有员工信息的 

emps = ['张三\t18\t男\t江苏','李四\t19\t男\t北京']


while True :
    print('='*20,' 欢迎使用员工管理系统 ','='*20)
    print('请选择要做的操作')
    print('\t1.查询员工')
    print('\t2.添加员工')
    print('\t3.删除员工')
    print('\t4.退出系统')

    choose = input('请选择[1-4]：')
    print('='*62)

    if choose == '1' :
        # 查询
        print('\t序号\t姓名\t年龄\t性别\t住址')
        n = 1
        for emp in emps :
            print(f'\t{n}\t{emp}')
            n += 1
    elif choose == '2' :
        # 添加
        name = input('请输入姓名：')
        age = input('请输入年龄：')
        gender = input('请输入性别：')
        address = input('请输入住址：')
        print(f'姓名：{name}，年龄：{age}，性别：{gender}，住址：{address}')
        confirm = input('确认添加该信息[Y/N]：')
        if confirm == 'Y' or confirm == 'y':
            # 添加
            emps.append(f'{name}\t{age}\t{gender}\t{address}')
    elif choose == '3' :
        # 删除
        num = int(input(f'请选择[1-{len(emps)}]：'))
        if 0 < num <= len(emps) :
            confirm = input('确认删除该信息[Y/N]：')
            if confirm == 'Y' or confirm == 'y':
                emps.pop(num-1)
        else :
            print('请选择存在的员工信息！')

    elif choose == '4' :
        # 退出
        input('欢迎下次再来！按回车键退出系统！')
        break
    else :
        # 选择错误
        print('请选择正确的操作！')

    print('='*62)