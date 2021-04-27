path_f = '/Users/communityproject/Downloads/checkin/dataset_TIST2015/'
temp = 1
fileName = path_f + str(temp)
fp = open(fileName,'w+')
with open('/Users/communityproject/Downloads/checkin/dataset_TIST2015/dataset_TIST2015_Checkins.txt', 'r')as reader:
    line = reader.readline()
    fp.write(line)
    counter = 1
    while line:
        if counter == 6652729:
            fp.close()
            temp = temp + 1
            fileName = path_f + str(temp)
            fp = open(fileName,'w+')
            counter = 0
        counter = counter + 1
        fp.write(line)
        line = reader.readline()
    # print counter

#合并
def merge(input1, input2, input3, input4, input5, output):
    with open(output, 'w') as writer:
        with open(input1, 'r') as reader:
            lines = reader.readlines()
            for line in lines:
                writer.write(line)
        with open(input2, 'r') as reader:
            lines = reader.readlines()
            for line in lines:
                writer.write(line)

        with open(input3, 'r') as reader:
            lines = reader.readlines()
            for line in lines:
                writer.write(line)
        with open(input4, 'r') as reader:
            lines = reader.readlines()
            for line in lines:
                writer.write(line)
        with open(input5, 'r') as reader:
            lines = reader.readlines()
            for line in lines:
                writer.write(line)


if __name__ == "__main__":
    merge(input1='',
          input2='',
          input3='',
          input4='',
          input5='',
          output='')