# Chingari Aptos

## Description
Chingari Aptos is a project that optimizes rewards for users participating in staking on the Aptos blockchain. It calculates dynamic rewards based on user stake and staking duration, considering market conditions like staking volume and volatility.

## Installation Instructions
To run this project, ensure you have Python installed. You can install the required dependencies using pip:

```bash
pip install requests
```

## Usage
To use the `AptosAgent` class, you need to set the smart contract address and run the script. Here is an example of how to use it:

```python
from aptos_agent import AptosAgent

if __name__ == "__main__":
    agent = AptosAgent()
    agent.update_rewards()
```

## Example
The following example demonstrates how to calculate the optimized reward for a user:

```python
from ai_reward_optimizer import AIRewardOptimizer

optimizer = AIRewardOptimizer()
user_stake = 1500 
staking_duration = 90 
reward = optimizer.calculate_dynamic_reward(user_stake, staking_duration)
print(f"Optimized Reward: {reward}")
```

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.

## Authors
- Subhranil Baul

## License
This project is licensed under the MIT License.
