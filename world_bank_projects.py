# install and import libraries : beautifulsoup4, lxml(parser)
from bs4 import BeautifulSoup
import requests
import pandas as pd

# gain access to the website
html_text = requests.get(
        'https://projects.worldbank.org/en/projects-operations/projects-list?os=40')
print(html_text)

# create a soup instance
soup = BeautifulSoup(html_text.text, 'lxml')

# get all data of the whole web page
projects = soup.find_all('tr', class_='ng-tns-c1-0 ng-star-inserted')
# print(projects)

for project in projects:
        project_title = project.find_next('td', class_='ng-tns-cl-0').text
        project_country = project.find_next('td', class_='ng-tns-cl-0').text
        project_id = project.find_next('td', class_='ng-tns-cl-0').text
        project_commitment_amount = project.find_next('td', class_='ng-tns-cl-0').text
        project_status = project.find_next('td', class_='ng-tns-cl-0').text
        project_approval_date = project.find_next('td', class_='ng-tns-cl-0').text
        project_last_updated_date = project.find_next('td', class_='ng-tns-cl-0').text
        project_last_stage_reached = project.find_next('td', class_='ng-tns-cl-0').text

        # NB to comment a bock of code use """ """
        #check if extracted successfully
        """
        print(f'''
            Project title : {project_title}
            Project Country : {project_country}
            Project ID : {project_id}
            Project Commitment Amount : {project_commitment_amount}
            Project status : {project_status}
            Project Approval date : {project_approval_date}
            Project last updated date : {project_last_updated_date}
            Project last stage reached : {project_last_stage_reached}
            ''')
        print('')
        """

        # initialize lists to append the data
        title_array = []
        id_array = []
        country_array = []
        commitment_amount_array = []
        status_array = []
        approval_date_array = []
        last_updated_date_array = []
        last_stage_reached_array = []

        #append the data extracted
        title_array.append(project_title)
        id_array.append(project_id)
        country_array.append(project_country)
        commitment_amount_array.append(project_commitment_amount)
        status_array.append(project_status)
        approval_date_array.append(project_approval_date)
        last_updated_date_array.append(project_last_updated_date)
        last_stage_reached_array.append(project_last_stage_reached)

        #check if appending is successful
        """
        print('title', title_array,
              'id', id_array,
              'country', country_array,
              'commitment_amount', commitment_amount_array,
              'project status', status_array,
              'approval date', approval_date_array,
              'last updated date', last_updated_date_array,
              'last stage reached', last_stage_reached_array,
              )
        """


        #add the appended data to a dataframe
        data = {'project title': title_array,
             'project id': id_array,
             'project country': country_array,
             'commitment amount': commitment_amount_array,
             'project status': status_array,
             'project approval date': approval_date_array,
             'project last apdated date': last_updated_date_array,
             'project last stage reched': last_stage_reached_array,
              }
        df = pd.DataFrame(data)
        print(df)
