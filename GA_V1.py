import random
import numpy as np
from functools import partial
from fitness import fitness
from figure import plot_elements




# 初始化种群
def initialize_population(tasks, population_size):
    population = []
    task_indices = list(range(len(tasks)))
    for _ in range(population_size):
        individual = task_indices[:]
        random.shuffle(individual)
        population.append(individual)
    return population



# 选择父代
def selection(population, fitnesses):
    selected = random.choices(population, weights=fitnesses, k=2)
    return selected[0], selected[1]

# 单点交叉
def crossover(parent1, parent2):
    size = len(parent1)
    cx_point = random.randint(1, size - 1)
    child1 = parent1[:cx_point] + [item for item in parent2 if item not in parent1[:cx_point]]
    child2 = parent2[:cx_point] + [item for item in parent1 if item not in parent2[:cx_point]]
    return child1, child2

# 变异
def mutate(individual, mutation_rate=0.1):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(individual) - 1)
            individual[i], individual[j] = individual[j], individual[i]

# 遗传算法
def genetic_algorithm(tasks_name,tasks, population_size, generations,wait_coefficients,max_work_time,rest_time):
    population = initialize_population(tasks, population_size)
    # 初始化全局最佳适应度和最佳个体
    global_best_individual = None
    global_best_fitness = float('inf')
    global_best_batch = None
    global_best_fitness_fo=[]

    # 部分应用fitness函数，使其只需要一个参数individual
    fitness_with_params = partial(fitness, tasks=tasks, wait_coefficients=wait_coefficients,
                                  max_work_time=max_work_time, rest_time=rest_time)

    for generation in range(generations):
        fitnesses = [ fitness(individual,tasks,wait_coefficients,max_work_time,rest_time)[0] for individual in population]  # 适应度越小越好，取倒数
        # fitnesses = [fitness(individual) for individual in population]
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = selection(population, fitnesses)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        population = new_population
        # 找到当前代的最佳个体
        best_individual = min(population, key=lambda ind: fitness(ind,tasks,wait_coefficients,max_work_time,rest_time)[0])
        best_fitness, best_batch = fitness(best_individual,tasks,wait_coefficients,max_work_time,rest_time)

        # 更新全局最佳个体和适应度
        if best_fitness < global_best_fitness:
            global_best_individual = best_individual
            global_best_fitness = best_fitness
            global_best_fitness = round(global_best_fitness, 2)
            # global_best_fitness = "{:.2f}".format(global_best_fitness)#限制两位小数输出
            global_best_batch = best_batch
            global_best_fitness_fo.append(global_best_fitness)
        else:
            global_best_fitness_fo.append(global_best_fitness)
        best_individual = min(population, key=fitness_with_params)
        # 按照新位置数组的顺序输出任务名
        new_task_order = [tasks_name[pos] for pos in best_individual]
        best_fitness,batch02 = fitness(best_individual,tasks,wait_coefficients,max_work_time,rest_time)
        batch_task_names = [[tasks_name[pos] for pos in batch] for batch in batch02]
        # print(f"第{generation}批次迭代完成,本轮最佳顺序{new_task_order},本轮最佳适应度{best_fitness},任务批次{batch_task_names}")

    plot_elements(global_best_fitness_fo)
    global_best_individual_out=[tasks_name[pos] for pos in global_best_individual]
    global_best_batch_out=[[tasks_name[pos] for pos in batch] for batch in global_best_batch]

    return global_best_individual_out, global_best_fitness, global_best_batch_out


