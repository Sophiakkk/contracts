import torch

# Custom optimizer setup function to set actor and critic learning rates
def custom_optimizer(policy, config):
    actor_params = policy.model.actor_parameters()
    critic_params = policy.model.critic_parameters()
    
    # Custom learning rates for actor and critic
    actor_lr = config.get("actor_lr", 1e-4)
    critic_lr = config.get("critic_lr", 1e-3)
    
    # Define separate optimizers
    actor_optimizer = torch.optim.Adam(actor_params, lr=actor_lr)
    critic_optimizer = torch.optim.Adam(critic_params, lr=critic_lr)
    
    return actor_optimizer, critic_optimizer