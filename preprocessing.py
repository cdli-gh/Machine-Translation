from pickle import dump

def save_clean_data(sentences, filename):
	dump(sentences, open(filename, 'wb'))
	print('Saved: %s' % filename)

# Opening and reading text from English tarin file
fileaname_eng = 'english_train.txt'
file_eng = open(fileaname_eng, encoding='utf-8')
text_eng = file_eng.read()
file_eng.close()

#Spliting document into sentances......Encoding 'utf-8' gives '\n' on new lines
lines_eng = text_eng.strip().split('\n')

# Opening and reading text file from Sumerian tarin file
filename_sum = 'sumerian_train.txt'
file_sum = open(filename_sum, encoding='utf-8')
text_sum = file_sum.read()
file_sum.close()

lines_sum = text_sum.strip().split('\n')

# Pairing text from both files..
pairs = []
for i in range(len(lines_sum)):
    pairs.append([lines_eng[i],lines_sum[i]])

""" .pkl files are form of data stream, read by python,
they process data as data datastrem, so better to train model with datastrem"""

# Saving all pairs as .pkl file
save_clean_data(pairs,'eng-sum.pkl')

# Spliting same file as test and train....although differnt file are given we can use them too
train, test = pairs[:13000], pairs[13000:]
save_clean_data(train, 'eng-sum_train.pkl')
save_clean_data(test, 'eng-sum_test.pkl')


