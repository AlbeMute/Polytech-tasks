#1
def proportion_of_education():
    data = { "education": [">12", "12", ">12", "college", "college", ">12", "12"] } # Example data
    total_children = len(data["education"])
    education_levels = ['less than high school', 'high school', 
                        'more than high school but not college', 'college']
    proportions = {}

    for level in education_levels:
        count = data["education"].count(level)
        proportion = count / total_children
        proportions[level] = proportion

    return proportions

#2
def average_influenza_doses():
    data = { "breastmilk": [True, False, True, True, False],
             "influenza_vaccine": [3, 0, 1, 2, 0] }  # Example data

    breastmilk_yes = []
    breastmilk_no = []

    for i in range(len(data["breastmilk"])):
        if data["breastmilk"][i]:
            breastmilk_yes.append(data["influenza_vaccine"][i])
        else:
            breastmilk_no.append(data["influenza_vaccine"][i])

    average_yes = sum(breastmilk_yes) / len(breastmilk_yes)
    average_no = sum(breastmilk_no) / len(breastmilk_no)

    return (average_yes, average_no)
