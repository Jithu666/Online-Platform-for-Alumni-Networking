# import json
from linkedin_api import Linkedin
import json


def extract_info(data):
    personal_info = {
        'first_name': data.get('firstName', 'N/A'),
        'last_name': data.get('lastName', 'N/A'),
        'birth_day': data.get('birthDate', {}).get('day', 'N/A'),
        'birth_month': data.get('birthDate', {}).get('month', 'N/A'),
        'profile_picture': data.get('profilePicture', {}).get('displayImage', 'N/A')
    }
    location_info = {
        'address': data.get('address', 'N/A'),
        'location_name': data.get('locationName', 'N/A'),
        'geo_country_name': data.get('geoCountryName', 'N/A')
    }
    
    professional_info = {
        'headline': data.get('headline', 'N/A'),
        'summary': data.get('summary', 'N/A'),
        'industry_name': data.get('industryName', 'N/A')
    }
    
    # Experience
    experience_list = []
    for exp in data.get('experience', []):
        experience = {
            'company_name': exp.get('companyName', 'N/A'),
            'title': exp.get('title', 'N/A'),
            'location_name': exp.get('locationName', 'N/A'),
            'start_month': exp.get('timePeriod', {}).get('startDate', {}).get('month', 'N/A'),
            'start_year': exp.get('timePeriod', {}).get('startDate', {}).get('year', 'N/A'),
            'end_month': exp.get('timePeriod', {}).get('endDate', {}).get('month', 'N/A'),
            'end_year': exp.get('timePeriod', {}).get('endDate', {}).get('year', 'N/A')
        }
        experience_list.append(experience)
    
    # Education
    education_list = []
    for edu in data.get('education', []):
        education = {
            'school_name': edu.get('schoolName', 'N/A'),
            'degree_name': edu.get('degreeName', 'N/A'),
            'field_of_study': edu.get('fieldOfStudy', 'N/A'),
            'start_month': edu.get('timePeriod', {}).get('startDate', {}).get('month', 'N/A'),
            'start_year': edu.get('timePeriod', {}).get('startDate', {}).get('year', 'N/A'),
            'end_month': edu.get('timePeriod', {}).get('endDate', {}).get('month', 'N/A'),
            'end_year': edu.get('timePeriod', {}).get('endDate', {}).get('year', 'N/A')
        }
        education_list.append(education)
    
    # Skills
    skills_list = [skill.get('name', 'N/A') for skill in data.get('skills', [])]
    
    # Compiling all extracted information into a dictionary
    extracted_info = {
        'personal_info': personal_info,
        'location_info': location_info,
        'professional_info': professional_info,
        'experience': experience_list,
        'education': education_list,
        'skills': skills_list
    }
    
    return extracted_info

username = 'ks@gmail.com'
password = '90*******2'
api = Linkedin(username, password)

# Specify the LinkedIn profile usernames
# profile_usernames = ["naveenkumars1003","sunaina-hanjura-51398314", "neel-raval", "sfehr", "chandra-cogentnext"]
profile_usernames="chandra-cogentnext"


alldata=api.get_profile(profile_usernames)
data=json.dumps(alldata, indent=4)
data = json.loads(data)
all=extract_info(data)
print("all",all)
