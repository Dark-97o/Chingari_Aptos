import requests
import time
from ai_reward_optimizer import AIRewardOptimizer

APTOS_NODE = "https://fullnode.mainnet.aptoslabs.com" 
SMART_CONTRACT_ADDRESS = "0xYOUR_ACTUAL_CONTRACT_ADDRESS"  #contract address

class AptosAgent:
    def __init__(self):
        self.optimizer = AIRewardOptimizer()

    def fetch_stakers(self):
        response = requests.get(f"{APTOS_NODE}/v1/accounts/{SMART_CONTRACT_ADDRESS}/resources")
        if response.status_code == 200:
            return response.json()
        return {}

    def update_rewards(self):
        stakers = self.fetch_stakers()
        for staker in stakers:
            user_stake = staker.get("amount", 0)
            staking_duration = (time.time() - staker.get("stake_time", time.time())) / 86400
            optimized_reward = self.optimizer.calculate_dynamic_reward(user_stake, staking_duration)
            self.send_reward_transaction(staker["address"], optimized_reward)

    def send_reward_transaction(self, user_address, reward_amount):
        payload = {
            "type": "entry_function_payload",
            "function": f"{SMART_CONTRACT_ADDRESS}::staking::claim_rewards",
            "arguments": [user_address, int(reward_amount)],
        }
        response = requests.post(f"{APTOS_NODE}/v1/transactions", json=payload)
        if response.status_code == 202:
            print(f"Successfully updated rewards for {user_address}")
        else:
            print(f"Failed to update rewards: {response.text}")

if __name__ == "__main__":
    agent = AptosAgent()
    while True: 
        try:
            agent.update_rewards()
            time.sleep(3600) 
        except Exception as e:
            print(f"Error updating rewards: {e}") 
            time.sleep(60)
