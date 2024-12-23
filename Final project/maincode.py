import math
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------------------------
# extract fecal

# creation of the function to extract fecal from the file data_real.csv
def extract_sample_types(filepath, outpath, sample_types):
    # open in read-only mode
    fd1 = open(filepath, 'r')
    # open in write-only mode
    fd2 = open(outpath, 'w')
    
    # retrieve the next line (skip)
    line = fd1.readline()
    fd2.write(line)

    # retrieve all next lines
    while line != '':
        # retrieve ONE line
        line = fd1.readline()
        # stop when there's no more line
        if line == '':
            break
        
        # remove the new_line character
        line = line.replace('\n', '')
        # Split line with ";"
        valueList = line.split(';')
        
        # check if list has the good length
        if len(valueList) < 3:
            continue
        
        # Retrieve sample type (fecal here) from the third column
        sample_type = valueList[2]
        
        # write the line in output file if the sample type is fecal
        if sample_type in sample_types:
            fd2.write(line + '\n')
    
    # Close input and output file
    fd1.close()
    fd2.close()

# Extract fecal samples from the file data_real.csv
input_file = 'data_real.csv'
output_file = 'fecal_samples.csv'
sample_types = ['fecal']

extract_sample_types(input_file, output_file, sample_types)


# -------------------------------------------------------------------------
# extract ileal


# use the same function again to extract ileal from the file data_real.csv
def extract_sample_types(filepath, outpath, sample_types):
    # open in read-only mode
    fd1 = open(filepath, 'r')
    # open in write-only mode
    fd2 = open(outpath, 'w')
    
    # retrieve the next line (just to skip it)
    line = fd1.readline()
    fd2.write(line)

    #retrieve all next lines
    while line != '':
        # retrieve ONE line
        line = fd1.readline()
        # stop when there's no more line
        if line == '':
            break
        
        # remove the new_line character
        line = line.replace('\n', '')
        # Split line with ";"
        valueList = line.split(';')
        
        # check if list has the good length
        if len(valueList) < 3:
            continue
        
        # Retrieve sample type (ileal here) from the third column
        sample_type = valueList[2]
        
        # write the line in output file if the sample type is ileal
        if sample_type in sample_types:
            fd2.write(line + '\n')
    
    # Close input and output file
    fd1.close()
    fd2.close()

# Extract ileal samples from the file data_real.csv
input_file = 'data_real.csv'
output_file = 'ileal_samples.csv'
sample_types = ['ileal']

extract_sample_types(input_file, output_file, sample_types)



# ------------------------------------------------------------------------------------------------
# extract cecal


# use the same function again to extract cecal from the file data_real.csv
def extract_sample_types(filepath, outpath, sample_types):
    # open in read-only mode
    fd1 = open(filepath, 'r')
    # open in write-only mode
    fd2 = open(outpath, 'w')
    
    # retrieve the next line (just to skip it)
    line = fd1.readline()
    fd2.write(line)

    #retrieve all next lines
    while line != '':
        # retrieve ONE line
        line = fd1.readline()
        # stop when there's no more line
        if line == '':
            break
        
        # remove the new_line character
        line = line.replace('\n', '')
        # Split line with ";"
        valueList = line.split(';')
        
        # check if list has the good length
        if len(valueList) < 3:
            continue
        
        # Retrieve sample type (cecal here) from the third column
        sample_type = valueList[2]
        
        # write the line in output file if the sample type is cecal
        if sample_type in sample_types:
            fd2.write(line + '\n')
    
    # Close input and output file
    fd1.close()
    fd2.close()

# Extract cecal samples from the file data_real.csv
input_file = 'data_real.csv'
output_file = 'cecal_samples.csv'
sample_types = ['cecal']

extract_sample_types(input_file, output_file, sample_types)




# ----------------------------------------------------------------------------------- 
# Draw the graphs




