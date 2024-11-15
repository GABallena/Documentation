import random

def randomize_sites(sites, stratify_by=None, num_groups=2, seed=None):
    # Set the seed for reproducibility
    if seed is not None:
        random.seed(seed)
    
    # If a stratification factor is provided, group sites based on that factor
    if stratify_by:
        stratified_groups = {}
        for site in sites:
            factor = site.get(stratify_by)
            if factor not in stratified_groups:
                stratified_groups[factor] = []
            stratified_groups[factor].append(site)

        # Assign sites within each stratified group to the specified number of groups
        randomized_groups = {i: [] for i in range(1, num_groups + 1)}
        for factor, factor_sites in stratified_groups.items():
            random.shuffle(factor_sites)
            for i, site in enumerate(factor_sites):
                group_number = (i % num_groups) + 1
                randomized_groups[group_number].append(site)

    else:
        # If no stratification, randomly assign all sites directly to groups
        random.shuffle(sites)
        randomized_groups = {i: [] for i in range(1, num_groups + 1)}
        for i, site in enumerate(sites):
            group_number = (i % num_groups) + 1
            randomized_groups[group_number].append(site)

    return randomized_groups

# Example setup
# List of site dictionaries, each with various potential stratification factors
sites = [
    {"id": 1, "location": "urban", "source": "residential", "season": "wet"},
    {"id": 2, "location": "rural", "source": "industrial", "season": "dry"},
    {"id": 3, "location": "urban", "source": "hospital", "season": "wet"},
    {"id": 4, "location": "rural", "source": "residential", "season": "dry"},
    # Add more sites as needed
]

# Set stratification factor, number of groups, and seed
stratify_by = None  # Set to "location", "source", "season", etc., or None for random sampling
num_groups = 2
seed = 42

# Get randomized site assignments
randomized_assignments = randomize_sites(sites, stratify_by=stratify_by, num_groups=num_groups, seed=seed)

# Print the results
for group, assigned_sites in randomized_assignments.items():
    print(f"Group {group}: {[site['id'] for site in assigned_sites]}")
