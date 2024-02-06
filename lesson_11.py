#1
'''
Write a function called `proportion_of_education` which returns the proportion of children in the dataset 
who had a mother with the education levels equal to less than high school (<12), high school (12), 
more than high school but not a college graduate (>12) and college degree.
'''
import pandas as pd

def proportion_of_education():
    # Load the dataset
    df = pd.read_csv('/home/albemute/Polytech-tasks/NISPUF17.csv')  # Replace with your actual file path

    # Assuming the column that represents mother's education level is named 'EDUC1'
    # The values in this column should represent the different education levels
    # Adjust the column name and value checks according to your dataset

    total_count = len(df)

    # Calculate proportions for each education level
    proportions = {
        "less than high school": len(df[df['EDUC1'] == '<12']) / total_count,
        "high school": len(df[df['EDUC1'] == '12']) / total_count,
        "more than high school but not college": len(df[df['EDUC1'] == '>12']) / total_count,
        "college": len(df[df['EDUC1'] == 'College']) / total_count
    }

    return proportions

# Example usage
proportions = proportion_of_education()
print(proportions)




#2
'''
Let's explore the relationship between being fed breastmilk as a child and getting a seasonal influenza vaccine from a healthcare provider. 
Return a tuple of the average number of influenza vaccines for those children we know received breastmilk as a child and those who know did not.
*This function should return a tuple in the form (use the correct numbers:*
(2.5, 0.1)
'''
file = '../home/albemute/Polytech-tasks/NISPUF17.csv'
data = pd.read_csv(file)

breastfed = data[data]






























