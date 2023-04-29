import boto3
path = 'D:/subishkrish/split/'
s3 = boto3.client('s3')
s3.download_file('private2proj', 'part2/randm.txt.part2', 'D:/subishkrish/downloaded/part1 and part2/random02.part2')
s3.download_file('my-project02', 'part1/randm.txt.part1', 'D:/subishkrish/downloaded/part1 and part2/random01.part1')

path = 'D:/subishkrish/downloaded/part1 and part2/'

with open(path + 'random01.part1', 'rb') as file1, \
     open(path + 'random02.part2', 'rb') as file2, \
     open('D:/subishkrish/downloaded/random.txt', 'wb') as output_file:
    
    output_file.write(file1.read())
    output_file.write(file2.read())