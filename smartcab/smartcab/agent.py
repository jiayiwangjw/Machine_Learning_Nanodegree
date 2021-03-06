import random
import math
import numpy as np
from numpy.random import choice
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator
from math import cos

class LearningAgent(Agent):
    """ An agent that learns to drive in the Smartcab world.
        This is the object you will be modifying. """ 

    def __init__(self, env, learning=False, epsilon=0.97, alpha=0.1):
        super(LearningAgent, self).__init__(env)     # Set the agent in the evironment 
        self.planner = RoutePlanner(self.env, self)  # Create a route planner
        self.valid_actions = self.env.valid_actions  # The set of valid actions

        # Set parameters of the learning agent
        self.learning = learning # Whether the agent is expected to learn
        self.Q = dict()          # Create a Q-table which will be a dictionary of tuples
        self.epsilon = epsilon   # Random exploration factor
        self.epslion_ori = epsilon # used to store original epsilon value
        self.alpha = alpha       # Learning factor
        self.pre_state = None    # store previous state
        self.pre_action = None   # store previous action
        self.pre_reward = None   # store previous reward      
        self.iter = 0           # store the count of trial 
        ###########
        ## TO DO ##
        ###########
        # Set any additional class parameters as needed


    def reset(self, destination=None, testing=False):
        """ The reset function is called at the beginning of each trial.
            'testing' is set to True if testing trials are being used
            once training trials have completed. """

        # Select the destination as the new location to route to
        self.planner.route_to(destination)
        
        ########### 
        ## TO DO ##
        ###########
        # Update epsilon using a decay function of your choice
        # Update additional class parameters as needed
        # If 'testing' is True, set epsilon and alpha to 0
        self.iter = self.iter+1 
        if testing:
            self.epsilon = 0
            self.alpha = 0
        else:
            #self.epsilon = self.epsilon - 0.05 
            self.epsilon = np.power(self.epslion_ori, self.iter)
            

           
        return None

    def build_state(self):
        """ The build_state function is called when the agent requests data from the 
            environment. The next waypoint, the intersection inputs, and the deadline 
            are all features available to the agent. """

        # Collect data about the environment
        waypoint = self.planner.next_waypoint() # The next waypoint 
        inputs = self.env.sense(self)           # Visual input - intersection light and traffic
        deadline = self.env.get_deadline(self)  # Remaining deadline

        state = None
        """
        Previous Version (should not hard-coded the states)
        States:
            is_red_light: Whether the traffic light is red. (red: True, green: False)
            left_traffic: Whether a car comes from the left. (yes: True, no: False)
            oncoming_forward: Whether there is an oncoming car that moves forward. (yes: True, no: False)
            oncoming_right: Whether there is an oncoming car that turns right. (yes: True, no: False)
            waypoint: Recommended action for getting close to the destination ('forward', 'left', 'right')
        

        is_red_light =  True if inputs['light']  == 'red' else False
        left_traffic = True if (inputs['left'] and inputs['left'] == 'forward') else False
        oncoming_forward = True if (inputs['oncoming'] and inputs['oncoming'] == 'forward') else False
        oncoming_right = True if (inputs['oncoming'] and inputs['oncoming'] == 'right') else False
        
        """

        ########### 
        ## TO DO ##
        ###########
        # Set 'state' as a tuple of relevant data for the agent
        # When learning, check if the state is in the Q-table
        #   If it is not, create a dictionary in the Q-table for the current 'state'
        #   For each action, set the Q-value for the state-action pair to 0
             

        """
        States:
            is_red_light: Whether the traffic light is red. (red: True, green: False)
        """


        if self.learning:
            is_red_light =  True if inputs['light']  == 'red' else False
            state = (is_red_light, inputs['oncoming'], waypoint)


        
        return state


    def get_maxQ(self, state):
        """ The get_max_Q function is called when the agent is asked to find the
            maximum Q-value of all actions based on the 'state' the smartcab is in. """

        ########### 
        ## TO DO ##
        ###########
        # Calculate the maximum Q-value of all actions for a given state
        # should consider the 
        maxQ = max(self.Q[state].values())
        return maxQ 


    def createQ(self, state):
        """ The createQ function is called when a state is generated by the agent. """

        ########### 
        ## TO DO ##
        ###########
        # When learning, check if the 'state' is not in the Q-table
        # If it is not, create a new dictionary for that state
        #   Then, for each action available, set the initial Q-value to 0.0

        if self.learning and state not in self.Q.keys():
            self.Q[state] = {'left':0.0, 'right':0.0, 'forward':0.0, None: 0.0}

        return


    def choose_action(self, state):
        """ The choose_action function is called when the agent is asked to choose
            which action to take, based on the 'state' the smartcab is in. """

        # Set the agent state and default action
        self.state = state
        self.next_waypoint = self.planner.next_waypoint()
        action = random.choice(self.valid_actions) 


        ########### 
        ## TO DO ##
        ###########
        # When not learning, choose a random action
        # When learning, choose a random action with 'epsilon' probability
        #   Otherwise, choose an action with the highest Q-value for the current state

        if self.learning:
             # when learning a model, determine whether to choose a random action
            draw = choice(['random','learning'], 1, p=[self.epsilon, 1-self.epsilon]) 
            if draw == 'learning': 
                # for learning, we need to consider the case that more than one actions have 
                # the same highest Q value. In this case, we randomly choose an action with the 
                # highest Q value. 
                max_Q = self.get_maxQ(state) # get max Q value with the current state.
                best_actions = [action for action in self.valid_actions if self.Q[state][action] == max_Q]
                # list of actions that have the highest Q value
                action = random.choice(best_actions) # randomly choose a feasible action.


        return action


    def learn(self, state, action, reward):
        """ The learn function is called after the agent completes an action and
            receives an award. This function does not consider future rewards 
            when conducting learning. """

        """
        previous version: (should consider gamma as 0)
        if self.pre_state:
            # if previous state exists, current state can be used to update previous Q value. 
            old_Q = self.Q[self.pre_state][self.pre_action] # previous Q value
            current_max_action = self.get_maxQ(state) # get the action in future state with the max value.
            current_Q = self.Q[state][current_max_action] #
            self.Q[self.pre_state][self.pre_action] = old_Q + self.alpha * (self.pre_reward + current_Q - old_Q)
        else:
            # the first iteration set gamma = 0 that future Q value can be ignored.
            Q_value = self.Q[state][action]
            self.Q[state][action] = Q_value + self.alpha * (reward - Q_value)

        """
        ########### 
        ## TO DO ##
        ###########
        # When learning, implement the value iteration update rule
        #   Use only the learning rate 'alpha' (do not use the discount factor 'gamma')
        if self.learning:
            Q_value = self.Q[state][action]
            # update Q value
            self.Q[state][action] = Q_value + self.alpha * (reward - Q_value)

        return


    def update(self):
        """ The update function is called when a time step is completed in the 
            environment for a given trial. This function will build the agent
            state, choose an action, receive a reward, and learn if enabled. """

        state = self.build_state()          # Get current state
        self.createQ(state)                 # Create 'state' in Q-table
        action = self.choose_action(state)  # Choose an action
        reward = self.env.act(self, action) # Receive a reward
        self.learn(state, action, reward)   # Q-learn
        
        return
        

