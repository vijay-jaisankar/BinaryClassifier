# BinaryClassifier
A simple binary classifier that uses Scikit-Learn's tree object, more specifically, the sklearn.tree.DecisionTreeClassifier.fit(...) function.



This project makes use of DecisionTreeClassifer() in scikit-learn's tree object to determine the quadrant/axis an entered point belongs to.

A classifer is a mechanism that takes a look at a number of distinguishing 'features' and assigns an 'object' with a 'label'.

***

Example of Classifer:
Let a dairy company making milk and curd have two features it uses to distinguish its products:
Fat content(>=50% means HIGH fat and <50% means LOW fat)
Type of product(milk is M and curd is C)
So, an object of type (67,C) is CURD of HIGH fat content- it's label.

We then feed the computer 'test-cases' i.e sample products it can learn from. These include edge cases like (50,M) or (50,C).
The computer then 'learns' i.e deduces a relationship to distinguish between the objects. Note that distinguishability is key here, we don't want to have controversial/vague features.

The computer deduces a relationship of sorts it uses to deduce the 'label' for an object supplied.
It makes sense to include more test cases and more importantly, edge cases, to the computer.

***
This project takes in two parameters- x co-ordinate and y co-ordinate; and with the help of the 25 test cases provided, tells us if the point entered is on the X/Y axes, is the Origin, or in the 1st,2nd,3rd or 4th quadrants.

Please see the code for more information regarding the encoding and the implementation of the afore-mentioned logic.




