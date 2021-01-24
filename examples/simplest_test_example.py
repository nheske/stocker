#!/usr/bin/env python3

# Include the directory up in the path:
import sys
sys.path.insert(0,'..')
import stocker


# Main:
if __name__== "__main__":
    us_stock_portfolio = stocker.Portfolio(
      name="US Stocks", \
      value=1000000, \
      positions=[stocker.US_Stocks()], \
      weights=[1] \
    )

    simplest_scenario = stocker.Scenario(
      name="Simple Stock Growth", \
      portfolio=us_stock_portfolio, \
      num_years=5, \
      annual_contribution=0, \
      annual_contribution_increase_perc=0, \
    )

    # Run the scenario once and print and plot the results:
    simplest_scenario.run()
    print(simplest_scenario.results())
#    simplest_scenario.plot(smooth=False)

    # Run a monte carlo simulation of this scenario with 400 iterations:
    mc = stocker.Monte_Carlo(simplest_scenario)
    mc.run(n=100)

    # Print the results of the monte carlo simulation, showing the probablility of not running out of funds.
    print(mc.results(goal=0.0))

    # Create the monte carlo plots:
    # mc.histogram()
    mc.plot(smooth=False)

    # Show all the stocker plots:
    stocker.show_plots()
