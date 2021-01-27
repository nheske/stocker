#!/usr/bin/env python3

# Include the directory up in the path:
import sys
import time
import stocker
sys.path.insert(0,'..')


# Main:
if __name__== "__main__":
    us_stock_portfolio = stocker.Portfolio(
      name="US Stocks", \
      value=1000000, \
      positions=[stocker.US_Stocks()], \
      weights=[1] \
    )

    stock_test = stocker.Scenario(
      name="Stock Growth Test", \
      portfolio=us_stock_portfolio, \
      num_years=5, \
      annual_contribution=0, \
      annual_contribution_increase_perc=0, \
    )

    # Run the scenario once and print and plot the results:
    start = time.time()
    stock_test.run()
    print(stock_test.results())
#    simplest_scenario.plot(smooth=False)

    # Run a monte carlo simulation of this scenario:
    mc = stocker.Monte_Carlo(stock_test)
    mc.run(n=100)

    # Print the results of the monte carlo simulation, showing the probability of not running out of funds.
    print(mc.results(goal=0.0))
    print("Calculation Time:     "+str((time.time() - start)))
    # Create the monte carlo plots:
    # mc.histogram()
    mc.plot(smooth=False)

    # Show all the stocker plots:
    stocker.show_plots()
