# code is missing imports
from scipy import *
from numpy import *
from matplotlib.pyplot import *
from scipy import integrate
from scipy.optimize import fmin


t = linspace(0, 51, 52) # changed to match data file (please double-check)

# probably need to call loadtxt here, and make the
# vectors for death and week
data = loadtxt('p3 data.txt', delimiter=',')
week = data[:,0]
death = data[:,1]

def odeVecField(x, t, gama, beta):
    """
    The system we're solving is

        dS/dt = - beta S I

        dI/dt =   beta S I - gamma I

    in that order.  You've messed up the order
    in a way that creates a serious bug.

    gamma is spelled with 2 m's FYI
    """
    S = x[0]
    I = x[1]
    return array([-beta*S*I, beta*S*I-gama*I])

def Error2(parameters):
    # I0 = data[0] # data[:,0] has units of time, not people
    # S0 = data[1] # data[:,1] has units of deaths, not susceptible people
    #
    # I've changed the name "data" to "parameters" to avoid confusion
    # with the actual data set to which we are trying to fit the model.
    #
    S0 = parameters[0]
    I0 = parameters[1]
    x0 = array([S0, I0])
    beta = parameters[2]
    gama = parameters[3]
    x = integrate.odeint(odeVecField, x0, t, args=(gama, beta))
    I = x[:, 0]
    S = x[:, 1]
    # the loop below is close, but has 2 mistakes.
    # First, there is no reason to divide by "week".
    # Second, the "return" event should happen AFTER the loop FINISHES
    # However, you don't even need the loop -- you can do this using
    # vector arithmetic and the "sum" function
    #
    #while n < death.shape[0]:
    #        E = E + (death[n]/week[n] - beta*S[n]*I[n])**2
    #        n += 1
    #        return E
    E = sum((death - beta*S*I)**2)

def main():

    # moved these lines into your "main" function to
    # avoid potential name collisions with global variables
    Z0 = array([10000,1000,0.001,0.25])
    Zbest = fmin(Error2,Z0)
    print('fmin finds a minimum at approximately',Zbest)

    # set up our initial conditions
    S0 = 8.19569017e+03
    I0 = 1.06202593e+03
    x0 = array([S0, I0])

    # Parameters
    gama = 3.99778578e-01
    beta = 9.13222275e-05

    # choose the time's we'd like to know the approximate solution
    t = linspace(0, 51, 52)

    # and solve
    x = integrate.odeint(odeVecField, x0, t, args=(gama, beta))
    S = x[:, 0]
    I = x[:, 1]

    figure(1)
    subplot(3,1,1)
    plot(t,S)
    ylabel('Susceptibles (S)')
    subplot(3,1,2)
    plot(t,I)
    ylabel('Infecteds (I)')
    subplot(3,1,3)
    plot(t, beta*S*I)
    plot(t, death)
    xlabel("Weeks", fontsize=15)
    ylabel("Infection Rate", fontsize=15)
    show()


main()
