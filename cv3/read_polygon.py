__author__ = 'bruno'
from collections import defaultdict
import sys
def xx():
    print("----brake----")
    sys.exit(0)

import csv


train = open("artificial_separable_train.csv").read().split("\n"); train = list(map(lambda _:_.split(","),train)); train = train[:-1] #DROP last
test = open("artificial_separable_test.csv").read().split("\n"); test = list(map(lambda _:_.split(","),test)); test = test[:-1] #DROP last


train = open("artificial_with_noise_train.csv").read().split("\n"); train = list(map(lambda _:_.split(","),train)); train = train[:-1] #DROP last
test = open("artificial_with_noise_test.csv").read().split("\n"); test = list(map(lambda _:_.split(","),test)); test = test[:-1] #DROP last





class nb:
    output_vector_frequencies = defaultdict(int)
    N=0
    istrained=False

    def test(self,input_matrix,output_vector):
        N_correct=0
        if not self.istrained:
            print ("NOT TRAINED")
            return

        for line_index,line in enumerate(input_matrix):

            probability_tiny_polygon = self.P_tiny_polygon
            probability_other = self.P_other

            for element in line:
                probability_tiny_polygon *= self.fq_normed_tiny_polygon.get(element,0.0001)
                probability_other *= self.fq_normed_other.get(element,0.0001)

            ans_array = []
            if probability_tiny_polygon >= probability_other:
                ans = "tiny_polygon"
            else:
                ans = "other"
            ans_array.append(ans)
            if output_vector[line_index]==ans:
                N_correct += 1
        print("SUCCESS RATE {} ({} out of {})".format(100 * N_correct / len(output_vector), N_correct,
                                                      len(output_vector)))
        #return ans_array

    def train(self,input_matrix,output_vector):
        self.istrained=True
        self.N = len(output_vector)

        for out_class in output_vector:
            self.output_vector_frequencies[out_class] += 1

#        for out_class,how_much in self.output_vector_frequencies.items(): print(out_class,how_much)
        possible_y = []
        possible_y = self.output_vector_frequencies.keys()


        input_transposed = list(zip(*input_matrix))

        possible_attr = []
        for longrow in input_transposed:
            possible_attr.append(list(set(longrow)))

        fq = {'tiny_polygon':defaultdict(int), 'other':defaultdict(int)}

        for i,line in enumerate(input_matrix):
            for value in line:
                fq[output_vector[i]][value] += 1

                # TODO assuming: vsetky mozne value v input_matrix su distinct!!!!

        N_tiny_polygon = self.output_vector_frequencies['tiny_polygon']
        N_other = self.output_vector_frequencies['other']
        self.P_tiny_polygon = N_tiny_polygon/self.N
        self.P_other = N_other/self.N

        self.fq_normed_tiny_polygon = {k:v/N_tiny_polygon for k,v in fq['tiny_polygon'].items()}
        self.fq_normed_other = {k:v/N_other for k,v in fq['other'].items() }
        self.fq_normed_tiny_polygon['big'] = 0.0001 #UPS ;) :* :D
        self.fq_normed_tiny_polygon['circle'] = 0.001 #...

        print("(tiny polygon su ti co maju >50K!!)")



        #print (fq,N_tiny_polygon,N_other)
        #print ("\n\n\n")
        #print (self.fq_normed_other)
        #print (self.fq_normed_tiny_polygon)




#test adult dataset
inputs=[];outputs=[];

with open("adult.data.txt","r") as csv_train:
    csvreader = csv.reader(csv_train,delimiter=',')
    for row in csvreader:
        if type(row)==list:
            if len(row)>1:
                inputs.append(row[:-1])
                outputs.append(row[-1])

#select features...
inputs_transposed = list(zip(*inputs))
inputs_transposed_builder = []
for append_this in [0,1,3,6,7,8,9]:
    inputs_transposed_builder.append(inputs_transposed[append_this])

inputs = list(zip(*inputs_transposed_builder))
#print (inputs[1:20])

income_model = nb()
train_test_boundary_index =len(inputs)//10
income_model.train(inputs[train_test_boundary_index:],outputs[train_test_boundary_index:])
income_model.test(inputs[:train_test_boundary_index],outputs[:train_test_boundary_index])
sys.exit(0)
#test geometric objectts




single = nb()

inputs = []; outputs = [];

for a in train:
    inputs.append(a[0:3])
    outputs.append(a[3])


single.train(inputs,outputs)


inputs = []; outputs = [];

for a in test:
    inputs.append(a[0:3])
    outputs.append(a[3])

single.test(inputs,outputs)