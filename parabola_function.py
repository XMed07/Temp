import matplotlib.pyplot as plt
import numpy as np
import numbers



# Function to return the Maximum and Minimum values of the quadratic function
# return [min_Value, Max_value]
def findMaxMinValue(a, b, c) :

	# Calculate the value of second part
  secondPart = c * 1.0 - (b * b / (4.0 * a));
	
	# Print the values
  if (a > 0) :
    # Open upward parabola function
    #print("Maxvalue =", "Infinity");
    #print("Minvalue = ", secondPart);
    return ([secondPart,"Infinity"]);
		
  elif (a < 0) :
		
		# Open downward parabola function
		#print("Maxvalue = ", secondPart);
		#print("Minvalue =", "-Infinity");
    return (["-Infinity",secondPart]);
		
  else :
		
		# If a=0 then it is not a quadratic function
		#print("Not a quadratic function");
    return([None,None])

#=========  Main section  ============================
if __name__ == "__main__" :
	#The quadratic equation ax**2 + bx + c = Function
  a = 0.3  ; b = -2.4  ; c =  9
  min_max_values = findMaxMinValue(a, b, c);

  # This code is contributed by AnkitRai01

  ############## Draw function ########################### 
  # create 100 equally spaced points between 0 and 5
  x = np.linspace(0, 5, 100)

  # calculate the y value for each element of the x vector
  y = a*(x**2) + b*x + c

  fig, ax = plt.subplots()
  ax.plot(x, y)

  # draw roots
  real_roots = [t for t in min_max_values if isinstance(t, numbers.Number)]
  x_axe      = real_roots
  y_axe      = list(map(lambda x:  a*(x**2) + b*x + c, real_roots))
  ax.plot(x_axe, y_axe ,'r+')
  
  print("Min is:", real_roots);

  # show
  plt.show()
