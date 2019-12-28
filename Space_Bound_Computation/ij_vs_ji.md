### Does it matter if the for loops are switched?
To answer that question, yes it does matter. This is because it changes the output. Say there are two martices, called A and B. If the loops
where to stay the same, you would be multiplying A * B. However, if the two loops were switched, it would not be same; you would be multiplying
B * A, which is completely different. In the first one, you would be taking the vertical for A and multiplying/adding it to the horizontial of B,
while in the second one you would be taking the vertical for B and multiplying/adding it to the horizontial of A, which will give out a completely different answer. 

As long as run time goes, they take the **same time to run**. Take a look at the graph of comparision between the two (https://github.com/GITHUBUSR01/personal-google-code-in/blob/master/Space_Bound_Computation/ij_vs_ji_graph.py). The graphs clearly shows that two lines are almost the same, expect for a slight difference near the top (for bigger martices), which is to be expected. This is because it will take different amounts of time to mutliply different martices, which is to be expected, because all of the random martices are different from one another. Looking at the two graphs, we can say, as long as time goes, they will take the same time to run.  
