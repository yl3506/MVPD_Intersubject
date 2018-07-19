# visualization of overall mean variance explained within subject raw
import os
import numpy as np
import matplotlib.pyplot as plt

# initialize parameters
work_dir = '/Users/chloe/Documents/output_denoise_pca_1_cross/'
main_out_dir = '/Users/chloe/Documents/'
### work_dir = '/mindhive/saxelab3/anzellotti/forrest/output_denoise_pca_1_cross/'
### main_out_dir = '/mindhive/saxelab3/anzellotti/forrest/'
all_subjects = ['sub-01', 'sub-02', 'sub-03', 'sub-04', 'sub-05', 'sub-09', 'sub-10', 'sub-14', 'sub-15', 'sub-16', 'sub-17', 'sub-18', 'sub-19', 'sub-20']
all_masks = ['rOFA', 'rFFA', 'rATL', 'rSTS']
total_run = 8
figure_min = 0
figure_max = 2
title_y = 1.15
labelpad_x = -245
data = np.zeros((len(all_masks), len(all_masks))) # initialize overall mean data matrix

# iterate through all combinations of subjects (including within subject)
for sub_index in range(0, len(all_subjects)):
	
	# initialize info
	subject = all_subjects[sub_index]
	sub_dir = work_dir + subject + '_to_' + subject + '/'
	data_dir = sub_dir + subject + '_to_' + subject + '_raw_ratio_chart.npy'
	if not os.path.exists(main_out_dir):
		os.makedirs(main_out_dir)
	# load data
	data += np.load(data_dir)

# calculate mean of all matrices
data = data / len(all_subjects)
# generate figure
plt.matshow(data, vmin=figure_min, vmax=figure_max) # plot matrix
plt.xticks(np.arange(len(all_masks)), all_masks) # set x axis tick
plt.yticks(np.arange(len(all_masks)).T, all_masks) # set y axis tick
plt.colorbar() # show color bar
plt.ylabel('Predictor') # set y axis label
plt.title(subject + ' to ' + subject + ' overall mean var explained raw', y=title_y) # set title
plt.xlabel('Target', labelpad=labelpad_x) # set x axis label
out_dir = main_out_dir + 'overall_within_raw_pc_1.png'
plt.savefig(out_dir) # save figure