def run():
    """ Driving function for running the simulation. 
        Press ESC to close the simulation, or [SPACE] to pause the simulation. """

    ##############
    # Create the environment
    # Flags:
    #   verbose     - set to True to display additional output from the simulation
    #   num_dummies - discrete number of dummy agents in the environment, default is 100
    #   grid_size   - discrete number of intersections (columns, rows), default is (8, 6)
    env = Environment()
    
    ##############
    # Create the driving agent
    # Flags:
    #   learning   - set to True to force the driving agent to use Q-learning
    #    * epsilon - continuous value for the exploration factor, default is 1
    #    * alpha   - continuous value for the learning rate, default is 0.5
    agent = env.create_agent(LearningAgent, learning=True)
    #agent = env.create_agent(LearningAgent)
    
    ##############
    # Follow the driving agent
    # Flags:
    #   enforce_deadline - set to True to enforce a deadline metric
    env.set_primary_agent(agent, enforce_deadline=True)
    #env.set_primary_agent(agent)

    ##############
    # Create the simulation
    # Flags:
    #   update_delay - continuous time (in seconds) between actions, default is 2.0 seconds
    #   display      - set to False to disable the GUI if PyGame is enabled
    #   log_metrics  - set to True to log trial and simulation results to /logs
    #   optimized    - set to True to change the default log file name
    sim = Simulator(env, update_delay=0.01, log_metrics=True, optimized = True)
    #sim = Simulator(env, update_delay=0.01, log_metrics=True)
    #sim = Simulator(env)
    
    ##############
    # Run the simulator
    # Flags:
    #   tolerance  - epsilon tolerance before beginning testing, default is 0.05 
    #   n_test     - discrete number of testing trials to perform, default is 0
    sim.run(tolerance=0.01, n_test=20)
    #sim.run(n_test=10)
    #sim.run()


if __name__ == '__main__':
    run()
