import statistics
import numpy as np


class HandSensor:
    all_avg_values = {}
    avg_of_all_avg = {}
    ts_records = {}

    def __init__(self, timestamps, left_heights, right_heights):
        self.average_heights = None
        self.ts = None
        self.timestamps = timestamps
        self.left_heights = left_heights
        self.right_heights = right_heights


   
    # def compute_average_heights(self, timestamps, left_heights, right_heights):
    def avgPressure(self):
        # if it has only 1-2 samples, we would omit the case
        if len(self.timestamps) < 3:
            return print(f'too less data available, not trustworthy')
       
        ## If the data seems noisy, requires multi step cleaning
        # firstly figuring out the data list without -100 (which is a wrong measurement)
        left_valid_heights = [h for h in self.left_heights if h != -100]
        right_valid_heights = [h for h in self.right_heights if h != -100]
        
        # finding out the percentage of correct data approximately
        left_ratio = len(left_valid_heights) / len(self.left_heights)
        right_ratio = len(right_valid_heights) / len(self.right_heights)
        
        # we're considering the list as valid if less than 10% data are wrongly measured
        if left_ratio < 0.1 or right_ratio < 0.1:
            print(f'ratio is too low')
            #return None
    

        # checking whether interpolation needed
        left_valid_heights  = self.interpolation(left_valid_heights)
        right_valid_heights = self.interpolation(right_valid_heights)

 
        # after all the cleaning, calcuating averages with cleaned data points      
        left_avg  = statistics.mean(left_valid_heights)
        right_avg = statistics.mean(right_valid_heights)
       
       
        avg_heights = (left_avg, right_avg)
        self.average_heights = avg_heights
        
        # keeping a track of how many time stamps were taken
        self.ts = (len(left_valid_heights), len(right_valid_heights))

        self.store_avg()

       
    def store_avg(self):
        existing_avg_counter = len(self.all_avg_values)
        key_id = 't_'+str(existing_avg_counter + 1)
        self.all_avg_values[key_id] =  self.average_heights
        # print(f'final avg detail: {self.average_heights}')
        self.ts_records[key_id+'_count'] = self.ts


        l_av = 0; r_av = 0
        for i, x in enumerate(self.all_avg_values):
            div = i + 1
            l_av = l_av + self.all_avg_values[x][0]
            l_av = l_av / div
            r_av = r_av + self.all_avg_values[x][1]
            r_av = r_av / div
            # print(f'each avg detail: {self.all_avg_values[x][0]}')
        # print(f'total avg detail: {l_av}, and {r_av}')
        self.avg_of_all_avg['t'] =  (l_av, r_av)





    def print_all_avg(self):
        print(f'avg of hand heights at diff timestamp: {self.all_avg_values}')
        # how many data points were taken for that particular time span
        print(f'timestamp records: {self.ts_records}')

        print(f'final average detail: {self.avg_of_all_avg}')


    
    def interpolation(self, lst):

        # print(f'dirty_data: {lst}')

        
        # we are assuming the difference between two consequtive valid data points can not 
        # exceed more than 100mm
        thrshld = 100
        # finding difference between two consequtive data points
        diff_temp_array = np.diff(np.array(lst))
        # print(f'diff: {diff_temp_array}')

        invalid_indices = [] # it holds the invalid indexes of the hand height data points
        # we are checking multiple cases based on index position
        for i, x in enumerate(diff_temp_array):
            # case 1 - if first index needs interpolation [the difference between adjacent data points
            # are more than 100]
            if i == 0 and abs(x) > thrshld:
                invalid_indices.append(i)
            # case 2 - if last index interpolation
            elif i == len(diff_temp_array) - 1 and abs(x) > thrshld:
                invalid_indices.append(i+1)
            # case 3 - if interpolation needed in middle indexes
            elif i > 0 and i < len(diff_temp_array) - 1 and abs(x) > thrshld and abs(diff_temp_array[i+1]) > thrshld:
                invalid_indices.append(i+1)

        ls_tmp = lst
        # creating a list after ommiting invalid hand height data points to get 
        # mean value of remaining valid data points
        ls_tmp = [i for j, i in enumerate(ls_tmp) if j not in invalid_indices]
        # print(statistics.mean(ls_tmp))

        # replacing invalid data points with the calculated mean of valid data
        for x in invalid_indices:
            lst[int(str(x))] = round(statistics.mean(ls_tmp))

        # print(f'clean_data: {lst}')

        return lst
       
       
       
if __name__ == "__main__":
    ts = [0.091, 0.165, 0.223, 0.318, 0.373, 0.429, 0.481, 0.559, 0.638, 0.734]
    lh = [275, 272, 271, 268, 19, 265, 260, 261, 262, 260]
    rh = [-100, 201, 202, 210, 222, 220, 199, -100, 195, 189]
    
    h  = HandSensor(ts, lh, rh) 
    h.avgPressure()
    
    ts = [2.057, 2.114, 2.208, 2.304, 2.338, 2.428, 2.523, 2.595, 2.659, 2.738]
    lh = [-100, -100, -100, -100, 300, -100, 299, -100, -100, 299]
    rh = [177, 164, 158, 151, 153, 147, 145, -100, -100, 1]

    h  = HandSensor(ts, lh, rh)
    h.avgPressure()
    
    h.print_all_avg()