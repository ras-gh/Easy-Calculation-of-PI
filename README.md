# Easy-Calculation-of-PI
An easy way to mathematically calculate the value of PI.

We often take PI for granted, but how was it originally calculated? (PI is classified as an irrational number which means its decimal value continues ad infinitum). The answer is that mathematicians have found several different mathematical series that, if carried out infinitely, will accurately calculate pi to a great number of decimal places. Some of these are so complex they require supercomputers to process them.
However, there is a much easier way to accurately approximate the value of pi mathematically.
The formula is to start with a simple approximation, ie 3, then add on to it the sine of that number.
ie. PI approximation = 3 + sin(3)  = 3.14112 (to 5 decimal places)
The result is accurate to within 3 decimal places, so we take 3.141 and add sin(3.141) to it.
Each time, a slightly more accurate value is produced, and we can increase the number of decimal places. I tested the above approximation by writing a simple program in Python. Inside the program I simply increased the number of decimal places by one on each iteration. We can comfortably double the number of decimal places on each iteration and still be accurate in the calculation.

The limitation is that it tops out at 15 decimal places when running in the terminal window.
However, this iteration could theoretically be performed ad infinitum to calculate pi.

