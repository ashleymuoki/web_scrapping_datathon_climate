# install and import libraries : beautifulsoup4, lxml(parser)
from bs4 import BeautifulSoup
import requests
import pandas as pd

# gain access to the website
html_text = requests.get(
        'https://www.thegef.org/projects-operations/database?f%5B0%5D=focal_areas%3A2207&search=&page=2')
print(html_text)

# create a soup instance
soup = BeautifulSoup(html_text.text, 'lxml')

# get all data of the whole web page
projects = soup.find_all('tr')
# print(projects)

for project in projects:
        project_title = project.find_next('td', class_='views-field views-field-title').text
        project_id = project.find_next('td', class_='views-field views-field-field-gef-project-id is-active').text
        project_country = project.find_next('td', class_='views-field views-field-field-countries').text
        project_focal_area = project.find_next('td', class_='views-field views-field-field-focal-areas').text
        project_type = project.find_next('td', class_='views-field views-field-field-project-type').text
        project_agency = project.find_next('td', class_='views-field views-field-field-implementing-agencies').text
        project_grant = project.find_next('td', class_='views-field views-field-field-gef-project-grant').text
        project_cofinancing = project.find_next('td', class_='views-field views-field-field-co-financing-total').text
        project_status = project.find_next('td', class_='views-field views-field-field-latest-timeline-status').text

        # NB to comment a bock of code use """ """
        #check if extracted successfully
        """
        print(f'''
            Project title : {project_title}
            Project ID : {project_id}
            Project Country : {project_country}
            Project focal area : {project_focal_area}
            Project Type : {project_type}
            Project Agency : {project_agency}
            Project Grant : {project_grant}
            Project Co-financing : {project_cofinancing}
            Project Status : {project_status}
            ''')
        print('')
        """

        # initialize lists to append the data
        title_array = []
        id_array = []
        country_array = []
        focal_area_array = []
        type_array = []
        agency_array = []
        grant_array = []
        co_financing_array = []
        status_array = []

        #append the data extracted
        title_array.append(project_title)
        id_array.append(project_id)
        country_array.append(project_country)
        focal_area_array.append(project_focal_area)
        type_array.append(project_type)
        agency_array.append(project_agency)
        grant_array.append(project_grant)
        co_financing_array.append(project_cofinancing)
        status_array.append(project_status)

        #check if appending is successful
        """
        print('title', title_array,
              'id', id_array,
              'country', country_array,
              'focal area', focal_area_array,
              'project type', type_array,
              'agency', agency_array,
              'grant', grant_array,
              'co financing', co_financing_array,
              'status', status_array
              )
        """

        #add the appended data to a dataframe
        data = {'project title': title_array,
             'project id': id_array,
             'project country': country_array,
             'focal area': focal_area_array,
             'project type': type_array,
             'project agency': agency_array,
             'project grant': grant_array,
             'project co financing': co_financing_array,
             'project status': status_array
              }
        df = pd.DataFrame(data)
        print(df)
