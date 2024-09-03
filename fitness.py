
def fitness(individual,tasks,wait_coefficients,max_work_time,rest_time):
    N = len(individual)

    total_time = 0  # 初始化总时间
    batch_time = 0  # 当前批次累计时间
    actual_time_list = []  # 存储当前批次中所有任务的实际完成时间
    batches = []  # 存储所有批次
    current_batch = []  # 当前批次的任务


    for i in individual:
        ideal_time = tasks[i]
        wait_factor = wait_coefficients[i]

        if batch_time == 0:
            # 如果是批次的第一个任务，等待时间为0
            actual_time = ideal_time
        else:
            # 否则，计算等待时间
            wait_time = sum(actual_time_list) * wait_factor
            actual_time = ideal_time + wait_time

        # 检查是否需要开始一个新的批次
        if batch_time + actual_time > max_work_time:
            total_time += rest_time
            batches.append(current_batch)
            batch_time = 0
            actual_time_list = []
            current_batch = []
            actual_time = ideal_time  # 重新计算，因为当前任务是新批次第一个任务

        # 增加当前任务的实际时间到当前批次和总时间
        batch_time += actual_time
        actual_time_list.append(actual_time)
        total_time += actual_time
        current_batch.append(i)

        # 当任务是最后一个任务时，检查并处理批次结束
        if i == individual[-2]:
            batches.append(current_batch)
            total_time += rest_time
            batch_time = 0
            actual_time_list = []

    # 返回总完成时间
    return total_time - rest_time,batches