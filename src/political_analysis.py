import matplotlib.pyplot as plt
import pandas as pd


def pol_analysis(df):

    # extract role and party column
    df_party = df[['role', 'party']]
    df_party = df_party.replace(['Bündnis 90/Die Grünen'], 'Bündnis 90 Die Grünen')

    for x in df_party.party.unique():
        result = df_party[df_party['party'] == str(x)]
        result['counts'] = result['role'].map(result['role'].value_counts())
        result.drop_duplicates(keep='last', inplace=True)

        plt.title('Distribution of nodes across roles \n Political party: ' + str(x))
        plt.xlabel('role')
        plt.ylabel('number of nodes')

        plt.bar(result.role, result.counts)
        plt.savefig(
            './plots/political_analysis/party/' + str(x).replace(' ', '_') + '.png')
        plt.close()

    # extract role and region column
    df_region = df[['role', 'region']]

    for x in df_region.region.unique():
        result = df_region[df_region['region'] == str(x)]
        result['counts'] = result['role'].map(result['role'].value_counts())
        result.drop_duplicates(keep='last', inplace=True)

        plt.title('Distribution of nodes across roles \n Region: ' + str(x))
        plt.xlabel('role')
        plt.ylabel('number of nodes')

        plt.bar(result.role, result.counts)
        plt.savefig(
            './plots/political_analysis/region/' + str(x).replace(' ', '_') + '.png')
        plt.close()

    # extract role and institution column
    df_institution = df[['role', 'institution']]

    for x in df_institution.institution.unique():
        result = df_institution[df_institution['institution'] == str(x)]
        result['counts'] = result['role'].map(result['role'].value_counts())
        result.drop_duplicates(keep='last', inplace=True)

        plt.title('Distribution of nodes across roles \n Political institution: ' + str(x))
        plt.xlabel('role')
        plt.ylabel('number of nodes')

        plt.bar(result.role, result.counts)
        plt.savefig(
            './plots/political_analysis/institution/' + str(x).replace(' ', '_') + '.png')
        plt.close()

    # extract role and office column
    df_office = df[['role', 'office']]

    for x in df_office.office.unique():
        result = df_office[df_office['office'] == str(x)]
        result['counts'] = result['role'].map(result['role'].value_counts())
        result.drop_duplicates(keep='last', inplace=True)

        plt.title('Distribution of nodes across roles \n Political office: ' + str(x))
        plt.xlabel('role')
        plt.ylabel('number of nodes')

        plt.bar(result.role, result.counts)
        plt.savefig(
            './plots/political_analysis/office/' + str(x).replace(' ', '_') + '.png')
        plt.close()

    # extract role and gender column
    df_gender = df[['role', 'gender']]

    for x in df_gender.gender.unique():
        result = df_gender[df_gender['gender'] == str(x)]
        result['counts'] = result['role'].map(result['role'].value_counts())
        result.drop_duplicates(keep='last', inplace=True)

        plt.title('Distribution of nodes across roles \n Gender: ' + str(x))
        plt.xlabel('role')
        plt.ylabel('number of nodes')

        plt.bar(result.role, result.counts)
        plt.savefig(
            './plots/political_analysis/gender/' + str(x).replace(' ', '_') + '.png')
        plt.close()

