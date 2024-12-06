import pickle

from graphrole import RecursiveFeatureExtractor, RoleExtractor

# apply role extraction and sort nodes into definitive roles

def compute_roles(g):
    # extract features using graphrole library
    feature_extractor = RecursiveFeatureExtractor(g)
    features = feature_extractor.extract_features()

    # assign node roles
    role_extractor = RoleExtractor(n_roles=None)
    role_extractor.extract_role_factors(features)
    node_roles = role_extractor.roles

    # save node_roles locally
    pickle.dump(node_roles, open("./pickles/node_roles.pickle", "wb"))
    return node_roles
