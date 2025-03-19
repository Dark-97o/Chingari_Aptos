module StakeToEarn::staking {
    use aptos_framework::coin;
    use aptos_framework::timestamp;
    use aptos_framework::signer;
    use aptos_framework::vector;

    struct Staker {
        amount: u64,
        stake_time: u64,
        last_claim_time: u64,
    }

    struct StakePool {
        total_staked: u64,
        reward_rate: u64,
    }

    public fun initialize_staking_pool(account: &signer) {
        assert!(borrow_global_opt<StakePool>(signer::address_of(account)).is_none(), "Staking pool already exists."); 
        let pool = StakePool { total_staked: 0, reward_rate: 100 }; 
        move_to(account, pool);
    }

    public fun stake(account: &signer, amount: u64) {
        let staker = Staker { amount, stake_time: timestamp::now(), last_claim_time: timestamp::now() };
        move_to(account, staker);
    }

    public fun unstake(account: &signer) {
        let staker_address = signer::address_of(account);
        let staker = borrow_global_mut<Staker>(staker_address);
        assert!(staker.amount > 0, "No staked amount to unstake.");

        coin::transfer(account, signer::address_of(account), staker.amount);
        move_from<Staker>(staker_address);
    }

    public fun claim_rewards(account: &signer) {
        let staker_address = signer::address_of(account);
        let staker = borrow_global_mut<Staker>(staker_address);
        assert!(staker.amount > 0, "No staked amount to claim rewards.");

        let elapsed_time = timestamp::now() - staker.last_claim_time;
        let rewards = (elapsed_time / 86400) * staker.amount * (100 / 100);
        coin::transfer(account, signer::address_of(account), rewards);
        staker.last_claim_time = timestamp::now();

    }
}
