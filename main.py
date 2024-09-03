from GA_V1 import genetic_algorithm


# 参数设置
rest_time = 10  #机器维修时间
max_work_time= 20  #机器允许的单批次最大时间
population_size = 30  #搜索种群
generations = 300  #最大迭代次数

# 任务和等待系数

# #情况1 10个任务
# tasks_name = ["A","B", "C", "D", "E" , "F" , "G" , "H" , "I" , "J" ]  #任务名称
# tasks_time = [2, 2, 3, 4, 6, 7 , 2 , 1 , 6 ,4]  #任务理想时间
# wait_coefficients = [0.1, 0.2, 0.4, 0.3, 0.1,0.5,0.7,0.2,0.1,0.2]  #任务劣化率

#情况2 15个任务
# tasks_name = ["A","B","C","D","E","F","G","H","I","J","K","L","M","O","P"]  #任务名称
# tasks_time = [2,2,3,4,6,7,2,1,6,4,3,2,2,1,4]  #任务理想时间
# wait_coefficients = [0.1,0.2,0.4,0.3,0.1,0.5,0.7,0.2,0.1,0.2,0.2,0.1,0.3,0.1,0.2]  #任务劣化率
#
#
# # 运行遗传算法
# optimal_batches, min_time,best_batch = genetic_algorithm(tasks_name,tasks_time, population_size, generations,wait_coefficients,max_work_time,rest_time)
# print("最佳任务顺序：", optimal_batches)
# print("最优总用时：", min_time)
# print("最优任务批次：" )
# for i, batch in enumerate(best_batch):
#     print(f"批次 {i + 1}: {batch}")