# creation of the function to create a graph
def renderCecal(filepath, outpath, sample_types):
    figure, axes = plt.subplots()

    # set title and axes
    axes.set_title('Cecal live bacteria')
    axes.set_ylabel('log10(live bacteria/wet g)')
    axes.set_xlabel('Treatment')

    # open in read-only mode
    fd1 = open(filepath, 'r')
    # retrieve the next line (skip)
    line = fd1.readline()

    # initialize data
    treatment = '' 
    x_ABX = []
    y_ABX = []
    x_placebo = []
    y_placebo = []
    x_ABX_axis = 2
    x_placebo_axis = 5

    # process each line
    while line != '':
        line = fd1.readline()
        if line == '':
            break
        
        # split line with ";"
        valueList = line.split(';')

        # retrieve values
        sample_type = valueList[2]
        treatment = valueList[5]

        # process ABX
        if (sample_type == sample_types) and (treatment == 'ABX'):
            # apply log 10
            bct = math.log(float(valueList[8])) / math.log(10)
            # fill X values
            x_ABX.append(x_ABX_axis)
            # fill Y values
            y_ABX.append(bct)
            color = 'blue'

        # Process Placebo
        if (sample_type == sample_types) and (treatment == 'placebo'):
            # apply log 10
            bct = math.log(float(valueList[8])) / math.log(10)
            # fill X values
            x_placebo.append(x_placebo_axis)
            # fill Y values
            y_placebo.append(bct)
            color = 'orange'

    # combine and customize appearance for violin graph
    data = [y_ABX, y_placebo]
    vp = axes.violinplot(data)
    vp['bodies'][0].set_facecolor('blue')
    vp['bodies'][1].set_facecolor('orange')
    axes.violinplot(data)

    # close input
    fd1.close()

    # Save as image
    figure.savefig(outpath, dpi=300)

# ------same for ileal



# creation of the function to create a graph
def renderFecal(filepath, outpath, sample_types):
    figure, axes = plt.subplots()

    # set title and axes
    axes.set_title('Fecal live bacteria')
    axes.set_ylabel('log10(live bacteria/wet g)')
    axes.set_xlabel('Washout day')

    # iterate in a range depending the mouse IDs
    for mouse_Id in range(17, 33):
        # open in read-only mode
        fd1 = open(filepath, 'r')
        # read the first line
        line = fd1.readline()

        # initialize
        treatment = ''
        x = []
        y = []

        # process each line
        while line != '':
            line = fd1.readline()
            if line == '':
                break

            # split line with ";"
            valueList = line.split(';')

            # retrieve values
            # extract sample type from column 3
            sample_type = valueList[2]
            # extract mouse ID from column 5 and remove ABX if present
            mid = int(valueList[4].replace('ABX', ''))

            #check if the sample type match with fecal and if mouse_id match current in the loop
            if (sample_type == sample_types) and (mid == mouse_Id):

                # fill datas
                treatment = valueList[5]
                day = int(valueList[7])
                bct = math.log(float(valueList[8]))/math.log(10)
                # fill X values
                x.append(day)
                # fill Y values
                y.append(bct)
        
        # close input
        fd1.close()

        # design
        color = ''
        if treatment == 'ABX':
            color = 'blue'
        else:
            color = 'orange'

        axes.plot(x,y, color)

        axes.plot(x,y, color, label=treatment)
        axes.legend(loc='lower right', fontsize=4, title="Type Traitement")
        
    # Save as image
    figure.savefig(outpath, dpi=300)




# same as cecal
def renderIleal(filepath, outpath, sample_types):
    figure, axes = plt.subplots()

    axes.set_title('Ileal live bacteria')
    axes.set_ylabel('log10(live bacteria/wet g)')
    axes.set_xlabel('Treatment')

    fd1 = open(filepath, 'r')
    line = fd1.readline()

    treatment = ''
    x_ABX = []
    y_ABX = []
    x_placebo = []
    y_placebo = []
    x_ABX_axis = 2
    x_placebo_axis = 5

    while line != '':
        line = fd1.readline()
        if line == '':
            break

        valueList = line.split(';')

        sample_type = valueList[2]
        treatment = valueList[5]

        if (sample_type == sample_types) and (treatment == 'ABX'):
            bct = math.log(float(valueList[8])) / math.log(10)
            x_ABX.append(x_ABX_axis)
            y_ABX.append(bct)

        if (sample_type == sample_types) and (treatment == 'placebo'):
            bct = math.log(float(valueList[8])) / math.log(10)
            x_placebo.append(x_placebo_axis)
            y_placebo.append(bct)

    data = [y_ABX, y_placebo]
    vp = axes.violinplot(data)
    vp['bodies'][0].set_facecolor('blue')
    vp['bodies'][1].set_facecolor('orange')
    fd1.close()


    figure.savefig(outpath, dpi=300)

# name and define input and output
input_file = 'data_real.csv'
output_ileal = 'ileal_samples.png'
output_cecal = 'cecal_samples.png'
output_fecal = 'fecal_samples.png'
sample_types = ['cecal', 'fecal', 'ileal']

# generate graph
renderFecal(input_file,output_fecal,sample_types[1])
renderCecal(input_file,output_cecal,sample_types[0])
renderIleal(input_file,output_ileal,sample_types[2])
