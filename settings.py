base_url = "https://uspsa.org/"

classifier_url = base_url + "/calculator"
hit_factor_url = classifier_url + "/calculate"


def getClassifierUrl():
    return classifier_url


def getHitFactorUrl():
    return hit_factor_url
